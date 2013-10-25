#!/usr/bin/env python
from sys import exit
import ast

class Writer(object):
    def __init__(self):
        self.data = {}

    def writing(self, f, data):
    	self.data = data
    	open(f, 'w').close()
        target = open(f, 'a')
        target.write(str(self.data))

    def reading(self, f):
    	s = open(f, 'r').read()
    	self.data = ast.literal_eval(s)
    	return self.data

# p = Person()      

# while True:
#     print "Type:\n\t*read to read data base\n\t*write to write to data base\n\t*exit to exit"
#     action = raw_input("\n> ")
#     if "write" in action:
#         p.name = raw_input("Name?\n> ")
#         p.phone = raw_input("Phone Number?\n> ")
#         p.age = raw_input("Age?\n> ")
#         p.address = raw_input("Address?\n>")
#         p.writing()
#     elif "read" in action:
#         p.reading()
#     elif "exit" in action:
#         exit(0)  