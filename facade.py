#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "system, log, tkinter"

import system

import log

import tkinter as tk

facade_logger = log.Logger("facade")

class event_handler:
	"""
	This acts as an intermediary between the actual functionality of the buttons and the UI component.

	Attributes
	----------
	logic : logic object
	update_screen : function
	export : function
	_alert_window : alert_window object
	"""
	def __init__(self, update_screen, export, alert_window):
		"""
		Parameters
		----------
		update_screen : function
		export : function
		alert_window : alert_window object
		"""
		self.logic = system.logic()
		self.update_screen = update_screen
		self.export = export
		self._alert_window = alert_window
		facade_logger.info(self.__class__.__name__, self.__init__.__name__, "Initialized")

	def import_pop_get_data(self, name):
		"""
		Calls get data function in system.py, must return true or false based on success or failure.

		Parameters
		----------
		name : str
		"""
		facade_logger.info(self.__class__.__name__, self.import_pop_get_data.__name__, "import_pop_get_data running")
		return self.logic.get_data(name)

	def import_pop_update_database(self):
		"""
		Updates database and then updates the screen. Returns True
		"""
		facade_logger.info(self.__class__.__name__, self.import_pop_update_database.__name__, "import_pop_update_database running")
		res = self.logic.update_database()
		self.update_screen()
		return True

	def import_files(self):
		"""
		Uses default os file selector in order to import files.
		Provides user with alerts based on if there are import issues.
		"""
		filenames = tk.filedialog.askopenfilenames(initialdir="/import")
		if filenames == "":
			print("Cancel Selected!")
		else:
			try:
				filenames_list = list(filenames)
				for filename in filenames_list:
					self.logic.get_data(filename)
				result, count = self.logic.update_database()
				self.update_screen()
				if not result:
					facade_logger.warning(self.__class__.__name__, self.import_files.__name__, f"{count} rows of data not inserted because it is repeated data already in the database")
					self._alert_window(f"{count} rows of data not inserted because \nit is repeated data already in the database \nor do not contian relivant data")
			except:
				facade_logger.warning(self.__class__.__name__, self.import_files.__name__, f"Issue with importing file!")
				self._alert_window(f"Issue with importing file! \nCheck file permissions and data format")


	def export_pop_export_data(self, filename):
		"""
		Calls the export function.

		Parameters
		----------
		filename : str
		"""
		facade_logger.info(self.__class__.__name__, self.export_pop_export_data.__name__, "export_pop_export_data running")
		return self.export(filename)

	def export_pop_no_update(self):
		"""
		Calls the no_update function, then returns True
		"""
		facade_logger.info(self.__class__.__name__, self.export_pop_no_update.__name__, "export_pop_no_update running")
		self.logic.no_update()
		return True

	def exit_button_press(self):
		"""
		Exits out of the program and then returns True.
		"""
		facade_logger.info(self.__class__.__name__, self.exit_button_press.__name__, "exit_button_press running")
		self.logic.exit()
		return True
