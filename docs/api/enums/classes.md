# Classes

The `classes` enum allows for mapping from a class id to a readable string. The key is a `number` _id_ and the value is a `string` _name_. It is accessed through `wow.enums.classes`.

For example:

```lua
print(wow.enums.classes.3 ) -- Mage
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