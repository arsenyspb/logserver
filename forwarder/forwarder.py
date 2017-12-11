#!/usr/bin/env python

import json
import conf as cfg
import time
import socket
import requests
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import base64

'''
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError
'''

class MyHandler(PatternMatchingEventHandler):

    patterns = cfg.fileextension
    ignore_directories=True
    case_sensitive=False
    recursive=False

    def process(self, event):

        with open(event.src_path, 'rb') as log_source:

            postheaders = {
                'Authorization' : 'Not Implemented',
                'Accept' : 'application/json',
                'Content-Type' : 'application/json'
            }
            postbody = {
                "hostname": socket.gethostname(),
                "filename": event.src_path,
                "filecontent": base64.b64encode(log_source.read())
            }

        r = requests.post(cfg.url, data=json.dumps(postbody), headers=postheaders)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
    observer = Observer()
    observer.schedule(MyHandler(), path=cfg.filepath)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
