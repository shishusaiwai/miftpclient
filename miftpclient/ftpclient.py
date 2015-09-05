# coding: utf-8
import subprocess


def connect_server(ftp_ip):
    cmd = "firefox ftp://%s:2121" % ftp_ip
    subprocess.call(cmd, shell=True)
    print u"\nFTP(%s:2121)已经在firefox中打开, 请查看\n" % ftp_ip
