# Player

This type represents the player. It inherits all API functionality from `Object`, `WorldObject`, and `Unit`.

## Members

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

## Functions

The following are callable on a `Player`. Most of these functions perform an action. It is recommended to only choose one action to perform per tick. Responsible use is left to the developer. Example usage:

```lua
some_bot:whisper(wow.master, "I'm alive!")
```

| Function               | Description                                                                      | Parameters                                             | Return Type       | Tested? |
| ---------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------- | ------- |
| follow                 | follow a unit                                                                    | `Unit` _target_, `number` _distance_, `number` _angle_ | none              | Yes     |
| stand                  | have the bot stand up                                                            | none                                                   | none              | No      |
| sit                    | have the bot sit down                                                            | none                                                   | none              | No      |
| kneel                  | have the bot kneel                                                               | none                                                   | none              | No      |
| interrupt              | stop casting/channeling                                                          | none                                                   | none              | Yes     |
| move                   | move to a position                                                               | `(x, y, z)` or `Unit` or `Position`                    | none              | No      |
| chase                  | chase a target                                                                   | `Unit` _target_, `number` distance, `number` angle     | none              | No      |
| set_chase_distance     | add distance while chasing a target                                              | `number` distance                                      | none              | No      |
| teleport_to            | teleport to a unit                                                               | `Unit` _target_                                        | none              | Yes     |
| reset_movement         | stops the player from moving and clears all movement tasks (i.e. follow, chase)  | none                                                   | none              | No      |
| stop                   | stops the player from moving                                                     | none                                                   | none              | No      |
| add_item               | execute the additem command as the given bot                                     | `string` _text_                                        | none              | No      |
| whisper                | whisper a player                                                                 | `Player` _target_, `string` _text_                     | none              | Yes     |
| tell_party             | send a message to party chat                                                     | `string` _text_                                        | none              | Yes     |
| tell_raid              | send a message to raid chat                                                      | `string` _text_                                        | none              | Yes     |
| say                    | send a message to local area                                                     | `string` _text_                                        | none              | Yes     |
| yell                   | yell a message to local area                                                     | `string` _text_                                        | none              | Yes     |
| set_target             | set the bot's target                                                             | `Unit` _target_                                        | none              | Yes     |
| clear_target           | clear the bot's target                                                           | none                                                   | none              | Yes     |
| clear_stealth          | clears stealth state                                                             | none                                                   | none              | Yes     |
| face                   | faces the given target or orientation                                            | `Unit` _target_ or `number` _orientation_              | none              | Yes     |
| has_power_to_cast      | checks to see if bot has enough power (mana, energy, etc.) to cast a given spell | `number` _spell_id_                                    | `bool`            | Yes     |
| can_cast               | returns of if the bot can cast a spell (checks cooldown, silenced, etc.)         | `number` _spell_id_                                    | `bool`            | Yes     |
| get_cast_time          | Get the cast time of the provided spell id                                       | `number` _spell_id_                                    | `number` (ms)     | No      |
| get_item_in_equip_slot | gets the item in the passed [equip_slot](#equip-slot)                            | `number` _slot_                                        | `Item` (nullable) | No      |
| get_item               | locates the first item matching the name (case sensitive) or id in inventory     | `string` _name_ or `number`                            | `Item` (nullable) | No      |
| cast                   | attempts to cast a spell- will cast on self if no target is provided             | `Unit` _target_ (optional), `number` _spell_id_        | `SpellCastResult` | Yes     |
| force_cast             | same as `cast`, will interrupt current cast before casting                       | `Unit` _target_ (optional), `number` _spell_id_        | `SpellCastResult` | Yes     |
| in_same_party_as       | will return whether or not the player is in the same party as the given player   | `Player` _target_                                      | `bool`            | Yes     |
