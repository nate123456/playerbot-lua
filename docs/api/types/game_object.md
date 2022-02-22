# GameObject

This type represents a game object. It inherits all API functionality from `Object` and `WorldObject`. All members and functions are read-only.

## Members

The following are members of `GameObject`. All members are read-only. For example:

```lua
print("Owner: " .. some_game_object.owner.name)
```

| Name   | Description                         | Return Type | Tested? |
| ------ | ----------------------------------- | ----------- | ------- |
| in_use | whether or not the object is in use | `bool`      | No      |
| owner  | the owner of the game object        | `Unit`      | No      |
| level  | the level of the game object        | `number`    | No      |

## Functions

The following are callable functions on any `GameObject`. All functions are read-only.

```lua
-- :(
```

| Function | Description | Parameters | Return Type | Tested? |
| -------- | ----------- | ---------- | ----------- | ------- |
