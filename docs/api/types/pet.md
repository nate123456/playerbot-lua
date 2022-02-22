# Pet

This type represents a pet. It inherits all API functionality from `Creature`, `Unit`, `WorldObject`, and `Object`.

## Members

The following are members of `Pet`. For example:

```lua
print("Pet owner: " .. pet_owner.name)
```

| Name        | Description                               | Return Type                                      | Tested? |
| ----------- | ----------------------------------------- | ------------------------------------------------ | ------- |
| pet_owner   | the pet's owner (better the owner member) | `Player`                                         | No      |
| happiness   | the pet's happiness                       | `number` 1: unhappy, 2: content, 3: happy        | No      |
| is_feeding  | whether or not the pet is feeding         | `bool`                                           | No      |
| react_state | get or set the pet's reaction state       | `number` 0: passive, 1: defensive, 2: aggressive | No      |

## Functions

The following are callable functions on any `Pet`.

```lua
-- :(
some_pet:summon()
```

| Function     | Description                                                          | Parameters                            | Return Type      | Tested? |
| ------------ | -------------------------------------------------------------------- | ------------------------------------- | ---------------- | ------- |
| set_autocast | set autocast for the given ability                                   | `number` _spell_id_, `bool` _enabled_ | none             | No      |
| summon       | summon the pet                                                       | none                                  | none             | No      |
| dismiss      | dismiss the pet                                                      | none                                  | none             | No      |
| attempt_feed | find food in the owner's inventory and attempt to feed it to the pet | none                                  | `bool` (success) | No      |
