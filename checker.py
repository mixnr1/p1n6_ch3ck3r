import subprocess
import config
ip_file = open(config.path_to_file+'missing.txt', 'r')
for line in ip_file:
    response=subprocess.Popen(["ping", "-c", "1", line.strip()],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    if (response.returncode == 0):
        status = line.rstrip() + " is Reachable"
        # subprocess.run(["/usr/bin/notify-send", "--icon=error", status])
        subprocess.run(["/usr/bin/notify-send", "--icon=/usr/share/icons/gnome/48x48/status/dialog-warning.png", status])
    else:
        status = line.rstrip() + " is Not Reachable"
        pass
    print(status)