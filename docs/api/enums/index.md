# Enums

## Introduction

In lua, enums are tables that represent a map between a number and a string. All enum tables are accessible through `wow.enums`. They are most often used to provide a clean way to represent different possible states which often take the form of a single element of a possible set.

For example, when working with player classes via the `player.class` member (see the [Player](../types/player.md) type) the return value is a number which uniquely identifies the class from the set of possible classes. While the numeric value serves well as a clean and straightforward way to represent each class, often times the name of that class is needed. The code snippet below demonstrates the value of having a map available.

```lua
print(some_player.class) -- 1: not particularly readable
print(wow.enums.classes[some_player.class]) -- mage
```

All enum tables are also 'flipped' or reversed, so each value is also the key to the corresponding value; `wow.enums.classes[1]` returns `mage`, and `wow.enums.classes["mage"]` returns `1`.

The 'reversed' mapping useful in the case where one might want to confirm whether or not a given player is a mage:

```lua
if some_player.class == wow.enums.classes["mage"] then
    print("It's a mage!")
end
```

This removes the need for memorization of class numbers and makes the code more readable. Furthermore, the use of a string as a key can be replaced with dot notation as below since the presence of the key is guaranteed:

```lua
if some_player.class == wow.enums.classes.mage then
    print("It's a mage!")
end
```

See the sidebar on the left for the list of all enums.
