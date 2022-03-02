# Specs

The `specs` enum allows for mapping from a equip slot id to its corresponding name. The key is a `number` _id_ and the value is a `string` _name_. It is accessed through `wow.enums.specs`. For example:

It is recommended to use `specs` alongside the `spec` member of the [Player](api/types/player.md) type. For example:

```lua
print(wow.enums.specs.mage.81 ) -- arcane
print(wow.enums.specs.arcane ) -- 81
print(wow.enums.specs[bot.spec] ) -- arcane
```

## Mage

| Key | Value  |
| --- | ------ |
| 81  | arcane |
| 41  | fire   |
| 61  | frost  |

## Warrior

| Key | Value      |
| --- | ---------- |
| 161 | arms       |
| 164 | fury       |
| 163 | protection |

## Rogue

| Key | Value         |
| --- | ------------- |
| 182 | assassination |
| 181 | combat        |
| 183 | subtlety      |

## Priest

| Key | Value      |
| --- | ---------- |
| 201 | discipline |
| 202 | holy       |
| 203 | shadow     |

## Shaman

| Key | Value       |
| --- | ----------- |
| 261 | elemental   |
| 263 | enhancement |
| 262 | restoration |

## Druid

| Key | Value       |
| --- | ----------- |
| 283 | balance     |
| 281 | feral       |
| 282 | restoration |

## Warlock

| Key | Value       |
| --- | ----------- |
| 302 | affliction  |
| 303 | demonology  |
| 301 | destruction |

## Hunter

| Key | Value         |
| --- | ------------- |
| 361 | beast_mastery |
| 363 | marksmanship  |
| 362 | survival      |

## Paladin

| Key | Value       |
| --- | ----------- |
| 382 | holy        |
| 383 | protection  |
| 381 | retribution |
