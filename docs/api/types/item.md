# Item

This type represents an item. It inherits all functionality from `Object`. All members are read-only.

## Members

The following are members of `Item`. For example:

```lua
    print("item stack count: " .. some_item.total_count)
```

| Name            | Description                                                                                    | Return Type | Tested? |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------- | ------- |
| total_count     | how many of this type of item are in the owner's inventory                                     | `number`    | No      |
| charges         | how many charges remain on the item                                                            | `number`    | No      |
| is_potion       | whether or not the item is a potion                                                            | `bool`      | No      |
| max_stack_count | the item's highest stack count before it makes another stack                                   | `number`    | No      |
| id              | the item's generic Id (not the id of the instance of the item)                                 | `number`    | No      |
| name            | the name of the item                                                                           | `string`    | No      |
| spell_id        | the item's associated spell id (if it can be 'cast')                                           | `number`    | No      |
| is_ready        | whether or not the associated spell is ready (returns false if the item does not have a spell) | `bool`      | No      |

## Functions

The following are callable functions on any `Item`.

```lua
some_item:use()
```

| Function | Description                                                                                       | Parameters                                                        | Return Type | Tested? |
| -------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------- | ------- |
| use      | use an item on either the given slot, target, or game object. will use self if no target provided | `number` _slot_ (0 - 18) or `Item` _target_ `GameObject` _target_ | none        | Yes     |
| destroy  | destroy an item.                                                                                  | none                                                              | none        | Yes     |
