import json

from event_class import *
from events_class import *
'''
cowrie-log-analyzer: Read Log File

'''
#As more files will be added, this will be useful
#if __name__ == '__main__':

#Opens the file
fileName = "cowrie.json.2020-03-19"
file = open(fileName, "r")

#Gets the lines from the log file
lines = []
lines = file.readlines()

#Converts each line from string of json to a python dictionary
#then puts each line into a list
json_list = []

for line in lines:
	json_line_dict = json.loads(line)
	json_list.append(json_line_dict)

obj_list = []
for json_dict in json_list:
		obj = Event(json_dict)
		obj_list.append(obj)

E = Events(obj_list)
#E.printEvents()
E.print_all_src_ips()









#
