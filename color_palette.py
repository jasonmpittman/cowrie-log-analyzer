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

class color:
	"""
	A class used to hold hex value color pallette for the UI
	
	Attributes:
	----------
	
	primary : str
	secondary_a : str
	secondary_b : str
	accent_a : str
	accent_b : str
	"""
	
	def __init__(self, primary, secondary_a, secondary_b, accent_a, accent_b):
		"""
		Parameters
		----------
		
		primary : str
		secondary_a : str
		secondary_b : str
		accent_a : str
		accent_b : str
		"""
		
		self.primary = primary
		self.secondary_a = secondary_a
		self.secondary_b = secondary_b
		self.accent_a = accent_a
		self.accent_b = accent_b
