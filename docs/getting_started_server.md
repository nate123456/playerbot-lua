### Server

Make sure the server is running the current latest commit on the master branch for your [core](cores) of choice. Build, install, initialize, and run the server as normal. Ensure that the appropriate migration scripts have been applied to the server database.

`Docker` is recommended to build and run a small API web application which the client CLI interacts with to manage scripts. A `docker-compose` file is available in the source which may be used as a convenient way to spin up the provided lua script development API web application as well as the mysql database used by the server (it is generally considered good practice to containerize mysql, especially if using an older version). If `Docker` is not available or desired, the web application may be built and run natively. There are guides available online to build an ASP.NET Core web app for Windows or Linux.

Run the sql setup script located in the source under `sql/base/mangos_lua.sql` e.g. `sudo mysql -uroot --database=tbccharacters < sql/base/mangos_lua.sql` where the database is the characters database for your core.

Bug reports, suggestions, or any other questions should be created as issues [here](https://github.com/nate123456/playerbot-lua/issues).
