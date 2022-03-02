# Position

This type represents a position. All members and functions are read-only.

### Members

The following are members of `Position`. All members are read-only. For example:

```lua
print("Pos X: " .. pos.x)
```

| Name     | Description                                          | Return Type | Tested? |
| -------- | ---------------------------------------------------- | ----------- | ------- |
| x        | get the x value of the position                      | `number`    | Yes     |
| y        | get the y value of the position                      | `number`    | Yes     |
| z        | get the z value of the position                      | `number`    | Yes     |
| o        | get the orientation value of the position            | `number`    | Yes     |
| is_empty | whether or not the position is empty (treat as null) | `number`    | no      |

## Functions

The following are callable functions on any `Position`. All functions are read-only.

```lua
print("Distance: " .. pos_1:get_distance_between(pos_2))
```

| Function        | Description                                                      | Parameters                                       | Return Type | Tested? |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------ | ----------- | ------- |
| get_distance_to | get the distance between two positions (returns squard distance) | `Position` _other_                               | `number`    | Yes     |
| get_angle       | get the angle to a given position                                | `Position` _other_ or `number` _x_, `number` _y_ | `number`    | Yes     |
