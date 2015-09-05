#! /usr/bin/env python
# coding: utf-8
import sys

from lib.ftpclient import connect_server
from lib.ipparser import parse_ip
from lib.scan import scan_miftp_ip


def main():
    lan_ip = parse_ip()
    if not lan_ip:
        print "lan_ip not found."
        sys.exit(0)

    ftp_ip = scan_miftp_ip(lan_ip)
    if not ftp_ip:
        print "no ftp found."
        sys.exit(0)

    connect_server(ftp_ip)


if __name__ == "__main__":
    main()
