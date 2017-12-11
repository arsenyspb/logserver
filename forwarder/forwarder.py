import sys, os
import requests
import socket
import conf as cfg

#print(socket.gethostname())


#a = list(set(os.listdir(cfg.path))

#lookup = open(changelist,"a")

for logfile in os.listdir(cfg.path):
    if logfile.endswith(cfg.extension):
        filename = os.path.join(cfg.path, logfile)


        print (format(os.stat(filename).st_mtime))

#url = 'https://api.example.com/api/dir/v1/accounts/9999999/orders'
#headers = {'Authorization' : '(some auth code)', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
#r = requests.post(url, data=open('example.json', 'rb'), headers=headers)
