#! /usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8001))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    try:
        conn.settimeout(5)
        buff = conn.recv(1024)
        if buff == '1':
            conn.send("Hello,Client...")
        else:
            conn.send("Please,Go Out...")
    except socket.timeout:
        print "Socket Time Out.."
    finally:
        conn.close()
