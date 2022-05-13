#!/usr/bin/python2.7

from paramiko import SSHClient
from paramiko import AutoAddPolicy
from scp import SCPClient

lines = open("list.txt", "r").readlines()
lines = [x.strip() for x in lines]
for i in lines:
    data = i.split()
    host = data[0]
    port = data[1]
    username = data[2]
    password = data[3]
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy)
    ssh.connect(host, port, username, password)
    scp = SCPClient(ssh.get_transport())
    scp.put('list.txt', recursive=True, remote_path='/dev/shm')
    scp.close()
    stdin, stdout, stderr = ssh.exec_command('/usr/bin/pwd')
    print(stdout.read())
    ssh.close()


    
