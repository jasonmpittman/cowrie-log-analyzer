from ui_elements import *

class facade:
	def __init__(self, root):
		self.root = root
		self.E = Events()
		'''
		Import and Export pop-up window
		should be in a client class
		'''
		self.import_pop = PopUp(self.E.get_data, update_data, self.root, "Import", "Import", "Not a file or directory", "File or directory name: ")
		self.export_pop = PopUp(Export, no_update, self.root, "Export", "Export", "", "Name of markdown file: ")
		'''
		Creation of the rows, so it can be organized
		'''
		self.first_row = tk.Frame()


		self.second_row = tk.Frame()

		'''
		Constant variables that control the size of the top 10 boxes
		'''
		self.scroll_section_col = 35
		self.scroll_section_row = 10

		'''
		First row of boxes
		'''
		self.ip_address = ScrollSection(self.first_row, self.scroll_section_row, scroll_section_col, "Top 10 IP Addresses")
		self.user_names = ScrollSection(self.first_row, self.scroll_section_row, scroll_section_col, "Top 10 Usernames")
		self.passwords = ScrollSection(self.first_row, self.scroll_section_row, scroll_section_col, "Top 10 Passwords")
		self.user_and_pass = ScrollSection(self.first_row, self.scroll_section_row, scroll_section_col, "Top 10 User/Pass Pairs")

		'''
		Second row of boxes
		'''
		self.download_file = ScrollSection(self.second_row, self.scroll_section_row, scroll_section_col, "Top 10 Downloads")
		self.origin_country = ScrollSection(self.second_row, self.scroll_section_row, scroll_section_col, "Top 10 Countries")
		self.session_duration = ScrollSection(self.second_row, self.scroll_section_row, scroll_section_col, "Top 10 Session Durations")
		self.overall_one = ScrollSection(self.second_row, self.scroll_section_row, scroll_section_col, "Overall #1")

		#Exit button creation and placement
		self.exit = standardButton(self.bottom_bar, sys.exit, "Exit")


		#Graph selection creation and button creation
		self.graph_selection_menu = Selection_menu(self.root)
		self.graph_button = standardButton(self.bottom_bar, self.graph_selection_menu.Pop, "Graph")


		#Import button and placement
		self.import = standardButton(self.bottom_bar, self.import_pop.pop_up, "Import")


		#Export button creation
		self.export = standardButton(self.bottom_bar, self.export_pop.pop_up, "Export")

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
		self.bottom_bar = tk.Frame(self.root)
		self.bottom_bar.pack(side="bottom")
		self.exit.Pack("right")
		self.graph_button.Pack("right")
		self.import.Pack("right")
		self.export.Pack("right")
