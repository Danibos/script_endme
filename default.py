import xbmcgui
import xbmc
import subprocess
import os
import sys

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
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        ok, msg = run_command(['/usr/bin/sudo', '/usr/bin/shutdown', 'now'])
        if not ok:
            xbmcgui.Dialog().ok('EndMe', f"Shutdown failed:\n{msg}")
    elif sys.platform == 'win32':
        os.system('shutdown /s /f /t 0')
    else:
        xbmcgui.Dialog().ok('EndMe', 'Unsupported platform for shutdown')

def reboot():
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        ok, msg = run_command(['/usr/bin/sudo', '/usr/bin/reboot'])
        if not ok:
            xbmcgui.Dialog().ok('EndMe', f"Reboot failed:\n{msg}")
    elif sys.platform == 'win32':
        os.system('shutdown /r /f /t 0')
    else:
        xbmcgui.Dialog().ok('EndMe', 'Unsupported platform for reboot')

# Display the options to the user in a dialog box
dialog = xbmcgui.Dialog()
option = dialog.select("Choose an action", ["Shutdown", "Reboot"])

if option == 0:
    shutdown()
elif option == 1:
    reboot()
