# API Reference

## Getting started

Check out the [getting started](/docs/getting_started_client) page to learn how to setup a script development environment.

Most interactions with the game state take place through the global access variable `wow`. For more information, check out the [globals](global/index) documentation.

## Lua script requirements

Each script AI should create an entrypoint script that defines a function `main`. The main function will be called every 50ms or so depending on server performance (referred to as a 'tick'). The function should read in game state data and perform actions as appropriate. The main function should return when processing is complete.

Even though most actions block (i.e. directly execute), it is possible to perform multiple actions per bot depending on the action (i.e. actions that don't affect GCD, like taking a pot or printing information). The following code snippet demonstrates having each bot activate both their trinkets in the same tick:

```lua
local has_used_trinkets = false

local function main()
    if not has_used_trinkets then
        for bot in each(wow.bots) do
            bot.trinket_1:use()
            bot.trinket_2:use()
        end
        has_used_trinkets = true
    end
end
```

It should be noted that the results of actions are not guaranteed to be immediately present in the game state data after an action is performed.

## Libraries

The lua scripting API supports libraries provides a set of 1st-party libraries that ship with lua. They are:

| Library                                                     | Description                                                    |
| ----------------------------------------------------------- | -------------------------------------------------------------- |
| [base](https://www.lua.org/manual/5.4/manual.html#6.1)      | Provides various basic functions like `ipairs`                 |
| [package](https://www.lua.org/manual/5.4/manual.html#6.3)   | Provides support for packages via require (and custom modules) |
| [coroutine](https://www.lua.org/manual/5.4/manual.html#6.2) | Provides support for coroutines, roughly 'parallel execution'  |
| [string](https://www.lua.org/manual/5.4/manual.html#6.4)    | Provides various features for working with strings             |
| [math](https://www.lua.org/manual/5.4/manual.html#6.7)      | Provides various functions for performing math via `math`      |
| [table](https://www.lua.org/manual/5.4/manual.html#6.6)     | Provides various tools to maniplate tables like `table.insert` |

### Json

A `json` library comes with the server and can be brought in by using `json = require("json")`. The json library used is [here](https://github.com/rxi/json.lua).

These are the functions available on the `json` module:

```lua
json.encode({ 1, 2, 3, { x = 10 } }) -- Returns '[1,2,3,{"x":10}]'
json.decode('[1,2,3,{"x":10}]') -- Returns { 1, 2, 3, { x = 10 } }
```

| Function | Description                                           | Parameters       | Return Type | Tested? |
| -------- | ----------------------------------------------------- | ---------------- | ----------- | ------- |
| encode   | Returns a string representing `value` encoded in JSON | `object` _data_  | `string`    | Yes     |
| decode   | Returns a value representing the decoded JSON string  | `string` _value_ | `object`    | Yes     |

### Custom Modules

`mangos-lua` supports custom modules that work in the same way they would with normal lua files using their relative path to the source root. Modules are importable through the same usage of `require`. Given the following files:

**modules/test.lua**

```lua
test = {}

function test.print_bot_name(bot)
    print(bot.name)
end

return test
```

**main.lua**

```lua
test = require("modules/test")

function main()
    for _, bot in ipairs(wow.bots) do
        test.print_bot_name(bot)
    end
end
```

The module import would work as expected and a list of bot names would be printed.

## Pointers

While memory objects are retained between ticks when created and managed in lua, all pointers to objects that are not managed by lua (e.g. a `Player` managed by the server) should not be trusted to persist at the same memory location between ticks. As such, it is recommended to only store value type objects provided by the API between ticks.

For example, the following code may be written to store bot CC assignments:

```lua
local cc_assignments = {}

local function main()
    for bot in each(wow.bots) do
        -- notice the usage of a pointer as the key
        if bot.class == wow.enums.classes.mage and not cc_assignments[bot] then
            cc_assignments[bot] = wow.raid_icons.moon
        end
    end
end
```

This strategy for storing CC assignments may seem appealing at first as it provides an easy way to uniquely identify and track assignments. For example, when individual mage behavior is being decided, the following code could be written:

```lua
-- in a mage decision function
local cc_target = cc_assignments[bot]
if cc_target then
    bot:cast(cc_target, POLYMORPH_SPELL_ID)
end
```

The issue arises in the next tick as the previous assignment would still be present with the previous pointer identifying the bot. When `cc_assignments` is indexed to see if the bot has an assignment, the bot pointer available will notmatch the original pointer by value. As such the mage Playerbot will not correctly cast the correct spell.

A better strategy might be to use the name of the bot as the key. Since it is a `string` and therefore a value type, it will represent the bot well between ticks. For example:

```lua
-- set
cc_assignments[bot.name] = wow.raid_icons.moon

-- get
local cc_target = cc_assignments[bot.name]
```

The bot object's `id` member would suffice as well.

Note- pointers provided from the API can be trusted to be consistent during the same tick. In the above example, if `cc_assignments` was repopulated at the beginning of each tick with the latest pointer, later iterations over the `wow.bots` array would provide the same pointers and equality would work as expected.

## Garbage Collection

The lua instance automatically garbage collects using internal best practices to retain high performance. Since the server understands that lua will be repeatedly executed, in each tick, after lua code execution, the server manually invokes garbage collection.

## Issues

Bug reports, suggestions, or any other questions should be created as issues [here](https://github.com/nate123456/mangos-lua/issues).
