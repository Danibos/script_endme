import xbmcgui
import xbmc
import subprocess
import os
import sys

def shutdown():
    try:
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            subprocess.run(['sudo', 'shutdown', 'now'])
        elif sys.platform == 'win32':
            os.system('shutdown /s /f /t 0')
        else:
            xbmcgui.Dialog().ok('EndMe', 'Unsupported platform for shutdown')
    except Exception as e:
        xbmcgui.Dialog().ok('EndMe', f"Error: {str(e)}")

def reboot():
    try:
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            subprocess.run(['sudo', 'reboot'])
        elif sys.platform == 'win32':
            os.system('shutdown /r /f /t 0')
        else:
            xbmcgui.Dialog().ok('EndMe', 'Unsupported platform for reboot')
    except Exception as e:
        xbmcgui.Dialog().ok('EndMe', f"Error: {str(e)}")

# Display the options to the user in a dialog box
dialog = xbmcgui.Dialog()
option = dialog.select("Choose an action", ["Shutdown", "Reboot"])

if option == 0:
    shutdown()
elif option == 1:
    reboot()
