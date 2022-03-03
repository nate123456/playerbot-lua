# Playerbot Lua Client CLI Tool Changelog

Initial alpha release for Windows.

## Features: 

- playerbot script directory initialization
- playerbot configuration file
  - created if not present
  - pre-populated with sensible default values
  - read at each CLI run
  - each field is validated to ensure required values are present and are the right data type and/or value
- automatic authentication each run
- if configured source directory is not present, directory is created and initialized with 'hello world' lua script
- `-deploy`
  - deploys all script files from configured source directory (recursive) via appropriate API calls
  - correctly maps script file names to lua module names with path mirroring
  - outputs result of deployment
- `-watch`
  - enables automatic deployment of changed files
  - checks for authenticated token before deployment
  - detects creation, modification, or deletion any lua file in the source directory (recursive)
  - uploads any changed script file via API calls
  - deletes any removed script file from via API calls
  - throttling of update frequency is configurable through config file
- `-logs`
  - enables subscription of lua log output for the given client
  - checks for authenticated token before subscribing
  - outputs logs in real time

## Instructions for installing the CLI to a global location (Windows):

1. In a global location, such as `C:\Program Files\`, create a folder called `Playerbot CLI`. 
2. Download the release file `playerbot.zip`. 
3. Right click on the downloaded file and choose `Extract All` from the context menu.
4. In the destination text box, enter the folder path created in step 1 e.g. `C:\Program Files\Playerbot CLI\` and press `Extract`. 
5. Open the windows start menu, and begin typing `environment variables`. Choose the first result `Edit the system environment variables`. A `System Properties` window will appear.
6. Click the `Environment Variables...` button at the bottom right. A `Environment Variables` windows will appear.
7. In the first table in the new window titled `User variables for <user>`, locate and double click on the row with the variable name `Path`. A new window titled `Editor Environment Variable` will appear.
8. Press the `New` button at the top right of the window. A new row in the table will appear.
9. In the new row text box, enter the folder location of `playerbot.exe` e.g. `C:\Program Files\Playerbot CLI\`.
10. Click `Ok` at the bottom of the `Editor Environment Variable` window, the `Environment Variables` window, and the `System Properties` window.
11. Open a new terminal such as `Powershell` or `Command Prompt` or open VS Code and run a terminal (CTRL+SHIFT+`) at the location where the lua script files will be located (if a terminal is already open, close and re-open it or restart VS Code).
12. Run the command `playerbot`. The directory will be initialized with a configuration file. 
13. In the WoW client, run the command `.bot ai get token`. Enter the provided token into the configuration file's `TOKEN` field value. 
14. Modify the configuration file to update the `API_HOST` and `LOG_HOST` addresses to point to the correct location. If desired, change the relative path where lua script files should be stored (default is `src/`).
14. Run the command `playerbot` again. It will attempt to authorize the token. If successful, the provided directory will initialize.
15. Run the command `playerbot -deploy`. The hello world provided script will deploy. 
16. Add a bot as normal using the command `bot add <name>`. 
17. In-game, run the command `.bot ai use lua` to switch to lua scripting mode. 
18. A system message will appear as instructed in `main.lua` which will read `AI scripting is alive :)`. 
19. Outside the game, edit the `main.lua` script file to change the printed string to something else, e.g. `AI scripting is alive!`.
20. In-game, run the command `.bot ai load`. The changed string will appear printed as written.
21. For more information on what the CLI can do, run the command `playerbot --help` or check the [documentation](https://nate123456.github.io/playerbot-lua/).
