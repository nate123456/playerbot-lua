# Welcome

This website serves as the documentation for the World of Warcraft playerbot lua scripting API available as part of the MaNGOS Core WoW Server applications.

The scripting API exposes Lua bindings to a per-client Lua environment that may be used to control all aspects of group member combat behavior. All information and actions accessible to the scripts are designed to mimic real player information and choices.

Check out the [cores](cores) page to check the integration status of your desired core.

An example of a simple lua script that prints each managed bot's name for the client is below:

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

If you are a client and would like to learn how to get started scripting, check out [getting started for clients](getting_started_client).

If you are the server administrator and would like to learn how to get started integrating `mangos-lua` into your core, check out [getting started for server admins](getting_started_server).
