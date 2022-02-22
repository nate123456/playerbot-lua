# Global

These are API features that are available in any context, accessible directly through their identifier.

## Members

These members are available anywhere. For example:

```lua
print(str(pi)) -- 3.14159265358979323846
```

| Name  | Description                   | Return Type | Tested? |
| ----- | ----------------------------- | ----------- | ------- |
| pi    | pi to the 20th decimal place  | `number`    | Yes     |
| wow   | state data for the wow server | `table`     | Yes     |
| store | store data for the wow server | `table`     | Yes     |

## Functions

These are functions available anywhere. All members are read-only. Usage example:

```lua
print(str(wow.time())) -- time in ticks
```

| Function | Description                                                                   | Parameters         | Return Type | Tested? |
| -------- | ----------------------------------------------------------------------------- | ------------------ | ----------- | ------- |
| print    | will generate a system message on the client that owns the environment        | `string` _message_ | none        | Yes     |
| log      | will send a log message to the log stream output (not necessarily the system) | `string` _message_ | none        | Yes     |
| str      | casts a lua object to a string (alias of `tostring`)                          | `object` _obj_     | `string`    | Yes     |
| num      | casts a lua object to a number (alias of `tonumber`)                          |
