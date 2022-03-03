# Equip Slot

The `equip_slots` enum allows for mapping from a equip slot id to its corresponding name. The key is a `string` _name_ and the value is a `number` _id_. It is accessed through `wow.enums.equip_slots`.

It is recommended to use `equip_slots` alongside the `type` member of the [Aura](../types/aura.md) type. For example:

```lua
print(wow.enums.equip_slots.1 ) -- magic
print(wow.enums.equip_slots.magic ) -- 1
print(wow.enums.equip_slots[aura.type] ) -- magic
```

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