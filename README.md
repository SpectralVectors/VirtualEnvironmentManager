# VirtualEnvironmentManager
Easily create, activate and deactivate Virtual Environments from within Blender.

## Who is this for?
Do you need to install Python packages that don't come with Blender?

Do you need a different version of a package that is already installed?

Do you miss the ease of package management that comes from a `requirements.txt`?

Are you unable or unwilling to open Blender with Admin access to install requirements?

If so, VirtualEnvironmentManager may be the solution!

## How does it work?
Open the addon preferences (Edit > Preferences > Addons > VirtualEnvironmentManager).

Enter a name for your virtual environment (venv).

Choose the directory it will be created (it defaults to the user's Documents folder)

Click 'Create & Activate'

Now, the display will update with the name and location of the active venv.

Below, you will find a file selector for the `requirements.txt` file, and next to it an 'Install requirements.txt' button.

Below that is a button to 'Deactivate & Remove' the venv.

## Future Plans
- separate Create, Activate, Deactivate, Remove into separate Operators
- store and select from previously created venvs
- allow for single package installation
- look at init options for users who want to create and use a persistent venv
