from ui_elements import *
from facade import *
import tkinter as tk
import color_palette
class ui:
	def __init__(self, root):
		'''
		Constant variables that control the size of the top 10 boxes
		'''
		self.palette = color_palette.color("#161925","#23395b","#406e8e","#8ea8c3","#cbf7ed")
		self._info_box_col = 35
		self._info_box_row = 10

		self.eh = event_handler(self.update_screen, self.export)

		self.root = root
		self.root.configure(bg=self.palette.primary)
		'''
		Import and Export pop-up window
		'''
		self.import_pop = PopUp(self.eh.import_pop_get_data, self.eh.import_pop_update_database, self.root, "Import", "Import", "Not a file or directory", "File or directory name: ", self.palette)
		self.export_pop = PopUp(self.eh.export_pop_export_data, self.eh.export_pop_no_update, self.root, "Export", "Export", "", "Name of markdown file: ", self.palette)
		'''
		Creation of the rows, so it can be organized
		'''
		self.first_row = tk.Frame()
		self.first_row.configure(bg=self.palette.primary)
		self.second_row = tk.Frame()
		self.second_row.configure(bg=self.palette.primary)

		'''
		First row of boxes
		'''
		self.ip_address = InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 IP Addresses", self.palette)
		self.user_names = InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 Usernames", self.palette)
		self.passwords = InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 Passwords", self.palette)
		self.user_and_pass = InfoBox(self.first_row, self._info_box_row, self._info_box_col, "Top 10 User/Pass Pairs", self.palette)

		'''
		Second row of boxes
		'''
		self.download_file = InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Top 10 Downloads", self.palette)
		self.origin_country = InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Top 10 Countries", self.palette)
		self.session_duration = InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Top 10 Session Durations", self.palette)
		self.overall_one = InfoBox(self.second_row, self._info_box_row, self._info_box_col, "Overall Number 1", self.palette)


		#Exit button creation and placement
		self.bottom_bar = tk.Frame(self.root)
		self.bottom_bar.configure(bg=self.palette.primary)

		self.exit_button = StandardButton(self.bottom_bar, self.eh.exit_button_press, "Exit", self.palette)


		#Graph selection creation and button creation
		self.graph_selection_menu = selection_menu(self.root, self.palette)
		self.graph_button = StandardButton(self.bottom_bar, self.graph_selection_menu.pop, "Graph", self.palette)


		#Import button and placement
		self.import_button = StandardButton(self.bottom_bar, self.import_pop.pop_up_box, "Import", self.palette)
		#Export button creation
		self.export_button = StandardButton(self.bottom_bar, self.export_pop.pop_up_box, "Export", self.palette)

	def place_first_row(self):
		'''
		Placing the first row in position
		'''
		self.first_row.pack(side="top")
		self.ip_address.grid(0, 1)
		self.user_names.grid(0, 2)
		self.passwords.grid(0, 3)
		self.user_and_pass.grid(0,4)

	def place_second_row(self):
		'''
		Placing the second row in position
		'''
		self.second_row.pack(side="top")
		self.download_file.grid(0, 0)
		self.origin_country.grid(0, 1)
		self.session_duration.grid(0, 2)
		self.overall_one.grid(0, 3)

	def place_button_bar(self):
		'''
		Creation of a bottom bar of buttons
		'''
		self.bottom_bar.pack(side="bottom")
		self.exit_button.pack("right")
		self.graph_button.pack("right")
		self.import_button.pack("right")
		self.export_button.pack("right")

	'''
	Exports the information to a file that the user specifies
	Input: filename --> name of file with or without .md on the end --> it will handle it either way
	'''
	def export(self, filename):
		extention = filename[-3::]
		if extention != ".md":
			filename = filename + ".md"

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
		return True

	# '''
	# update_screen --> updates all the visible data with what is in the datebase
	# '''
	def update_screen(self):
		conn = create_connection("events.db")
		try:
			ip_res, ip1 = query_top_ten(conn, "ip_address")
			self.ip_address.clear()
			self.ip_address.append(ip_res)

			usr_res, usr1 = query_top_ten(conn, "username")
			self.user_names.clear()
			self.user_names.append(usr_res)

			pass_res, pass1 = query_top_ten(conn, "password")
			self.passwords.clear()
			self.passwords.append(pass_res)

			user_pass_res, usr_pass_1 = top_ten_user_pass(conn)
			self.user_and_pass.clear()
			self.user_and_pass.append(user_pass_res)

			#more information needed
			download_res, download1 = query_top_ten(conn, "filename")
			self.download_file.clear()
			self.download_file.append(download_res)

			country_res, country1 = query_top_ten(conn, "country")
			self.origin_country.clear()
			self.origin_country.append(country_res)

			sess_res, sess1 = longest_durations()
			self.session_duration.clear()
			self.session_duration.append(sess_res)

			self.overall_one.clear()
			self.overall_one.append(f"- ip: {ip1}\n- usr: {usr1}\n- pass: {pass1}\n- User/Pass: {usr_pass_1} \n- Downloads: {download1}\n- Country: {country1}\n- Duration: {sess1}")
		except:
			print("Please Import Data")


	def start_up(self):
		self.place_first_row()
		self.place_second_row()
		self.place_button_bar()
		self.update_screen()
