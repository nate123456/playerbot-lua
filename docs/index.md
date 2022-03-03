# Welcome

This website serves as the documentation for the World of Warcraft playerbot lua scripting API `playerbot-lua` available as part of the MaNGOS Core WoW Server applications.

The scripting API exposes Lua bindings to a per-client Lua environment that may be used to control all aspects of Playerbot combat behavior. All information and actions accessible to the scripts are designed to mimic real player information and choices.

An example of a simple lua script that prints each playerbot's name once for the client is below:

```lua
local has_printed = false

local function main()
    if not has_printed then
        for _, bot in ipairs(wow.bots) do
            print(bot.name)
        end
        has_printed = true
    end
end
```

## Getting Started

To get started with Playerbot scripting, check out [getting started for clients](getting_started_client).

To get started migrating a server that has a [core with playerbot-lua][cores](cores) integrated or you are interested in setting up a new server, check out [getting started for server admins](getting_started_server).
