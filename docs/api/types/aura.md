# Aura

This type represents an aura, buff, or debuff.

## Members

The following are members of `Aura`. For example:

```lua
    print("duration: " .. some_aura.duration)
```

| Name         | Description                              | Return Type | Tested? |
| ------------ | ---------------------------------------- | ----------- | ------- |
| id           | the id of the aura                       | `number`    | No      |
| type         | the dispel type of the aura (e.g. magic) | `number`    | No      |
| target       | the target of the aura                   | `Unit`      | No      |
| caster       | the caster of the aura                   | `Unit`      | No      |
| stacks       | aura's stack count                       | `number`    | No      |
| duration     | aura's remaining time, -1 if not found   | `number`    | No      |
| max_duration | aura's maximum duration                  | `number`    | No      |
| charges      | aura's charge count                      | `number`    | No      |
