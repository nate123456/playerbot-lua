# Store

## Functions

These are functions available anywhere on the `store` table, accessible anywhere. Usage example:

```lua
json = require("json")
local json_str = wow.store.get()  -- { "some_key": "some_value" }
data = json.decode(json_str)
print(data.some_key)
```

The store allow for unstructured data to be saved between lua script sessions, e.g. getting and setting json strings.

| Function | Description                      | Parameters       | Return Type | Tested? |
| -------- | -------------------------------- | ---------------- | ----------- | ------- |
| get      | get data from persistent store   | none             | `string`    | Yes     |
| set      | set data from persistent store   | `string` _value_ | none        | Yes     |
| clear    | clear data from persistent store | none             | none        | Yes     |
