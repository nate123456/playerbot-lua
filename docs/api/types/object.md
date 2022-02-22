# Object

This type represents a generic object. All members and functions are read-only.

## Members

The following are members of `Object`. All members are read-only. For example:

```lua
print("Object is player: " .. some_object.is_player)
```

| Name           | Description                                 | Return Type | Tested?      |
| -------------- | ------------------------------------------- | ----------- | ------------ |
| is_player      | whether or not the object is a `Player`     | `bool`      | Yes          |
| is_creature    | whether or not the object is a `Creature`   | `bool`      | Yes          |
| is_game_object | whether or not the object is a `GameObject` | `bool`      | Hard to test |
| is_unit        | whether or not the object is a `Unit`       | `bool`      | Yes          |

## Functions

The following are callable functions on any `Object`. All functions are read-only.

```lua
print("Last Message: " .. some_object:as_player().last_message)
```

| Function       | Description                        | Parameters | Return Type  | Tested? |
| -------------- | ---------------------------------- | ---------- | ------------ | ------- |
| as_player      | casts the object to a `Player`     | none       | `Player`     | No      |
| as_creature    | casts the object to a `Creature`   | none       | `Creature`   | No      |
| as_game_object | casts the object to a `GameObject` | none       | `GameObject` | No      |
| as_unit        | casts the object to a `Unit`       | none       | `Unit`       | No      |

Note- these functions are required to be able to access the corresponding members and functions for that object type.
