#! /usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko

# 实例化SSHClient
client = paramiko.SSHClient()
# 自动添加策略，保存服务器的主机名和密钥信息
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接SSH服务端，以用户名和密码进行认证
client.connect('192.168.5.6', username='root', password='Cs123456')
# 实例化Transport，并建立会话Session
ssh_session = client.get_transport().open_session()
if ssh_session.active:
    ssh_session.exec_command('ls')
    print ssh_session.recv(1024)
client.close()
