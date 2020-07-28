#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "ui_elements, facade, tkinter, color_palette, log, events_database"

from UI import ui_elements

import facade

import tkinter as tk

from UI import color_palette

from Log import log

from Events import events_database

ui_class_logger = log.Logger("ui_class")

class ui:
	"""
	Attributes
	----------
	palette : color_palette object
	_info_box_col : int
	_info_box_row : int
	root : tk.Tk object
	alert : alert window object
	eh : event handler object
	import_pop : PopUp object
	export_pop : PopUp object
	first_row : tk.Frame object
	second_row : tk.Frame object
	ip_address : InfoBox object
	user_names : InfoBox object
	passwords : InfoBox object
	user_and_pass : InfoBox object
	download_file : InfoBox object
	origin_country : InfoBox object
	session_duration : InfoBox object
	overall_one : InfoBox object
	bottom_bar : tk.Frame object
	exit_button : StandardButton object
	graph_button : StandardButton object
	import_button : StandardButton object
	export_button : StandardButton object
	graph_selection_menu : SelectionMenu object

	"""
	def __init__(self, root):
		"""
		Constant variables that control the size of the top 10 boxes

		Parameters
		----------
		root : tk.Tk object
		"""

		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "Palette initialization")
		self.palette = color_palette.color("#161925","#23395b","#406e8e","#8ea8c3","#cbf7ed")
		self._info_box_col = 35
		self._info_box_row = 10

		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "Event handler creation")


		self.root = root
		self.root.configure(bg=self.palette.primary)

		self.alert = ui_elements.alert_window(self.root, self.palette)
		self.eh = facade.event_handler(self.update_screen, self.export, self.alert.pop_up)
		'''
		Import and Export pop-up window
		'''
		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "Import and export pop-ups initialization")
		self.import_pop = ui_elements.PopUp(self.eh.import_pop_get_data, self.eh.import_pop_update_database, self.root, "Import", "Import", "Not a file or directory", "File or directory name: ", self.palette)
		self.export_pop = ui_elements.PopUp(self.eh.export_pop_export_data, self.eh.export_pop_no_update, self.root, "Export", "Export", "", "Name of markdown file: ", self.palette)
		'''
		Creation of the rows, so it can be organized
		'''
		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "First and second row creation")
		self.first_row = tk.Frame()
		self.first_row.configure(bg=self.palette.primary)
		self.second_row = tk.Frame()
		self.second_row.configure(bg=self.palette.primary)

		'''
		First row of boxes
		'''
		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "Creation of first row of boxes")
		self.ip_address = ui_elements.InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 IP Addresses", self.palette)
		self.user_names = ui_elements.InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 Usernames", self.palette)
		self.passwords = ui_elements.InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 Passwords", self.palette)
		self.user_and_pass = ui_elements.InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 User/Pass Pairs", self.palette)

		'''
		Second row of boxes
		'''
		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "Creation of second row of boxes")
		self.download_file = ui_elements.InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Top 10 Downloads", self.palette)
		self.origin_country = ui_elements.InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Top 10 Countries", self.palette)
		self.session_duration = ui_elements.InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Top 10 Session Durations", self.palette)
		self.overall_one = ui_elements.InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Overall Number 1", self.palette)


		#Exit button creation and placement
		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "Creation of bottom bar")
		self.bottom_bar = tk.Frame(self.root)
		self.bottom_bar.configure(bg=self.palette.primary)
		self.exit_button = ui_elements.StandardButton(self.bottom_bar, self.eh.exit_button_press, "Exit", self.palette)


		#Graph selection creation and button creation
		ui_class_logger.info(self.__class__.__name__, self.__init__.__name__, "Graph portion creation")
		self.graph_selection_menu = ui_elements.SelectionMenu(self.root, self.palette)
		self.graph_button = ui_elements.StandardButton(self.bottom_bar, self.graph_selection_menu.pop, "Graph", self.palette)


		#Import button and placement
		# self.import_button = ui_elements.StandardButton(self.bottom_bar, self.import_pop.pop_up_box, "Import", self.palette)

		self.import_button = ui_elements.StandardButton(self.bottom_bar, self.eh.import_files, "Import", self.palette)
		#Export button creation
		self.export_button = ui_elements.StandardButton(self.bottom_bar, self.export_pop.pop_up_box, "Export", self.palette)

	def _place_first_row(self):
		"""
		Places the first row in position.
		"""
		ui_class_logger.info(self.__class__.__name__, self._place_first_row.__name__, "First row placement")
		self.first_row.pack(side="top")
		self.ip_address.grid(0, 1)
		self.user_names.grid(0, 2)
		self.passwords.grid(0, 3)
		self.user_and_pass.grid(0,4)

	def _place_second_row(self):
		"""
		Places the second row in position.
		"""
		ui_class_logger.info(self.__class__.__name__, self._place_second_row.__name__, "Secord row placement")
		self.second_row.pack(side="top")
		self.download_file.grid(0, 0)
		self.origin_country.grid(0, 1)
		self.session_duration.grid(0, 2)
		self.overall_one.grid(0, 3)

	def _place_button_bar(self):
		"""
		Places bottom bar of buttons and places those buttons in the bar.
		"""
		ui_class_logger.info(self.__class__.__name__, self._place_button_bar.__name__, "Bottom bar placement")
		self.bottom_bar.pack(side="bottom")
		self.exit_button.pack("right")
		self.graph_button.pack("right")
		self.import_button.pack("right")
		self.export_button.pack("right")


	def export(self, filename):
		"""
		Exports the information to a file that the user specifies
		Input: filename --> name of file with or without .md on the end --> it will handle it either way

		Parameters
		----------
		filename : str
		"""
		self.export_alert = ui_elements.alert_window(self.root, self.palette)
		try:
			ui_class_logger.info(self.__class__.__name__, self.export.__name__, "Export")
			extention = filename[-3::]
			if extention != ".md":
				filename = filename + ".md"
				ui_class_logger.info(self.__class__.__name__, self.export.__name__, ".md added")

			str_output = "#Text Output\n"
			str_output += self.ip_address.export_md()
			str_output += self.user_names.export_md()
			str_output += self.passwords.export_md()
			str_output += self.user_and_pass.export_md()
			str_output += self.download_file.export_md()
			str_output += self.origin_country.export_md()
			str_output += self.session_duration.export_md()
			str_output += "\n"
			str_output += self.overall_one.export_md()

			with open(filename, "w") as f:
				f.write(str_output)
			ui_class_logger.info(self.__class__.__name__, self.export.__name__, f"Written to {str_output} file")
			self.export_alert.pop_up("Export Successful")
			return True
		except:
			ui_class_logger.info(self.__class__.__name__, self.export.__name__, f"Failed to write to {str_output} file")
			self.export_alert.pop_up("Export failed")
			return False

	def update_screen(self):
		"""
		update_screen --> updates all the visible data with what is in the datebase
		"""
		conn = events_database.create_connection()
		ui_class_logger.info(self.__class__.__name__, self.update_screen.__name__, "Performing screen update")
		try:
			ip_res, ip1 = events_database.query_top_ten(conn, "ip_address")
			self.ip_address.clear()
			self.ip_address.append(ip_res)

			usr_res, usr1 = events_database.query_top_ten(conn, "username")
			self.user_names.clear()
			self.user_names.append(usr_res)

			pass_res, pass1 = events_database.query_top_ten(conn, "password")
			self.passwords.clear()
			self.passwords.append(pass_res)

			user_pass_res, usr_pass_1 = events_database.top_ten_user_pass(conn)
			self.user_and_pass.clear()
			self.user_and_pass.append(user_pass_res)

			#more information needed
			download_res, download1 = events_database.query_top_ten(conn, "filename")
			self.download_file.clear()
			self.download_file.append(download_res)

			country_res, country1 = events_database.query_top_ten(conn, "country")
			self.origin_country.clear()
			self.origin_country.append(country_res)

			sess_res, sess1 = events_database.longest_durations()
			self.session_duration.clear()
			self.session_duration.append(sess_res)

			self.overall_one.clear()
			self.overall_one.append(f"- ip: {ip1}\n- usr: {usr1}\n- pass: {pass1}\n- User/Pass: {usr_pass_1} \n- Downloads: {download1}\n- Country: {country1}\n- Duration: {sess1}")
			ui_class_logger.info(self.__class__.__name__, self.update_screen.__name__, "Successfully updated")
		except:
			ui_class_logger.info(self.__class__.__name__, self.update_screen.__name__, "Screen update failed")
			self.update_screen_alert = ui_elements.alert_window(self.root, self.palette)
			self.update_screen_alert.pop_up(f"Please import data")
			print("Please Import Data")


	def start_up(self):
		"""
		Runs when starting up the application. It gets everything placed, setup, and displayed.
		"""
		ui_class_logger.info(self.__class__.__name__, self.start_up.__name__, "Running start up...")
		self._place_first_row()
		self._place_second_row()
		self._place_button_bar()
		self.update_screen()
