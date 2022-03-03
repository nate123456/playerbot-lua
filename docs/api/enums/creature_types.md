# Creature Types

The `creature_types` enum allows for mapping from a creature type name to its corresponding id. The key is a `string` _name_ and the value is a `number` _id_. It is accessed through `wow.enums.creature_types`.

It is recommended to use `creature_types` alongside the `type` member of the [Unit](../types/unit.md) type. For example:

```lua
print(wow.enums.classes.1 ) -- beast
print(wow.enums.classes.dragonkin ) -- 1
print(wow.enums.classes[target.type] ) -- beast
```

| Key            | Value |
| -------------- | ----- |
| beast          | 1     |
| dragonkin      | 2     |
| demon          | 3     |
| elemental      | 4     |
| giant          | 5     |
| undead         | 6     |
| humanoid       | 7     |
| critter        | 8     |
| mechanical     | 9     |
| unknown        | 10    |
| totem          | 11    |
| non_combat_pet | 12    |
| gas_cloud      | 13    |
