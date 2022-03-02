# WorldObject

This type represents a generic object. It inherits all API functionality from `Object`. All members and functions are read-only.

## Members

The following are members of `WorldObject`. All members are read-only. For example:

```lua
print("Enemy orientation: " .. enemy.orientation)
```

| Name        | Description              | Return Type | Tested? |
| ----------- | ------------------------ | ----------- | ------- |
| orientation | the object's orientation | `number`    | Yes     |
| name        | the object's name        | `string`    | Yes     |
| zone_id     | the object's Zone Id     | `number`    | No      |
| area_id     | the object's Area Id     | `number`    | No      |
| position    | the object's position    | `Position`  | Yes     |

## Functions

The following are callable functions on any `WorldObject`. All functions are read-only.

```lua
print("Bot A angle to bot b: " .. bot_a:get_angle(bot_b))
```

| Function                | Description                                                          | Parameters                                                                       | Return Type                              | Tested? |
| ----------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------- | ------- |
| get_angle               | get the angle of given object                                        | `WorldObject` _world_object_ or `Position` _pos_ or (`number` _x_, `number` _y_) | `number`                                 | No      |
| get_close_point         | get a point close to the object                                      | `number` _bounding_radius_, `number` _distance_, `number` _angle_                | `number` _x_, `number` _y_, `number` _z_ | No      |
| has_in_arc              | whether or not the given target is in the object's arc               | `Unit` _target_                                                                  | `bool`                                   | No      |
| is_within_los           | whether or not the given target is in the object's line of sight     | `Unit` _target_                                                                  | `bool`                                   | No      |
| is_in_range             | whether or not the given target is in range of the given spell       | `Unit` _target_, `number` _spell_id_                                             | `bool`                                   | No      |
| gcd                     | global cooldown remaining for the given spell, 0 if ready            | `number` _spell_id_                                                              | `number` (remaining time)                | No      |
| get_nearby_game_objects | get an array of all game objects within given radius of world object | `number` _radius_                                                                | `array<GameObject>`                      | No      |
| get_nearby_units        | get an array of all units within given radius of world object        | `number` _radius_                                                                | `array<Unit>`                            | No      |

Note- functions with muliple returns can be unpacked like so:

```lua
x, y, z = unpack(some_obj:get_close_point(1, 1, 1))
```
