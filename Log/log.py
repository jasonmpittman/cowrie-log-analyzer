#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "logging"


import logging

class Logger:
	"""
	This class is in charge of handling all the logging.

	Attributes
	----------
	logger : logger object
	file_handler : FileHandler object
	formatter : Formatter object
	"""
	def __init__(self, name):
		"""
		Sets up a logger with the provided name.

		Parameters
		----------
		name : str
		"""
		self.logger = logging.getLogger(name)
		self.logger.setLevel(logging.INFO)
		self.file_handler = logging.FileHandler("Log/logfile.log")
		self.formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s:%(message)s")
		self.file_handler.setFormatter(self.formatter)
		self.logger.addHandler(self.file_handler)

	def info(self, class_name, function_name, message):
		"""
		Info logging level message creation.

		Parameters
		----------
		class_name : str
		function_name : str
		message : str
		"""
		if class_name == "":
			self.logger.info(f"{function_name} - {message}")
		else:
			self.logger.info(f"{class_name}.{function_name} - {message}")

	def warning(self, class_name, function_name, message):
		"""
		Warning logging level message creation.

		Parameters
		----------
		class_name : str
		function_name : str
		message : str
		"""
		if class_name == "":
			self.logger.warning(f"{function_name} - {message}")
		else:
			self.logger.warning(f"{class_name}.{function_name} - {message}")

	def error(self, message):
		"""
		Error logging level message creation.

		Parameters
		----------
		message : str
		"""
		self.logger.error(message)
