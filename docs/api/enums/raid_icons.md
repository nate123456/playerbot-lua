# Raid Icons

The `raid_icons` enum allows for mapping from a raid icon name to its corresponding id. The key is a `string` _name_ and the value is a `number` _id_. It is accessed through `wow.enums.raid_icons`.

It is recommended to use `raid_icons` alongside the `raid_icon` member of the [Unit](api/types/unit.md) type. For example:

```lua
print(wow.enums.raid_icon.1 ) -- circle
print(wow.enums.raid_icon.circle ) -- 1
print(wow.enums.raid_icon[unit.raid_icon] ) -- magic
```

| Key      | Value |
| -------- | ----- |
| star     | 0     |
| circle   | 1     |
| diamond  | 2     |
| triangle | 3     |
| moon     | 4     |
| square   | 5     |
| cross    | 6     |
| skull    | 7     |
