from ui_elements import *
from facade import *
import tkinter as tk

class ui:
	def __init__(self, root):
		'''
		Constant variables that control the size of the top 10 boxes
		'''
		self.scroll_section_col = 35
		self.scroll_section_row = 10

		self.eh = event_handler()

		self.root = root
		self.E = Events()
		'''
		Import and Export pop-up window
		'''
		self.import_pop = PopUp(self.eh.import_pop_get_data(), self.eh.import_pop_update_database(), self.root, "Import", "Import", "Not a file or directory", "File or directory name: ")
		self.export_pop = PopUp(self.eh.export_pop_export_data(), self.eh.export_pop_no_update(), self.root, "Export", "Export", "", "Name of markdown file: ")
		'''
		Creation of the rows, so it can be organized
		'''
		self.first_row = tk.Frame()
		self.second_row = tk.Frame()

		'''
		First row of boxes
		'''
		self.ip_address = ScrollSection(self.first_row, self.scroll_section_row, self.scroll_section_col, "Top 10 IP Addresses")
		self.user_names = ScrollSection(self.first_row, self.scroll_section_row, self.scroll_section_col, "Top 10 Usernames")
		self.passwords = ScrollSection(self.first_row, self.scroll_section_row, self.scroll_section_col, "Top 10 Passwords")
		self.user_and_pass = ScrollSection(self.first_row, self.scroll_section_row, self.scroll_section_col, "Top 10 User/Pass Pairs")

		'''
		Second row of boxes
		'''
		self.download_file = ScrollSection(self.second_row, self.scroll_section_row, self.scroll_section_col, "Top 10 Downloads")
		self.origin_country = ScrollSection(self.second_row, self.scroll_section_row, self.scroll_section_col, "Top 10 Countries")
		self.session_duration = ScrollSection(self.second_row, self.scroll_section_row, self.scroll_section_col, "Top 10 Session Durations")
		self.overall_one = ScrollSection(self.second_row, self.scroll_section_row, self.scroll_section_col, "Overall Number 1")


		#Exit button creation and placement
		self.bottom_bar = tk.Frame(self.root)

		self.exit_button = standardButton(self.bottom_bar, self.eh.exit_button_press(), "Exit")


		#Graph selection creation and button creation
		self.graph_selection_menu = Selection_menu(self.root)
		self.graph_button = standardButton(self.bottom_bar, self.graph_selection_menu.Pop, "Graph")


		#Import button and placement
		self.import_button = standardButton(self.bottom_bar, self.import_pop.pop_up, "Import")
		#Export button creation
		self.export_button = standardButton(self.bottom_bar, self.export_pop.pop_up, "Export")

	def place_first_row(self):
		'''
		Placing the first row in position
		'''
		self.first_row.pack(side="top")
		self.ip_address.Grid(0, 1)
		self.user_names.Grid(0, 2)
		self.passwords.Grid(0, 3)
		self.user_and_pass.Grid(0,4)

	def place_second_row(self):
		'''
		Placing the second row in position
		'''
		self.second_row.pack(side="top")
		self.download_file.Grid(0, 0)
		self.origin_country.Grid(0, 1)
		self.session_duration.Grid(0, 2)
		self.overall_one.Grid(0, 3)

	def place_button_bar(self):
		'''
		Creation of a bottom bar of buttons
		'''
		self.bottom_bar.pack(side="bottom")
		self.exit_button.Pack("right")
		self.graph_button.Pack("right")
		self.import_button.Pack("right")
		self.export_button.Pack("right")

	'''
	Exports the information to a file that the user specifies
	Input: filename --> name of file with or without .md on the end --> it will handle it either way
	'''
	# def export(self, filename):
	# 	extention = filename[-3::]
	# 	if extention != ".md":
	# 		filename = filename + ".md"
	#
	# 	str_output = "#Text Output\n"
	# 	str_output += self.ip_address.export_md()
	# 	str_output += self.user_names.export_md()
	# 	str_output += self.passwords.export_md()
	# 	str_output += self.user_and_pass.export_md()
	# 	str_output += self.download_file.export_md()
	# 	str_output += self.origin_country.export_md()
	# 	str_output += self.session_duration.export_md()
	# 	str_output += "\n"
	# 	str_output += self.overall_one.export_md()
	#
	# 	with open(filename, "w") as f:
	# 		f.write(str_output)
	# 	return True

	# '''
	# update_screen --> updates all the visible data with what is in the datebase
	# '''
	def update_screen(self):
		conn = create_connection("events.db")
		try:
			ip_res, ip1 = query_top_ten(conn, "ip_address")
			self.ip_address.Clear()
			self.ip_address.Append(ip_res)

			usr_res, usr1 = query_top_ten(conn, "username")
			self.user_names.Clear()
			self.user_names.Append(usr_res)

			pass_res, pass1 = query_top_ten(conn, "password")
			self.passwords.Clear()
			self.passwords.Append(pass_res)

			user_pass_res, usr_pass_1 = top_ten_user_pass(conn)
			self.user_and_pass.Clear()
			self.user_and_pass.Append(user_pass_res)

			#more information needed
			download_res, download1 = query_top_ten(conn, "filename")
			self.download_file.Clear()
			self.download_file.Append(download_res)

			country_res, country1 = query_top_ten(conn, "country")
			self.origin_country.Clear()
			self.origin_country.Append(country_res)

			sess_res, sess1 = longest_durations()
			self.session_duration.Clear()
			self.session_duration.Append(sess_res)

			self.overall_one.Clear()
			self.overall_one.Append(f"- ip: {ip1}\n- usr: {usr1}\n- pass: {pass1}\n- User/Pass: {usr_pass_1} \n- Downloads: {download1}\n- Country: {country1}\n- Duration: {sess1}")
		except:
			print("Please Import Data")

	# def no_update(self):
	# 	pass

	def start_up(self):
		self.place_first_row()
		self.place_second_row()
		self.place_button_bar()
		self.update_screen()

	# def update_data(self):
	# 	conn = create_connection("events.db")
	# 	config_dict = get_config()
	# 	for event in E.events:
	# 		add_event(conn, event)
	#
	# 	conn.commit()
	# 	conn = create_connection("events.db")
	# 	update_screen()
