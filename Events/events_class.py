#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "event_class, json, os, pathlib"

from Events import event_class

import json

import os

import pathlib

class Events:
	"""
	This class holds a list of event objects.

	Properties : events
	"""
	def __init__(self, events=[]):
		self.events = events


	def get_data_from_file(self, file_name):
		'''
		Gets data from a file and puts it into the events list
		Input: file_name

		Parameters
		----------
		file_name : str

		'''
		file = open(file_name, "r")

		#Gets the lines from the log file
		lines = []
		lines = file.readlines()

		#Converts each line from string of json to a python dictionary
		#then puts each line into Events clas

		json_list = []

		for line in lines:
			json_line_dict = json.loads(line)
			obj = event_class.Event(json_line_dict)
			self.events.append(obj)



	def get_data_from_dir(self, dir_name):
		'''
		Runs the get_data_from_file function repeatedly on all files in a given directory
		Input: dir_name -> directory name

		Parameters
		----------
		dir_name : str
		'''
		for filename in os.listdir(dir_name):
			self.get_data_from_file(dir_name + "/" + filename)



	def get_data(self, name):
		'''
		Determines if it is a file or directory name and acts accordingly
		Input: name

		Parameters
		----------
		name : str
		'''
		file = pathlib.Path(name)
		if file.exists():
			if os.path.isfile(name):
				self.get_data_from_file(name)
			else:
				self.get_data_from_dir(name)
			return True
		else:
			print("Not a file or directory with that path")
			return False


	def print_events(self):
		'''
		Prints all events in the events list
		'''
		for event in self.events:
			event.printEvent()


	def get_event_category(self, event_id):
		'''
		Returns all rows with columns with a given value
		Input: eventid --> category

		Parameters
		----------
		event_id : str
		'''
		ret = []
		for ev in self.events:
			if event_id == ev.event["eventid"]:
				ret.append(ev)
		return ret


#
