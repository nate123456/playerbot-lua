# Dispel Types

The `dispel_types` enum allows for mapping from a dispel type name to its corresponding id. The key is a `string` _name_ and the value is a `number` _id_. It is accessed through `wow.enums.dispel_types`.

It is recommended to use `dispel_types` alongside the `type` member of the [Aura](../types/aura.md) type. For example:

```lua
print(wow.enums.dispel_types.1 ) -- magic
print(wow.enums.dispel_types.magic ) -- 1
print(wow.enums.dispel_types[aura.type] ) -- magic
```

| Key          | Value |
| ------------ | ----- |
| none         | 0     |
| magic        | 1     |
| curse        | 2     |
| disease      | 3     |
| poison       | 4     |
| stealth      | 5     |
| invisibility | 6     |
| all          | 7     |
| enrage       | 9     |
