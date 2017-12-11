###
### original idea from http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html
###

import json
import conf as cfg
import time
import socket
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import base64

class MyHandler(PatternMatchingEventHandler):

    pattern = cfg.extension
    ignore_directories=True
    case_sensitive=False
    recursive=False

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        #print event.src_path, event.event_type  # print now only for degug

        with open(event.src_path, 'rb') as log_source:

        #url = 'https://api.example.com/api/dir/v1/accounts/9999999/orders'
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

        print(json.dumps(postbody))
        # r = requests.post(cfg.url, data=open('example.json', 'rb'), headers=headers)

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
