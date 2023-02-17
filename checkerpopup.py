import subprocess
import config
import time
import notify2
import os
os.environ['DISPLAY'] = ':0'
notify2.init("My Application")
ip_file = open(config.path_to_file+'ip_list.txt', 'r')
for line in ip_file:
    response=subprocess.Popen(["ping", "-c", "1", line.strip()],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    if (response.returncode == 0):
        status = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + line.strip() 
        n = notify2.Notification(
            "PING SUCCESS NOTIFICATION", 
            status,
            "notification-message-im")
        n.set_timeout(0)
        n.add_action("close", "Close", lambda *args: None)
        n.show()
    else:
        pass