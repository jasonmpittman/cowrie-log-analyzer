import json

from event_class import *

import os

import pathlib

class Events:
	def __init__(self, events=[]):
		self.events = events

	'''
	Gets data from a file and puts it into the events list
	Input: filename
	'''
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


	'''
	Runs the getDataFromFile function repeatedly on all files in a given directory
	Input: dir_name -> directory name
	'''
	def get_data_from_dir(self, dir_name):
		for filename in os.listdir(dir_name):
			self.getDataFromFile(dir_name + "/" + filename)

	'''
	Determines if it is a file or directory name and acts accordingly
	Input: name
	'''
	def get_data(self, name):
		file = pathlib.Path(name)
		if file.exists():
			if os.path.isfile(name):
				self.getDataFromFile(name)
			else:
				self.get_data_from_dir(name)
			return True
		else:
			print("Not a file or directory with that path")
			return False

	'''
	Prints all events in the events list
	'''
	def printEvents(self):
		for event in self.events:
			event.printEvent()

	'''
	Returns all rows with columns with a given value
	Input: eventid --> category
	'''
	def getEventCategory(self, eventid):
		ret = []
		for ev in self.events:
			if eventid == ev.event["eventid"]:
				ret.append(ev)
		return ret


#
