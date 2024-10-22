# backpack-cli

backpack-cli is a command-line tool designed for managing and organizing your collections of gear, providing a local alternative to services like Lighterpack.

![image](https://github.com/user-attachments/assets/804e2197-db11-43e9-87a6-88a6f59ee2b5)

## Downloading
I cannot provide binaries as of yet. Please download the repository and use in-folder with python.

## Usage

Whenever you run the program, it will look for the database at `XDG_CONFIG_HOME/backpack-cli/`. It will be created if it is not found.


For detailed command line usage, refer to [Command Line Usage](https://github.com/Kaya-Sem/backpack-cli/wiki/Command-Line-Usage)



## Import

To import a csv list from Lighterpack, you can use the command `backpack import-lighterpack [path/to/file]`. This command will do the following:

1. Parse all items and create them in the database
2. create a collection named after the filename
3. add all the items to the collection

🛈 Importing collections with the same items will create duplicates
