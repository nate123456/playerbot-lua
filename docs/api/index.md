# API Reference

## Lua script requirements:

Each script AI should create an entrypoint script that defines a function `main`. The main function will be called every 50ms or so depending on server performance. The function should read in game state data and perform actions as appropriate. The main function should return when processing is complete.

Since actions are non-blocking, it is possible to perform multiple actions per bot depending on the action (i.e. actions that don't affect GCD, like taking a pot).

```lua
local has_printed = false

local function main()
    if not has_printed then
        for _, bot in ipairs(wow.bots) do
            print(bot.name)
        end
        has_printed = true
    end
end
```

## Modules

WoW lua scripting supports modules that work in the same way they would with normal lua files- they are importable through the same usage of `require` and function the same. Given the following files:

**test.lua**

```lua
test = {}

function test.print_bot_name(bot)
    print(bot.name)
end

return test
```

**main.lua**

```lua
test = require("test")

function main()
    for _, bot in ipairs(wow.bots) do
        test.print_bot_name(bot)
    end
end
```

The module import would work as expected.

Note- the `json` module comes with the server and can be brought in by using `json = require("json")`. Json library used is [here](https://github.com/rxi/json.lua).

### Functions

These are the functions available on the `json` module:

```lua
json.encode({ 1, 2, 3, { x = 10 } }) -- Returns '[1,2,3,{"x":10}]'
json.decode('[1,2,3,{"x":10}]') -- Returns { 1, 2, 3, { x = 10 } }
```

| Function | Description                                           | Parameters       | Return Type | Tested? |
| -------- | ----------------------------------------------------- | ---------------- | ----------- | ------- |
| encode   | Returns a string representing `value` encoded in JSON | `object` _data_  | `string`    | Yes     |
| decode   | Returns a value representing the decoded JSON string  | `string` _value_ | `object`    | Yes     |

For more information on the usage of the library, head to the link above.

                   | `object` _obj_     | `number`    | Yes     |
