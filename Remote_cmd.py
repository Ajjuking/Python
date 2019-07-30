#!/usr/bin/env python

import sys, paramiko, csv
command = sys.argv[1]
username = "abc"
port = 22
password = "xyz"
X = {}
w = csv.writer(open("output.csv", "w"))
f = open("server.txt","r")
Inp=[line.rstrip('\n') for line in f]
for server in Inp:
    try:
        print(server)
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port=port, username=username, password=password, pkey=None, key_filename=None)
        stdin, stdout, stderr = client.exec_command(command)
        a = stdout.read()
        X.update({server: a})
    except:
        a = sys.exc_info()[0]
        X.update({server: a})
    finally:
        client.close()
for key, val in X.items():
    w.writerow([key, val])
    print("Output.csv has been exported at script root path")

