import sys
import socket
from socket import AF_INET, SOCK_STREAM


def scan_miftp_ip(lan_ip):
    ftp_ips = []
    ip_parts = lan_ip.split(".")
    for i in range(0, 256):
        try_ip_parts = ip_parts[: 3] + [str(i)]
        try_ip = ".".join(try_ip_parts)

        try:
            sys.stdout.write("%s/256\r" % (i + 1))
            sys.stdout.flush()
            tcpCliSock = socket.socket(AF_INET, SOCK_STREAM)
            tcpCliSock.settimeout(0.3)
            tcpCliSock.connect((try_ip, 2121))
            tcpCliSock.close()
            del tcpCliSock
            ftp_ips.append(try_ip)
        except:
            continue
    return ftp_ips
