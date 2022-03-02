# mangos-lua

`mangos-lua` is a World of Warcraft lua scripting API that allows for dynamic automation of Playerbots at runtime. This project aims to enable players to automate every aspect Playerbot combat behavior in order to unlock the potential of Playerbot group members.

`mangos-lua` is designed to create a first-class experience for those who wish to write their own lua scripts (and for server administrators supporting their efforts). Using the provided CLI tool `playerbot`, running `playerbot -deploy` in a local terminal where scripts are located deploys them to the server. In-game, running `.bot ai load` loads the scripts into the client's isolated lua environment and begins execution. The entire process takes a few seconds. No rebuilds, redeployments, or restarts of the server needed to facilitate script changes.

Script management uses a new short-lived token authentication system that allows players authorize themselves or others to manage scripts for their account thus alleviating the need to pass private credentials between clients. Tokens expire after 24 hours.

`mangos-lua` also allows the usage of characters as Playerbots from accounts other than the developer's account in order to allow raid-size groups to be managed by one master. Usage of a token generated from the source account is required to authorize usage of the account's characters.

Browse the [documentation](https://nate123456.github.io/mangos-lua/) to learn more and get started.
