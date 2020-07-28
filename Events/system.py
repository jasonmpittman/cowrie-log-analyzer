#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "events_class, events_database, sys, log"

from Events import events_class

from Events import events_database

import sys

from Log import log

system_logger = log.Logger("system")

class logic:
	"""
	This class holds functionality code that the facade calls.

	Attributes
	----------
	events_object : events_class object
	"""
	def __init__(self):
		self.events_object = events_class.Events()

	def get_data(self, name):
		"""
		Calls the get_data function in the events class.

		Parameters
		----------
		name : str
		"""
		system_logger.info(self.__class__.__name__, self.get_data.__name__, "get_data called")
		return self.events_object.get_data(name)

	def update_database(self):
		"""
		Updates the events database with what is in the events object.
		returns the a touple of test and count
		test : determins if any event failed to be inserted
		count : number of failed inserts (usually due to repeate data)
		"""
		system_logger.info(self.__class__.__name__, self.update_database.__name__, "update_database called")
		conn = events_database.create_connection()
		config_dict = events_database.get_config()
		test = True
		count = 0
		for event in self.events_object.events:
			res = events_database.add_event(conn, event)
			if not res:
				test = False
				count += 1

		conn.commit()
		conn = events_database.create_connection()

		return test, count

	def no_update(self):
		pass

	def exit(self):
		"""
		Calls the sys.exit function
		"""
		system_logger.info(self.__class__.__name__, self.exit.__name__, "exit called")
		sys.exit()
