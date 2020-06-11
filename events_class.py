import json

from event_class import *

import os

class Events:
	def __init__(self, events=[]):
		self.events = events

	def getDataFromFile(self, fileName):
		file = open(fileName, "r")

		#Gets the lines from the log file
		lines = []
		lines = file.readlines()

		#Converts each line from string of json to a python dictionary
		#then puts each line into Events clas

		json_list = []

		for line in lines:
			json_line_dict = json.loads(line)
			obj = Event(json_line_dict)
			self.events.append(obj)

	def get_data_from_dir(self, dir_name):
		for filename in os.listdir(dir_name):
			self.getDataFromFile(dir_name + "/" + filename)



	def printEvents(self):
		for event in self.events:
			event.printEvent()

	def print_all_src_ips(self):
		for event in self.events:
			event.print_src_ip()

	def print_all_src_ports(self):
		for event in self.events:
			event.print_src_port()

	def topTen(self, category1, category2=""):
		totals = {}
		for event in self.events:
			res = event.getEventValue(category1, category2)
			if res != "":
				if res not in totals:
					totals.update({res : 1})
				else:
					totals[res] += 1

		sortedDictionary = sorted(totals.items(), key = lambda x : x[1], reverse=True)

		i = 0
		strReturn = ""
		while i < 10 and i < len(sortedDictionary):
			key, value = sortedDictionary[i]
			if i == 9:
				strReturn += str(i + 1) + ". " + key + "\n"
			else:
				strReturn += str(i + 1) + ".  " + key + "\n"
			i += 1
		return strReturn

	def getEventCategory(self, eventid):
		ret = []
		for ev in self.events:
			if eventid == ev.event["eventid"]:
				ret.append(ev)
		return ret



#
