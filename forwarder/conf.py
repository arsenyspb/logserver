#!/usr/bin/env python

# FILEPATH is used by forwarder.py to monitor.
# other configuration options are not exposed, but it's possible to include
# recursive notifications and so on, refer to code itself and to http://pythonhosted.org/watchdog/api.html
# example: filepath = "/tmp/app101"

filepath = "/tmp/app101"

# FILEEXTENSION is used by forwarder.py -- below. multiple extensions are supported, should be separated
# with a comma within one array, i.e. ["*.log", "*.xml", "*.debug"]
# example: fileextension = ["*.log"]

fileextension = ["*.txt"]

# URL is used to pass the protocol, FQDN, port, and exaxt RESTful verb's route for the the server
# that would accept the logfile. File content is sent as a JSONified BASE64 POST method
# example: url = "http://localhost:5000/save"

url = "http://localhost:5000/save"
