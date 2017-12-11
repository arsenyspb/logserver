#!/usr/bin/env python

# path to monitor must have 'r' before path with doublequotes

filepath = "/Users/arseny/Documents/OneDrive - FOOD BUDDY SERVICE/training/2017-gojek/solution"

path = r"/Users/arseny/Documents/OneDrive - FOOD BUDDY SERVICE/training/2017-gojek/solution"


# TO BE REMOVED?.. extension to monitor must have double-quotes

extension = ".txt"

#for watchdog -- below

fileextension = ["*.txt"]

#changelist is used needed to track what has been sent

changelist = r"/Users/arseny/Documents/OneDrive - FOOD BUDDY SERVICE/training/2017-gojek/solution/changelist.log"

# server API

url = "http://localhost:5000/save"
