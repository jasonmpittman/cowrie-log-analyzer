#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "tkinter, ui_class, log"

import tkinter as tk

from UI import ui_class

from Log import log

def main():
	"""
	Function constructs logger, tkinter, and ui_class objects
	"""
	c_logger = log.Logger("client")
	root = tk.Tk()
	c_logger.info("", main.__name__, "Root window created")
	root.resizable(False, False)
	root.title("Cowrie Log Analyzer")
	root.configure()


	user_interface = ui_class.ui(root)
	c_logger.info("", main.__name__, "UI class object created")
	user_interface.start_up()
	c_logger.info("", main.__name__, "UI drawn in root window")
	root.mainloop()

if __name__ == '__main__':
	main()
