# Getting Started

To setup your `playerbot-lua` development environment, follow the installation instructions below.

## Installation instructions (Windows):

The following instructions will guide you through installing the playerbot CLI to a global location (optional) and initializing a script source directory.

1. In a global location, such as `C:\Program Files\`, create a folder called `Playerbot CLI`.
2. Download the file `playerbot.zip` from the latest [release](https://github.com/nate123456/playerbot-lua/releases).
3. Right click on the downloaded file and choose `Extract All` from the context menu.
4. In the destination text box, enter the folder path created in step 1 e.g. `C:\Program Files\Playerbot CLI\` and press `Extract`.
5. Open the windows start menu, and begin typing `environment variables`. Choose the first result `Edit the system environment variables`. A `System Properties` window will appear.
6. Click the `Environment Variables...` button at the bottom right. A `Environment Variables` windows will appear.
7. In the first table in the new window titled `User variables for <user>`, locate and double click on the row with the variable name `Path`. A new window titled `Editor Environment Variable` will appear.
8. Press the `New` button at the top right of the window. A new row in the table will appear.
9. In the new row text box, enter the folder location of `playerbot.exe` e.g. `C:\Program Files\Playerbot CLI\`.
10. Click `Ok` at the bottom of the `Editor Environment Variable` window, the `Environment Variables` window, and the `System Properties` window.
11. Open a new terminal such as `Powershell` or `Command Prompt` or open [VS Code](https://code.visualstudio.com/) and run a terminal (CTRL+SHIFT+`) at the location where the lua script files will be located (if a terminal is already open, close and re-open it or restart VS Code).
12. Run the command `playerbot`. The directory will be initialized with a configuration file.
13. In the WoW client, run the command `.bot ai get token`. Enter the provided token into the configuration file's `TOKEN` field value.
14. Modify the configuration file to update the `API_HOST` and `LOG_HOST` addresses to point to the correct location. If desired, change the relative path where lua script files should be stored (default is `src/`).
15. Run the command `playerbot` again. It will attempt to authorize the token. If successful, the provided directory will initialize.
16. Run the command `playerbot -deploy`. The hello world provided script will deploy.
17. Add a bot as normal using the command `bot add <name>`.
18. In-game, run the command `.bot ai use lua` to switch to lua scripting mode.
19. A system message will appear as instructed in `main.lua` which will read `AI scripting is alive :)`.
20. Outside the game, edit the `main.lua` script file to change the printed string to something else, e.g. `AI scripting is alive!`.
21. In-game, run the command `.bot ai load`. The changed string will appear printed as written.
22. For more information on what the CLI can do, run the command `playerbot --help` or check the [documentation](https://nate123456.github.io/playerbot-lua/).

## Workflow

1. Login to the WoW server and choose your master character.
2. In the in-game chat, run the command `.bot ai use lua`.
3. Run the command `.bot ai get token` and update `config.yml` in your script source directory with the updated token if necessary.
4. Begin scripting using the [API](api/index.md).
5. Once you'd like to your run your scripts, run `playerbot -deploy`.
6. In-game, run the command `.bot ai load`.

Repeat steps 4 through 6 as you develop your scripts. If you get errors on deployment indicating that your token has expired, repeat step 3.

Bug reports, suggestions, or any other questions should be created as issues [here](https://github.com/nate123456/playerbot-lua/issues).
