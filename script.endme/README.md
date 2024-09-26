
# EndMe - Kodi Add-on for System Shutdown and Reboot

**EndMe** Due to a recent issue with Python that prevents shutting down or rebooting Kodi on Linux (not sure if it occurs on other distributions), I decided to create this simple add-on to give users the ability to shut down or reboot their machine directly from the Kodi interface using system-level commands.

## Features

- **Reboot or Shutdown** your system directly from Kodi without the need to enter terminal commands.
- Supports **sudo-less shutdown** and reboot commands using the appropriate permissions in the `sudoers` file.

## To do

- Sends a **CEC command** to turn off all connected HDMI devices when Kodi is shut down.

## Requirements

- **Kodi Omega**: Should work from Matrix as well but i didn't test it.
- **sudoers configuration**: To allow the add-on to shut down or reboot without requiring a password, add the necessary permissions to your `/etc/sudoers` file. Please read the "Important: Pay attention" part

## Installation

1. Clone this repository or download the `.zip` of the add-on.
2. Install the add-on in Kodi through the "Install from Zip file" option in the add-ons menu. 
   You can also extract the zip folder to ~/.kodi/addons/
3. Depending on your Linux distribution, **verify how the sudoers file should be edited and where is located**
   This as been tested only in Arch:
   Add the following lines to your `sudoers` file (use `visudo` to edit):
   ```
   username ALL=(ALL) NOPASSWD: /usr/bin/systemctl poweroff, /usr/bin/systemctl reboot, /sbin/shutdown
   ```
   **Replace `username`** with your user or the user running Kodi.

   alternative way with one command:
   ```
   echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/systemctl poweroff, /usr/bin/systemctl reboot, /sbin/shutdown" | sudo EDITOR='tee -a' visudo
   ```

**Important: Pay Attention When Modifying the sudoers File**
   
Modifying the sudoers file can give users additional privileges on your system, but incorrect changes may result in losing the ability to use sudo entirely. Always use the visudo command when editing the file, as it helps prevent syntax errors that could break the file.   
In the steps below a bash command is provided to automate the necessary changes. 
Be sure to double-check any manual modifications to avoid potential issues.



## License

This add-on is released under the **MIT License**, allowing you to use, modify, and distribute it as long as the original author is credited.

