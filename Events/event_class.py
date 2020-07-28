#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = " "

class Event:
	"""
	This is the event class which holds the data for an event
	Properties
	----------
	event : python dictionary
	"""
	def __init__(self, json):
		"""
		Parameters
		----------
		json : python dictionary
		"""
		self.event = json

	def printEvent(self):
		print(self.event)

	def get(self, key):
		"""
		Get function:
		returns the value for the given key or "-" if it does not have one, otherwise it returns the event key

		Parameters
		----------
		key : str
		"""
		try:
			return self.event[key]
		except:
			return "-"
