# Global

Globals are members and functions that are available in any context, accessible directly through their identifier. They often serve as the entrypoint when drilling into the game state.

## Members

These members are available anywhere. For example:

```lua
print(str(pi)) -- 3.14159265358979323846
```

| Name           | Description                   | Return Type | Tested? |
| -------------- | ----------------------------- | ----------- | ------- |
| pi             | pi to the 20th decimal place  | `number`    | Yes     |
| [wow](wow)     | state data for the wow server | `table`     | Yes     |
| [store](store) | store data for the wow server | `table`     | Yes     |

## Functions

These are functions available anywhere. All members are read-only. Usage example:

```lua
print(str(wow.time())) -- time in ticks
```

| Function | Description                                                                                         | Parameters         | Return Type | Tested? |
| -------- | --------------------------------------------------------------------------------------------------- | ------------------ | ----------- | ------- |
| print    | will generate a system message on the client that owns the environment (overrides default behavior) | `string` _message_ | none        | Yes     |
| log      | will send a log message to the log stream output (not necessarily the system)                       | `string` _message_ | none        | Yes     |
| str      | casts a lua object to a string (alias of `tostring`)                                                | `object` _obj_     | `string`    | Yes     |
| num      | casts a lua object to a number (alias of `tonumber`)                                                | `object` _obj_     | `number`    | Yes     |
| each     | returns a stateful iterator that can be used when the index is not desired                          | `array` _arr_      | `iterator`  | Yes     |

### Each

`each` is offered to cleanup a mild but common code smell in lua when iteration through an array of elements is desired but the index of the current element is not desired. In vanilla lua, the following code would be used:

```lua
for _, item in ipairs(items) do
    print(item)
end
```

With `each`, the same code would read:

```lua
for item in each(items) do
    print(item)
end
```

This simplifies the code and improves readability. `ipairs` remains still available when the index is desired.
