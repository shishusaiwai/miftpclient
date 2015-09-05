import subprocess


def connect_server(ftp_ip):
    cmd = "firefox ftp://%s:2121" % ftp_ip
    subprocess.call(cmd, shell=True)
