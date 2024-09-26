import os

def shutdown_cec():
    # Use cec-client to send the command to turn off all devices
    os.system('echo "standby 0" | cec-client -s -d 1')
