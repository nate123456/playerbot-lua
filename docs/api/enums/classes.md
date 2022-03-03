# Classes

The `classes` enum allows for mapping from a class id to its corresponding name. The key is a `number` _id_ and the value is a `string` _name_. It is accessed through `wow.enums.classes`.

It is recommended to use `classes` alongside the `class` member of the [Player](../types/player.md) type. For example:

```lua
print(wow.enums.classes.3 ) -- mage
print(wow.enums.classes.mage ) -- 3
print(wow.enums.classes[bot.class] ) -- Mage
```

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
