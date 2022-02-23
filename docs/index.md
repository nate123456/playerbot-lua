# Welcome

This website serves as the documentation for the World of Warcraft playerbot scripting API available as part of the MaNGOS Core WoW Server applications.

The scripting API exposes Lua bindings to a per-client Lua environment that may be used to control all aspects of group member combat behavior. All information and actions accessible to the scripts are designed to mimic real player information and choices and are restricted so as to not enable lua scripts to exploit their proximity to the server to perform actions that a normal client could not perform.

The latest version of the API is currently maintained in a fork of `mangos-tbc` located [here](https://github.com/nate123456/mangos-tbc). This fork aims to stay current with the latest stable upstream when builds succeed.

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

### Client

Clients should download the playerbot CLI program from the latest [release](https://github.com/nate123456/mangos-lua/releases) and install it in a global location such as a folder in `C:\Program Files` if on Windows, then add the folder to the path environment variable so the CLI program is available anywhere.

Open a blank folder in a lua editor of choice (VS Code is a good choice) and run `playerbot`. It will initialize the lua directory. The environment may be configured using the provided `config.json` file. The command `playerbot --help` lists available arguments and commands.

Begin scripting using the [API reference](api/index.md).

When in-game, summon bots as normal using `.bot add <name>`. Use the commands `.bot ai use lua` or `.bot ai use legacy` to allow the client to switch between usage of their bots scripts or the legacy AI. When the lua AI is enabled, the legacy AI will not perform any combat actions, but will still respond to certain events as the per the legacy AI, such as an invite or trade request. 

### Server

Make sure the server is running the current latest commit on the master branch of the [server](https://github.com/nate123456/mangos-tbc). Build, install, and run the server as normal. Ensure that the appropriate migration scripts have been applied to the server database.

`Docker` is recommended to build and run a small API web application which the client CLI interacts with to manage scripts. A `docker-compose` file is available in the source [here](https://github.com/nate123456/mangos-tbc/blob/master/src/Playerbot/docker-compose.yml) which may be used as a convenient way to spin up the provided lua script development API web application as well as the mysql database used by the server (it is generally considered good practice to containerize mysql). If `Docker` is not available or desired, the web application may be built and run natively. There are guides available online to build an ASP.NET Core web app for Windows or Linux.

Bug reports, suggestions, or any other questions should be created as issues at the repo containing the client and documentation [here](https://github.com/nate123456/mangos-lua/issues).
