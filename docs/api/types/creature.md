# Creature

This type represents a creature. It inherits all API functionality from `Object`, `WorldObject`, and `Unit`. All members and functions are read-only.

## Members

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
