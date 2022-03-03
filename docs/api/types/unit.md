# Unit

This type represents a unit, which can be a player, creature, npc, or pet. It inherits all API functionality from `Object` and `WorldObject`. All members and functions are read-only.

## Members

The following are members of `Unit`. All members are read-only. For example:

```lua
print("Raid Icon: " .. some_unit.in_combat)
```

| Name                | Description                                                         | Return Type                    | Tested? |
| ------------------- | ------------------------------------------------------------------- | ------------------------------ | ------- |
| bounding_radius     | the bounding radius of the unit i.e. '_thiccness_'                  | `number`                       | Yes     |
| pet                 | the unit's pet                                                      | `Pet`                          | Yes     |
| in_combat           | whether or not the unit is in combat                                | `bool`                         | Yes     |
| raid_icon           | the units raid icon                                                 | `number` 0-7 (255 for no icon) | Yes     |
| attackers           | all units with threat on unit                                       | `list<Unit>`                   | No      |
| target              | the unit's target                                                   | `Unit`                         | Yes     |
| is_alive            | whether or not the unit is alive                                    | `bool`                         | Yes     |
| crowd_controlled    | whether or not the unit is CC'd (not used by original playerbot)    | `bool`                         | No      |
| health              | current hit points                                                  | `number`                       | Yes     |
| max_health          | max hit points                                                      | `number`                       | Yes     |
| power               | current power (mana, energy, etc.)                                  | `number`                       | Yes     |
| max_power           | max power (mana, energy, etc.)                                      | `number`                       | Yes     |
| current_cast        | the spell the unit is casting (0 if not found)                      | `number`                       | No      |
| current_cast_time   | the remaining time on the currently casting spell (ms)              | `number`                       | No      |
| current_auto_attack | the auto attack spell the unit is casting (0 if not found)          | `number`                       | No      |
| current_channel     | the channel spell the unit is casting (0 if not found)              | `number`                       | No      |
| type                | the unit's type (see [creature_types](api/enums/creature_types.md)) | `number`                       | No      |

## Functions

The following are functions that can be called on a `Unit`. All functions are read-only. Example usage:

```lua
print("Bot threat: " .. some_unit:get_threat(some_bot))
```

| Function       | Description                                                                       | Parameters                                     | Return Type   | Tested? |
| -------------- | --------------------------------------------------------------------------------- | ---------------------------------------------- | ------------- | ------- |
| is_attacked_by | whether or not the given unit is attacking the unit                               | `Unit` _target_                                | `bool`        | No      |
| get_threat     | get the threat the given target has on the unit                                   | `Unit` _target_                                | `number`      | No      |
| in_melee_range | get whether or not the given target is reachable with melee                       | `Unit` _target_                                | `bool`        | Yes     |
| is_enemy       | whether or not the unit can attack the given unit or group if target not provided | `Unit` _target_ (optional)                     | `bool`        | Yes     |
| is_friendly    | whether or not the unit can assist (not /assist) the given unit                   | `Unit` _target_                                | `bool`        | Yes     |
| get_aura       | get the first instance of an aura affecting the unit for the given id             | `number` _aura_id_, `Unit` _caster_ (optional) | `Aura`        | No      |
| get_buffs      | get all beneficial auras on the unit                                              | none                                           | `array<Aura>` | No      |
| get_debuffs    | get all harmful auras on the unit- optional filter by dispel type                 | `number` _dispel_type_ (optional)              | `array<Aura>` | No      |
