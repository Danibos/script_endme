import xbmcgui
import xbmc
import subprocess
import os
import sys
import shutil

def find_cmd(cmd):
    # Find the absolute path of the command in the system
    path = shutil.which(cmd)
    if not path:
        xbmcgui.Dialog().ok('EndMe', f'Command not found: {cmd}')
    return path

def run_command(cmd):
    try:
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return (True, result.stdout)
    except subprocess.CalledProcessError as e:
        return (False, f"Command failed: {e.stderr}")
    except Exception as e:
        return (False, f"Error: {str(e)}")

def shutdown():
    # Shutdown the system depending on the platform
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        sudo = find_cmd('sudo')
        shutdown_cmd = find_cmd('shutdown')
        if sudo and shutdown_cmd:
            ok, msg = run_command([sudo, shutdown_cmd, 'now'])
            if not ok:
                xbmcgui.Dialog().ok('EndMe', f"Shutdown failed:\n{msg}")
    elif sys.platform == 'win32':
        os.system('shutdown /s /f /t 0')
    else:
        xbmcgui.Dialog().ok('EndMe', 'Unsupported platform for shutdown')

def reboot():
    # Reboot the system depending on the platform
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        sudo = find_cmd('sudo')
        reboot_cmd = find_cmd('reboot')
        if sudo and reboot_cmd:
            ok, msg = run_command([sudo, reboot_cmd])
            if not ok:
                xbmcgui.Dialog().ok('EndMe', f"Reboot failed:\n{msg}")
    elif sys.platform == 'win32':
        os.system('shutdown /r /f /t 0')
    else:
        xbmcgui.Dialog().ok('EndMe', 'Unsupported platform for reboot')

# Show options to the user in a dialog box
dialog = xbmcgui.Dialog()
option = dialog.select("Choose an action", ["Shutdown", "Reboot"])

if option == 0:
    shutdown()
elif option == 1:
    reboot()
