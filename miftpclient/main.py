#! /usr/bin/env python
# coding: utf-8
import sys

from colorama import Fore, init

from ftpclient import connect_server
from ipparser import parse_ip
from scan import scan_miftp_ip

init(autoreset=True)


def main():
    lan_ip = parse_ip()
    if not lan_ip:
        print Fore.RED + u"\n[错误]没有找到内网IP."
        sys.exit(1)

    ftp_ips = scan_miftp_ip(lan_ip)
    if not ftp_ips:
        print Fore.RED + u"\n[错误]没有找到FTP, 请检查手机端是否开启FTP."
        sys.exit(1)
    elif len(ftp_ips) == 1:
        ftp_ip = ftp_ips[0]
    else:
        print Fore.GREEN + u"\n在您的子网内发现如下小米FTP:"
        for i, ip in enumerate(ftp_ips):
            print Fore.GREEN + "%s. %s" % (i, ip)
        index = input(u"请输入序号选择您想连接的FTP: ")
        try:
            ftp_ip = ftp_ips(int(index))
        except (IndexError, ValueError):
            print Fore.RED + u"[错误]错误的输入"
            sys.exit(2)

    connect_server(ftp_ip)


if __name__ == "__main__":
    main()
