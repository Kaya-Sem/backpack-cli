# backpack-cli

backpack-cli is a command-line tool designed for managing and organizing your collections of gear, providing a local alternative to services like Lighterpack.

![image](https://github.com/user-attachments/assets/804e2197-db11-43e9-87a6-88a6f59ee2b5)

## Downloading

I am not providing any binaries as of yet. Please download the repository and use in-folder to experiment with the given database.

## USAGE

Whenever you run the program, it will look for the database at `XDG_CONFIG_HOME/backpack-cli/`. It will be created if it is not found.

With backpack-cli, you can easily interact with your database using the following commands:

For detailed usage, refer to [Command Line Usage](https://github.com/Kaya-Sem/backpack-cli/wiki/Command-Line-Usage)



## IMPORT

To import a csv list from Lighterpack, you can use the command `backpack import-lighterpack [path/to/file]`. This command will do the following:

1. Parse all items and create them in the database
2. create a collection named after the filename
3. add all the items to the collection

⚠️ There is no checking for duplicates. You either have to remove them yourself from the spreadsheet, or delete them later on with the program itself.

## EXPORT

Features under development include:

    Export to CSV

⚠️ Note

backpack-cli is still in development. Be aware that changes to the database structure or code may affect compatibility in future updates.
