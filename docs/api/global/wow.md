# wow

Most state data is accessible through the readonly `wow` table.

## Members

These members are available anywhere. For example:

```lua
print(wow.master.name)
```

| Name             | Description                                                   | Return Type     | Tested? |
| ---------------- | ------------------------------------------------------------- | --------------- | ------- |
| command_message  | the last message sent as a command (from `.bot ai write ...`) | `string`        | No      |
| command_position | the last position sent as a command (from command spell)      | `Position`      | No      |
| bots             | All the bots that are managed by the master                   | `array<Bot>`    | No      |
| raid_icons       | All raid icon targets (nullable) ex. `raid_icons.skull`       | `table<Unit>`   | No      |
| master           | get the master                                                | `Player`        | Yes     |
| enums            | provides access to the enums table                            | `table`         | Yes     |
| group            | all group members                                             | `array<Player>` | Yes     |

## Functions

These are functions available anywhere. All members are read-only. Usage example:

```lua
print(str(wow.time())) -- time in ticks
```

| Function          | Description                                        | Parameters          | Return Type | Tested? |
| ----------------- | -------------------------------------------------- | ------------------- | ----------- | ------- |
| spell_exists      | get whether or not a spell is available            | `number` _spell_id_ | `bool`      | No      |
| time              | Get the current time in ticks since the epoch (ms) | `number`            | Yes         |
| spell_is_positive | get whether or not a spell is helpful or harmful   | `number` _spell_id_ | `bool`      | No      |
