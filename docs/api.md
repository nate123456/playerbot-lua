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

These are functions available on the json module:

```lua
json.encode({ 1, 2, 3, { x = 10 } }) -- Returns '[1,2,3,{"x":10}]'
json.decode('[1,2,3,{"x":10}]') -- Returns { 1, 2, 3, { x = 10 } }
```

| Function | Description                                           | Parameters       | Return Type | Tested? |
| -------- | ----------------------------------------------------- | ---------------- | ----------- | ------- |
| encode   | Returns a string representing `value` encoded in JSON | `object` _data_  | `string`    | Yes     |
| decode   | Returns a value representing the decoded JSON string  | `string` _value_ | `object`    | Yes     |

For more information on the usage of the library, head to the link above.

## Global

These are API features that are available in any context, accessible directly through their identifier.

### Members

These members are available anywhere. For example:

```lua
print(str(pi)) -- 3.14159265358979323846
```

| Name | Description                  | Return Type | Tested? |
| ---- | ---------------------------- | ----------- | ------- |
| pi   | pi to the 20th decimal place | `number`    | Yes     |

### Functions

These are functions available anywhere. All members are read-only. Usage example:

```lua
print(str(wow.time())) -- time in ticks
```

| Function | Description                                                                   | Parameters         | Return Type | Tested? |
| -------- | ----------------------------------------------------------------------------- | ------------------ | ----------- | ------- |
| print    | will generate a system message on the client that owns the environment        | `string` _message_ | none        | Yes     |
| log      | will send a log message to the log stream output (not necessarily the system) | `string` _message_ | none        | Yes     |
| str      | casts a lua object to a string (alias of `tostring`)                          | `object` _obj_     | `string`    | Yes     |
| num      | casts a lua object to a number (alias of `tonumber`)                          | `object` _obj_     | `number`    | Yes     |

## wow

Most state data is accessible through the readonly `wow` table.

### Members

These members are available anywhere. For example:

```lua
print(wow.master.name)
```

| Name             | Description                                                   | Return Type     | Tested? |
| ---------------- | ------------------------------------------------------------- | --------------- | ------- |
| command_message  | the last message sent as a command (from `.bot ai write ...`) | `string`        | No      |
| command_position | the last position sent as a command (from command spell)      | `Position`      | No      |
| bots             | All the bots that are managed by the master                   | `array<Bot>`    | No      |
| raid_icons       | All raid icon targets (nullable) ex. `raid_icons.skull`       | `table<Unit>`   | No      |
| master           | get the master                                                | `Player`        | Yes     |
| enums            | provides access to the enums table                            | `table`         | Yes     |
| group            | all group members                                             | `array<Player>` | Yes     |

### Functions

These are functions available anywhere. All members are read-only. Usage example:

```lua
print(str(wow.time())) -- time in ticks
```

| Function          | Description                                        | Parameters          | Return Type | Tested? |
| ----------------- | -------------------------------------------------- | ------------------- | ----------- | ------- |
| spell_exists      | get whether or not a spell is available            | `number` _spell_id_ | `bool`      | No      |
| time              | Get the current time in ticks since the epoch (ms) | `number`            | Yes         |
| spell_is_positive | get whether or not a spell is helpful or harmful   | `number` _spell_id_ | `bool`      | No      |

## Store

### Functions

These are functions available anywhere. All members are read-only. Usage example:

```lua
print(wow.store.get()) -- { "some_key": "some_value" }
```

The store allow for unstructured data to be saved between lua script sessions, i.g. getting and setting json strings.

| Function | Description                      | Parameters       | Return Type | Tested? |
| -------- | -------------------------------- | ---------------- | ----------- | ------- |
| get      | get data from persistent store   | none             | `string`    | Yes     |
| set      | set data from persistent store   | `string` _value_ | none        | Yes     |
| clear    | clear data from persistent store | none             | none        | Yes     |

## Enums

All enums provided to the lua environment consist of a table which can be indexed by the key or the value to get its corresponding value. The table can be access through `wow.enums`.

Enums allows for easy mapping between the ID for an item and its string representation or vice versa.

For example:

```lua
print(wow.enums.classes.3 ) -- Mage
print(wow.enums.classes.mage ) -- 3
print(wow.enums.classes[bot.class] ) -- Mage
```

### Classes

The `classes` enum allows for mapping from a class id to a readable string. The key is a `number` _id_ and the value is a `string` _name_. It is accessed through `wow.enums.classes`.

| Key | Value   |
| --- | ------- |
| 3   | mage    |
| 4   | warrior |
| 5   | warlock |
| 6   | priest  |
| 7   | druid   |
| 8   | rogue   |
| 9   | hunter  |
| 10  | paladin |
| 11  | shaman  |

### Specs

The `specs` enum allows for mapping from a class spec id to a readable string. The key is a `number` _id_ and the value is a `string` _name_. It is accessed through `wow.enums.specs`. For example:

```lua
print(wow.enums.specs.81 ) -- arcane
print(wow.enums.specs.arcane ) -- 81
print(wow.enums.specs[bot.spec] ) -- arcane
```

**Mage**

| Key | Value  |
| --- | ------ |
| 81  | arcane |
| 41  | fire   |
| 61  | frost  |

**Warrior**

| Key | Value      |
| --- | ---------- |
| 161 | arms       |
| 164 | fury       |
| 163 | protection |

**Rogue**

| Key | Value         |
| --- | ------------- |
| 182 | assassination |
| 181 | combat        |
| 183 | subtlety      |

**Priest**

| Key | Value      |
| --- | ---------- |
| 201 | discipline |
| 202 | holy       |
| 203 | shadow     |

**Shaman**

| Key | Value       |
| --- | ----------- |
| 261 | elemental   |
| 263 | enhancement |
| 262 | restoration |

**Druid**

| Key | Value       |
| --- | ----------- |
| 283 | balance     |
| 281 | feral       |
| 282 | restoration |

**Warlock**

| Key | Value       |
| --- | ----------- |
| 302 | affliction  |
| 303 | demonology  |
| 301 | destruction |

**Hunter**

| Key | Value         |
| --- | ------------- |
| 361 | beast_mastery |
| 363 | marksmanship  |
| 362 | survival      |

**Paladin**

| Key | Value       |
| --- | ----------- |
| 382 | holy        |
| 383 | protection  |
| 381 | retribution |

### Equip Slot

The `equip_slot` enum allows for mapping from a equip slot name to its corresponding. The key is a `string` _name_ and the value is a `number` _id_. It is accessed through `wow.enums.equip_slots`.

| Key       | Value |
| --------- | ----- |
| head      | 0     |
| neck      | 1     |
| shoulders | 2     |
| chest     | 3     |
| waist     | 5     |
| legs      | 6     |
| feet      | 7     |
| wrists    | 8     |
| hands     | 9     |
| finger_1  | 10    |
| finger_2  | 11    |
| trinket_1 | 12    |
| trinket_2 | 13    |
| back      | 14    |
| main_hand | 15    |
| off_hand  | 16    |
| ranged    | 17    |

### Spell Result

The `spell_result` enum allows for mapping from a spell result id to a readable string. The key is a `number` _id_ and the value is a `string` _name_. It is accessed through `wow.enums.spell_results`.

| Key | Value                                       |
| --- | ------------------------------------------- |
| 0   | SPELL_FAILED_AFFECTING_COMBAT               |
| 1   | SPELL_FAILED_ALREADY_AT_FULL_HEALTH         |
| 2   | SPELL_FAILED_ALREADY_AT_FULL_MANA           |
| 3   | SPELL_FAILED_ALREADY_AT_FULL_POWER          |
| 4   | SPELL_FAILED_ALREADY_BEING_TAMED            |
| 5   | SPELL_FAILED_ALREADY_HAVE_CHARM             |
| 6   | SPELL_FAILED_ALREADY_HAVE_SUMMON            |
| 7   | SPELL_FAILED_ALREADY_OPEN                   |
| 8   | SPELL_FAILED_AURA_BOUNCED                   |
| 9   | SPELL_FAILED_AUTOTRACK_INTERRUPTED          |
| 10  | SPELL_FAILED_BAD_IMPLICIT_TARGETS           |
| 11  | SPELL_FAILED_BAD_TARGETS                    |
| 12  | SPELL_FAILED_CANT_BE_CHARMED                |
| 13  | SPELL_FAILED_CANT_BE_DISENCHANTED           |
| 14  | SPELL_FAILED_CANT_BE_DISENCHANTED_SKILL     |
| 15  | SPELL_FAILED_CANT_BE_PROSPECTED             |
| 16  | SPELL_FAILED_CANT_CAST_ON_TAPPED            |
| 17  | SPELL_FAILED_CANT_DUEL_WHILE_INVISIBLE      |
| 18  | SPELL_FAILED_CANT_DUEL_WHILE_STEALTHED      |
| 19  | SPELL_FAILED_CANT_STEALTH                   |
| 20  | SPELL_FAILED_CASTER_AURASTATE               |
| 21  | SPELL_FAILED_CASTER_DEAD                    |
| 22  | SPELL_FAILED_CHARMED                        |
| 23  | SPELL_FAILED_CHEST_IN_USE                   |
| 24  | SPELL_FAILED_CONFUSED                       |
| 25  | SPELL_FAILED_DONT_REPORT                    |
| 26  | SPELL_FAILED_EQUIPPED_ITEM                  |
| 27  | SPELL_FAILED_EQUIPPED_ITEM_CLASS            |
| 28  | SPELL_FAILED_EQUIPPED_ITEM_CLASS_MAINHAND   |
| 29  | SPELL_FAILED_EQUIPPED_ITEM_CLASS_OFFHAND    |
| 30  | SPELL_FAILED_ERROR                          |
| 31  | SPELL_FAILED_FIZZLE                         |
| 32  | SPELL_FAILED_FLEEING                        |
| 33  | SPELL_FAILED_FOOD_LOWLEVEL                  |
| 34  | SPELL_FAILED_HIGHLEVEL                      |
| 35  | SPELL_FAILED_HUNGER_SATIATED                |
| 36  | SPELL_FAILED_IMMUNE                         |
| 37  | SPELL_FAILED_INTERRUPTED                    |
| 38  | SPELL_FAILED_INTERRUPTED_COMBAT             |
| 39  | SPELL_FAILED_ITEM_ALREADY_ENCHANTED         |
| 40  | SPELL_FAILED_ITEM_GONE                      |
| 41  | SPELL_FAILED_ITEM_NOT_FOUND                 |
| 42  | SPELL_FAILED_ITEM_NOT_READY                 |
| 43  | SPELL_FAILED_LEVEL_REQUIREMENT              |
| 44  | SPELL_FAILED_LINE_OF_SIGHT                  |
| 45  | SPELL_FAILED_LOWLEVEL                       |
| 46  | SPELL_FAILED_LOW_CASTLEVEL                  |
| 47  | SPELL_FAILED_MAINHAND_EMPTY                 |
| 48  | SPELL_FAILED_MOVING                         |
| 49  | SPELL_FAILED_NEED_AMMO                      |
| 50  | SPELL_FAILED_NEED_AMMO_POUCH                |
| 51  | SPELL_FAILED_NEED_EXOTIC_AMMO               |
| 52  | SPELL_FAILED_NOPATH                         |
| 53  | SPELL_FAILED_NOT_BEHIND                     |
| 54  | SPELL_FAILED_NOT_FISHABLE                   |
| 55  | SPELL_FAILED_NOT_FLYING                     |
| 56  | SPELL_FAILED_NOT_HERE                       |
| 57  | SPELL_FAILED_NOT_INFRONT                    |
| 58  | SPELL_FAILED_NOT_IN_CONTROL                 |
| 59  | SPELL_FAILED_NOT_KNOWN                      |
| 60  | SPELL_FAILED_NOT_MOUNTED                    |
| 61  | SPELL_FAILED_NOT_ON_TAXI                    |
| 62  | SPELL_FAILED_NOT_ON_TRANSPORT               |
| 63  | SPELL_FAILED_NOT_READY                      |
| 64  | SPELL_FAILED_NOT_SHAPESHIFT                 |
| 65  | SPELL_FAILED_NOT_STANDING                   |
| 66  | SPELL_FAILED_NOT_TRADEABLE                  |
| 67  | SPELL_FAILED_NOT_TRADING                    |
| 68  | SPELL_FAILED_NOT_UNSHEATHED                 |
| 69  | SPELL_FAILED_NOT_WHILE_GHOST                |
| 70  | SPELL_FAILED_NO_AMMO                        |
| 71  | SPELL_FAILED_NO_CHARGES_REMAIN              |
| 72  | SPELL_FAILED_NO_CHAMPION                    |
| 73  | SPELL_FAILED_NO_COMBO_POINTS                |
| 74  | SPELL_FAILED_NO_DUELING                     |
| 75  | SPELL_FAILED_NO_ENDURANCE                   |
| 76  | SPELL_FAILED_NO_FISH                        |
| 77  | SPELL_FAILED_NO_ITEMS_WHILE_SHAPESHIFTED    |
| 78  | SPELL_FAILED_NO_MOUNTS_ALLOWED              |
| 79  | SPELL_FAILED_NO_PET                         |
| 80  | SPELL_FAILED_NO_POWER                       |
| 81  | SPELL_FAILED_NOTHING_TO_DISPEL              |
| 82  | SPELL_FAILED_NOTHING_TO_STEAL               |
| 83  | SPELL_FAILED_ONLY_ABOVEWATER                |
| 84  | SPELL_FAILED_ONLY_DAYTIME                   |
| 85  | SPELL_FAILED_ONLY_INDOORS                   |
| 86  | SPELL_FAILED_ONLY_MOUNTED                   |
| 87  | SPELL_FAILED_ONLY_NIGHTTIME                 |
| 88  | SPELL_FAILED_ONLY_OUTDOORS                  |
| 89  | SPELL_FAILED_ONLY_SHAPESHIFT                |
| 90  | SPELL_FAILED_ONLY_STEALTHED                 |
| 91  | SPELL_FAILED_ONLY_UNDERWATER                |
| 92  | SPELL_FAILED_OUT_OF_RANGE                   |
| 93  | SPELL_FAILED_PACIFIED                       |
| 94  | SPELL_FAILED_POSSESSED                      |
| 95  | SPELL_FAILED_REAGENTS                       |
| 96  | SPELL_FAILED_REQUIRES_AREA                  |
| 97  | SPELL_FAILED_REQUIRES_SPELL_FOCUS           |
| 98  | SPELL_FAILED_ROOTED                         |
| 99  | SPELL_FAILED_SILENCED                       |
| 100 | SPELL_FAILED_SPELL_IN_PROGRESS              |
| 101 | SPELL_FAILED_SPELL_LEARNED                  |
| 102 | SPELL_FAILED_SPELL_UNAVAILABLE              |
| 103 | SPELL_FAILED_STUNNED                        |
| 104 | SPELL_FAILED_TARGETS_DEAD                   |
| 105 | SPELL_FAILED_TARGET_AFFECTING_COMBAT        |
| 106 | SPELL_FAILED_TARGET_AURASTATE               |
| 107 | SPELL_FAILED_TARGET_DUELING                 |
| 108 | SPELL_FAILED_TARGET_ENEMY                   |
| 109 | SPELL_FAILED_TARGET_ENRAGED                 |
| 110 | SPELL_FAILED_TARGET_FRIENDLY                |
| 111 | SPELL_FAILED_TARGET_IN_COMBAT               |
| 112 | SPELL_FAILED_TARGET_IS_PLAYER               |
| 113 | SPELL_FAILED_TARGET_IS_PLAYER_CONTROLLED    |
| 114 | SPELL_FAILED_TARGET_NOT_DEAD                |
| 115 | SPELL_FAILED_TARGET_NOT_IN_PARTY            |
| 116 | SPELL_FAILED_TARGET_NOT_LOOTED              |
| 117 | SPELL_FAILED_TARGET_NOT_PLAYER              |
| 118 | SPELL_FAILED_TARGET_NO_POCKETS              |
| 119 | SPELL_FAILED_TARGET_NO_WEAPONS              |
| 120 | SPELL_FAILED_TARGET_UNSKINNABLE             |
| 121 | SPELL_FAILED_THIRST_SATIATED                |
| 122 | SPELL_FAILED_TOO_CLOSE                      |
| 123 | SPELL_FAILED_TOO_MANY_OF_ITEM               |
| 124 | SPELL_FAILED_TOTEM_CATEGORY                 |
| 125 | SPELL_FAILED_TOTEMS                         |
| 126 | SPELL_FAILED_TRAINING_POINTS                |
| 127 | SPELL_FAILED_TRY_AGAIN                      |
| 128 | SPELL_FAILED_UNIT_NOT_BEHIND                |
| 129 | SPELL_FAILED_UNIT_NOT_INFRONT               |
| 130 | SPELL_FAILED_WRONG_PET_FOOD                 |
| 131 | SPELL_FAILED_NOT_WHILE_FATIGUED             |
| 132 | SPELL_FAILED_TARGET_NOT_IN_INSTANCE         |
| 133 | SPELL_FAILED_NOT_WHILE_TRADING              |
| 134 | SPELL_FAILED_TARGET_NOT_IN_RAID             |
| 135 | SPELL_FAILED_DISENCHANT_WHILE_LOOTING       |
| 136 | SPELL_FAILED_PROSPECT_WHILE_LOOTING         |
| 137 | SPELL_FAILED_PROSPECT_NEED_MORE             |
| 138 | SPELL_FAILED_TARGET_FREEFORALL              |
| 139 | SPELL_FAILED_NO_EDIBLE_CORPSES              |
| 140 | SPELL_FAILED_ONLY_BATTLEGROUNDS             |
| 141 | SPELL_FAILED_TARGET_NOT_GHOST               |
| 142 | SPELL_FAILED_TOO_MANY_SKILLS                |
| 143 | SPELL_FAILED_TRANSFORM_UNUSABLE             |
| 144 | SPELL_FAILED_WRONG_WEATHER                  |
| 145 | SPELL_FAILED_DAMAGE_IMMUNE                  |
| 146 | SPELL_FAILED_PREVENTED_BY_MECHANIC          |
| 147 | SPELL_FAILED_PLAY_TIME                      |
| 148 | SPELL_FAILED_REPUTATION                     |
| 149 | SPELL_FAILED_MIN_SKILL                      |
| 150 | SPELL_FAILED_NOT_IN_ARENA                   |
| 151 | SPELL_FAILED_NOT_ON_SHAPESHIFT              |
| 152 | SPELL_FAILED_NOT_ON_STEALTHED               |
| 153 | SPELL_FAILED_NOT_ON_DAMAGE_IMMUNE           |
| 154 | SPELL_FAILED_NOT_ON_MOUNTED                 |
| 155 | SPELL_FAILED_TOO_SHALLOW                    |
| 156 | SPELL_FAILED_TARGET_NOT_IN_SANCTUARY        |
| 157 | SPELL_FAILED_TARGET_IS_TRIVIAL              |
| 158 | SPELL_FAILED_BM_OR_INVISGOD                 |
| 159 | SPELL_FAILED_EXPERT_RIDING_REQUIREMENT      |
| 160 | SPELL_FAILED_ARTISAN_RIDING_REQUIREMENT     |
| 161 | SPELL_FAILED_NOT_IDLE                       |
| 162 | SPELL_FAILED_NOT_INACTIVE                   |
| 163 | SPELL_FAILED_PARTIAL_PLAYTIME               |
| 164 | SPELL_FAILED_NO_PLAYTIME                    |
| 165 | SPELL_FAILED_NOT_IN_BATTLEGROUND            |
| 166 | SPELL_FAILED_ONLY_IN_ARENA                  |
| 167 | SPELL_FAILED_TARGET_LOCKED_TO_RAID_INSTANCE |
| 168 | SPELL_FAILED_UNKNOWN                        |
| 253 | SPELL_FAILED_PVP_CHECK                      |
| 254 | SPELL_NOT_FOUND                             |
| 255 | SPELL_CAST_OK                               |

# Types

This section outlines each type and its members and functions. All members for all types are read-only and are accessed through the dot or period accessor, i.e. `bot.name`. All functions for all types are accessed through the colon accessor, i.e. `bot:stand()`.

## Player

This type represents the player. It inherits all API functionality from `Object`, `WorldObject`, and `Unit`.

### Members

The following are members of `Player`. All members are read-only. For example:

```lua
print("Last message: " .. some_bot.last_message)
```

| Name         | Description                                                   | Return Type                        | Tested? |
| ------------ | ------------------------------------------------------------- | ---------------------------------- | ------- |
| last_message | the last whisper or party/raid message (only player messages) | `string`                           | Yes     |
| class        | the player's class id- see the class enum [class](#classes)   | `number`                           | No      |
| inventory    | all the items in the player's backpack(s)                     | `array<Item>`                      | No      |
| trinket_1    | the player's first trinket                                    | `Item`                             | Yes     |
| trinket_2    | the player's second trinket                                   | `Item`                             | Yes     |
| destination  | the player's destination (if given a movement command)        | `number` x, `number` y, `number` z | No      |
| spec         | The player's deepest tree specialization                      | `number`                           | No      |
| party        | the player's party number (i.e. the number in the raid panel) | `number`                           | No      |

### Functions

The following are callable on a `Player`. Most of these functions perform an action. It is recommended to only choose one action to perform per tick. Responsible use is left to the developer. Example usage:

```lua
some_bot:whisper(wow.master, "I'm alive!")
```

| Function               | Description                                                                            | Parameters                                             | Return Type                                               | Tested?                 |
| ---------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------- | ----------------------- |
| follow                 | follow a unit                                                                          | `Unit` _target_, `number` _distance_, `number` _angle_ | none                                                      | Yes                     |
| stand                  | have the bot stand up                                                                  | none                                                   | none                                                      | No                      |
| sit                    | have the bot sit down                                                                  | none                                                   | none                                                      | No                      |
| kneel                  | have the bot kneel                                                                     | none                                                   | none                                                      | No                      |
| interrupt              | stop casting/channeling                                                                | none                                                   | none                                                      | Yes                     |
| move                   | move to a position                                                                     | `(x, y, z)` or `Unit` or `Position`                    | none                                                      | No                      |
| chase                  | chase a target                                                                         | `Unit` _target_, `number` distance, `number` angle     | none                                                      | No                      |
| set_chase_distance     | add distance while chasing a target                                                    | `number` distance                                      | none                                                      | No                      |
| teleport_to            | teleport to a unit                                                                     | `Unit` _target_                                        | none                                                      | Yes                     |
| reset_movement         | stops the player from moving and clears all movement tasks (i.e. follow, chase)        | none                                                   | none                                                      | No                      |
| stop                   | stops the player from moving                                                           | none                                                   | none                                                      | No                      |
| whisper                | whisper a player                                                                       | `Player` _target_, `string` _text_                     | none                                                      | Yes                     |
| tell_party             | send a message to party chat                                                           | `string` _text_                                        | none                                                      | Yes                     |
| tell_raid              | send a message to raid chat                                                            | `string` _text_                                        | none                                                      | Yes                     |
| say                    | send a message to local area                                                           | `string` _text_                                        | none                                                      | Yes                     |
| yell                   | yell a message to local area                                                           | `string` _text_                                        | none                                                      | Yes                     |
| set_target             | set the bot's target                                                                   | `Unit` _target_                                        | none                                                      | Yes                     |
| clear_target           | clear the bot's target                                                                 | none                                                   | none                                                      | Yes                     |
| clear_stealth          | clears stealth state                                                                   | none                                                   | none                                                      | Yes                     |
| face                   | faces the given target or orientation                                                  | `Unit` _target_ or `number` _orientation_              | none                                                      | Yes                     |
| has_power_to_cast      | checks to see if bot has enough power (mana, energy, etc.) to cast a given spell       | `number` _spell_id_                                    | `bool`                                                    | Yes                     |
| can_cast               | returns of if the bot can cast a spell (checks cooldown, silenced, etc.)               | `number` _spell_id_                                    | `bool`                                                    | Yes (doesn't check gcd) |
| get_cast_time          | Get the cast time of the provided spell id                                             | `number` _spell_id_                                    | `number` (ms)                                             | No                      |
| get_item_in_equip_slot | gets the item in the passed [equip_slot](#equip-slot)                                  | `number` _slot_                                        | `Item` (nullable)                                         | No                      |
| get_item               | locates the first item matching the name (case sensitive) or id in inventory           | `string` _name_ or `number`                            | `Item` (nullable)                                         | No                      |
| cast                   | attempts to cast a spell- will cast on self if no target is provided                   | `Unit` _target_ (optional), `number` _spell_id_        | `SpellCastResult` (`enum` or `number`, 255 means success) | Yes                     |
| force_cast             | will interrupt current cast before casting- will cast on self if no target is provided | `Unit` _target_ (optional), `number` _spell_id_        | `SpellCastResult` (`enum` or `number`, 255 means success) | Yes                     |
| in_same_party_as       | will return whether or not the player is in the same party as the given player         | `Player` _target_                                      | `bool`                                                    | Yes                     |

## Unit

This type represents a unit, which can be a player, creature, npc, or pet. It inherits all API functionality from `Object` and `WorldObject`. All members and functions are read-only.

### Members

The following are members of `Unit`. All members are read-only. For example:

```lua
print("Raid Icon: " .. some_unit.in_combat)
```

| Name                | Description                                                      | Return Type                    | Tested? |
| ------------------- | ---------------------------------------------------------------- | ------------------------------ | ------- |
| bounding_radius     | the bounding radius of the unit i.e. '_thiccness_'               | `number`                       | Yes     |
| pet                 | the unit's pet                                                   | `Pet`                          | Yes     |
| in_combat           | whether or not the unit is in combat                             | `bool`                         | Yes     |
| raid_icon           | the units raid icon                                              | `number` 0-7 (255 for no icon) | Yes     |
| attackers           | all units with threat on unit                                    | `list<Unit>`                   | No      |
| target              | the unit's target                                                | `Unit`                         | Yes     |
| is_alive            | whether or not the unit is alive                                 | `bool`                         | Yes     |
| crowd_controlled    | whether or not the unit is CC'd (not used by original playerbot) | `bool`                         | No      |
| health              | current hit points                                               | `number`                       | Yes     |
| max_health          | max hit points                                                   | `number`                       | Yes     |
| power               | current power (mana, energy, etc.)                               | `number`                       | Yes     |
| max_power           | max power (mana, energy, etc.)                                   | `number`                       | Yes     |
| current_cast        | the spell the unit is casting (0 if not found)                   | `number`                       | No      |
| current_auto_attack | the auto attack spell the unit is casting (0 if not found)       | `number`                       | No      |
| current_channel     | the channel spell the unit is casting (0 if not found)           | `number`                       | No      |

### Functions

The following are functions that can be called on a `Unit`. All functions are read-only. Example usage:

```lua
print("Bot threat: " .. some_unit:get_threat(some_bot))
```

| Function       | Description                                                           | Parameters                                     | Return Type | Tested? |
| -------------- | --------------------------------------------------------------------- | ---------------------------------------------- | ----------- | ------- |
| is_attacked_by | whether or not the given unit is attacking the unit                   | `Unit` _target_                                | `bool`      | No      |
| get_threat     | get the threat the given target has on the unit                       | `Unit` _target_                                | `number`    | No      |
| in_melee_range | get whether or not the given target is reachable with melee           | `Unit` _target_                                | `bool`      | Yes     |
| is_enemy       | whether or not the unit can attack the given unit                     | `Unit` _target_                                | `bool`      | Yes     |
| is_friendly    | whether or not the unit can assist (not /assist) the given unit       | `Unit` _target_                                | `bool`      | Yes     |
| get_aura       | get the first instance of an aura affecting the unit for the given id | `number` _aura_id_, `Unit` _caster_ (optional) | `Aura`      | No      |

## Creature

This type represents a creature. It inherits all API functionality from `Object`, `WorldObject`, and `Unit`. All members and functions are read-only.

### Members

The following are members of `Creature`. All members are read-only. For example:

```lua
print("Creature is elite: " .. some_creature.is_elite)
```

| Name           | Description                                                                          | Return Type | Tested? |
| -------------- | ------------------------------------------------------------------------------------ | ----------- | ------- |
| is_elite       | whether or not the creature is elite                                                 | `bool`      | No      |
| is_world_boss  | whether or not the creature is a world boss                                          | `bool`      | No      |
| can_aggro      | whether or not the creature can be aggro'd                                           | `bool`      | No      |
| is_totem       | whether or not the creature is a totem                                               | `bool`      | No      |
| is_invisible   | whether or not the creature is invisible (could be exploit?)                         | `bool`      | No      |
| is_civilian    | whether or not the creature is a civilian                                            | `bool`      | No      |
| is_critter     | whether or not the creature is a critter                                             | `bool`      | No      |
| is_regen_hp    | whether or not the creature is regenerating health (no sure what this means exactly) | `bool`      | No      |
| is_regen_power | whether or not the creature is regenerating hp (not sure what this means exactly)    | `bool`      | No      |
| can_walk       | whether or not the creature can walk                                                 | `bool`      | No      |
| can_swim       | whether or not the creature can swim                                                 | `bool`      | No      |
| can_fly        | whether or not the creature can fly                                                  | `bool`      | No      |

## Object

This type represents a generic object. All members and functions are read-only.

### Members

The following are members of `Object`. All members are read-only. For example:

```lua
print("Object is player: " .. some_object.is_player)
```

| Name           | Description                                 | Return Type | Tested?      |
| -------------- | ------------------------------------------- | ----------- | ------------ |
| is_player      | whether or not the object is a `Player`     | `bool`      | Yes          |
| is_creature    | whether or not the object is a `Creature`   | `bool`      | Yes          |
| is_game_object | whether or not the object is a `GameObject` | `bool`      | Hard to test |
| is_unit        | whether or not the object is a `Unit`       | `bool`      | Yes          |

### Functions

The following are callable functions on any `Object`. All functions are read-only.

```lua
print("Last Message: " .. some_object:as_player().last_message)
```

| Function       | Description                        | Parameters | Return Type  | Tested? |
| -------------- | ---------------------------------- | ---------- | ------------ | ------- |
| as_player      | casts the object to a `Player`     | none       | `Player`     | No      |
| as_creature    | casts the object to a `Creature`   | none       | `Creature`   | No      |
| as_game_object | casts the object to a `GameObject` | none       | `GameObject` | No      |
| as_unit        | casts the object to a `Unit`       | none       | `Unit`       | No      |

Note- these functions are required to be able to access the corresponding members and functions for that object type.

## WorldObject

This type represents a generic object. It inherits all API functionality from `Object`. All members and functions are read-only.

### Members

The following are members of `WorldObject`. All members are read-only. For example:

```lua
print("Enemy orientation: " .. enemy.orientation)
```

| Name        | Description              | Return Type | Tested? |
| ----------- | ------------------------ | ----------- | ------- |
| orientation | the object's orientation | `number`    | Yes     |
| name        | the object's name        | `string`    | Yes     |
| zone_id     | the object's Zone Id     | `number`    | No      |
| area_id     | the object's Area Id     | `number`    | No      |
| position    | the object's position    | `Position`  | Yes     |

### Functions

The following are callable functions on any `WorldObject`. All functions are read-only.

```lua
print("Bot A angle to bot b: " .. bot_a:get_angle(bot_b))
```

| Function        | Description                                                      | Parameters                                                                     | Return Type                              | Tested? |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------- | ------- |
| get_angle       | get the angle of given object                                    | `WorldObject` _world_object_ or `Position` _pos_ or `number` _x_, `number` _y_ | `number`                                 | No      |
| get_close_point | get a point close to the object                                  | `number` _bounding_radius_, `number` _distance_, `number` _angle_              | `number` _x_, `number` _y_, `number` _z_ |
| has_in_arc      | whether or not the given target is in the object's arc           | `Unit` _target_                                                                | `bool`                                   | No      |
| is_within_los   | whether or not the given target is in the object's line of sight | `Unit` _target_                                                                | `bool`                                   | No      |
| is_in_range     | whether or not the given target is in range of the given spell   | `Unit` _target_, `number` _spell_id_                                           | `bool`                                   | No      |
| gcd             | global cooldown remaining for the given spell, 0 if ready        | `number` _spell_id_                                                            | `number` (remaining time)                | No      |

Note- functions with muliple returns can be unpacked like so:

```lua
x, y, z = unpack(some_obj:get_close_point(1, 1, 1))
```

## GameObject

This type represents a game object. It inherits all API functionality from `Object` and `WorldObject`. All members and functions are read-only.

### Members

The following are members of `GameObject`. All members are read-only. For example:

```lua
print("Owner: " .. some_game_object.owner.name)
```

| Name   | Description                         | Return Type | Tested? |
| ------ | ----------------------------------- | ----------- | ------- |
| in_use | whether or not the object is in use | `bool`      | No      |
| owner  | the owner of the game object        | `Unit`      | No      |
| level  | the level of the game object        | `number`    | No      |

### Functions

The following are callable functions on any `GameObject`. All functions are read-only.

```lua
-- :(
```

| Function | Description | Parameters | Return Type | Tested? |
| -------- | ----------- | ---------- | ----------- | ------- |

## Position

This type represents a position. All members and functions are read-only.

### Members

The following are members of `Position`. All members are read-only. For example:

```lua
print("Pos X: " .. pos.x)
```

| Name     | Description                                          | Return Type | Tested? |
| -------- | ---------------------------------------------------- | ----------- | ------- |
| x        | get the x value of the position                      | `number`    | Yes     |
| y        | get the y value of the position                      | `number`    | Yes     |
| z        | get the z value of the position                      | `number`    | Yes     |
| o        | get the orientation value of the position            | `number`    | Yes     |
| is_empty | whether or not the position is empty (treat as null) | `number`    | no      |

### Functions

The following are callable functions on any `Position`. All functions are read-only.

```lua
print("Distance: " .. pos_1:get_distance_between(pos_2))
```

| Function        | Description                            | Parameters                                       | Return Type | Tested? |
| --------------- | -------------------------------------- | ------------------------------------------------ | ----------- | ------- |
| get_distance_to | get the distance between two positions | `Position` _other_                               | `number`    | Yes     |
| get_angle       | get the angle to a given position      | `Position` _other_ or `number` _x_, `number` _y_ | `number`    | Yes     |

## Pet

This type represents a pet. It inherits all API functionality from `Creature`, `Unit`, `WorldObject`, and `Object`.

### Members

The following are members of `Pet`. For example:

```lua
print("Pet owner: " .. pet_owner.name)
```

| Name        | Description                               | Return Type                                      | Tested? |
| ----------- | ----------------------------------------- | ------------------------------------------------ | ------- |
| pet_owner   | the pet's owner (better the owner member) | `Player`                                         | No      |
| happiness   | the pet's happiness                       | `number` 1: unhappy, 2: content, 3: happy        | No      |
| is_feeding  | whether or not the pet is feeding         | `bool`                                           | No      |
| react_state | get or set the pet's reaction state       | `number` 0: passive, 1: defensive, 2: aggressive | No      |

### Functions

The following are callable functions on any `Pet`.

```lua
-- :(
some_pet:summon()
```

| Function     | Description                                                          | Parameters                            | Return Type      | Tested? |
| ------------ | -------------------------------------------------------------------- | ------------------------------------- | ---------------- | ------- |
| set_autocast | set autocast for the given ability                                   | `number` _spell_id_, `bool` _enabled_ | none             | No      |
| summon       | summon the pet                                                       | none                                  | none             | No      |
| dismiss      | dismiss the pet                                                      | none                                  | none             | No      |
| attempt_feed | find food in the owner's inventory and attempt to feed it to the pet | none                                  | `bool` (success) | No      |

## Aura

This type represents an aura, buff, or debuff.

### Members

The following are members of `Aura`. For example:

```lua
    print("duration: " .. some_aura.duration)
```

| Name         | Description               | Return Type | Tested? |
| ------------ | ------------------------- | ----------- | ------- |
| stacks       | aura's stack count        | `number`    | No      |
| duration     | aura's remaining duration | `number`    | No      |
| max_duration | aura's maximum duration   | `number`    | No      |
| charges      | aura's charge count       | `number`    | No      |
| caster       | the caster of the aura    | `Unit`      | No      |

## Item

This type represents an item. It inherits all functionality from `Object`. All members are read-only.

### Members

The following are members of `Item`. For example:

```lua
    print("item stack count: " .. some_item.stack_count)
```

| Name            | Description                                                                                    | Return Type | Tested? |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------- | ------- |
| stack_count     | the item's stack count                                                                         | `number`    | No      |
| is_potion       | whether or not the item is a potion                                                            | `bool`      | No      |
| max_stack_count | the item's highest stack count before it makes another stack                                   | `number`    | No      |
| id              | the item's generic Id (not the id of the instance of the item)                                 | `number`    | No      |
| name            | the name of the item                                                                           | `string`    | No      |
| spell_id        | the item's associated spell id (if it can be 'cast')                                           | `number`    | No      |
| is_ready        | whether or not the associated spell is ready (returns false if the item does not have a spell) | `bool`      | No      |

### Functions

The following are callable functions on any `Item`.

```lua
some_item:use()
```

| Function | Description                                                                                       | Parameters                                                        | Return Type | Tested? |
| -------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------- | ------- |
| use      | use an item on either the given slot, target, or game object. will use self if no target provided | `number` _slot_ (0 - 18) or `Item` _target_ `GameObject` _target_ | none        | Yes     |
| destory  | destroy an item.                                                                                  | none                                                              | none        | Yes     |
