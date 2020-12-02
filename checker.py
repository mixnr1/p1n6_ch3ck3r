import subprocess
ip_list = ['google.com', 'tvnet.lv', 'ddfadlkjdklfja.fa']
for line in ip_list:
    response=subprocess.Popen(["ping", "-c", "1", line],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    stdout, stderr = response.communicate()
    if (response.returncode == 0):
        status = line + " is Reachable"
        subprocess.run(["/usr/bin/notify-send", "--icon=error", status])
    else:
        pass