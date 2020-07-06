'''
TODO

'''

from events_class import *

from ui_elements import *

from events_database import *

import sys

'''
update_data function creates updates the database then the screen
'''
def update_data():
	conn = create_connection("events.db")
	config_dict = get_config()
	for event in E.events:
		add_event(conn, event)

	conn.commit()
	conn = create_connection("events.db")
	update_screen()

'''
Exports the information to a file that the user specifies
Input: filename --> name of file with or without .md on the end --> it will handle it either way
'''

#this would be in facade
def Export(filename):
	extention = filename[-3::]
	if extention != ".md":
		filename = filename + ".md"

	str_output = "#Text Output\n"
	str_output += IP_Address.export_md()
	str_output += User_names.export_md()
	str_output += Passwords.export_md()
	str_output += user_and_pass.export_md()
	str_output += download_file.export_md()
	str_output += origin_country.export_md()
	str_output += session_duration.export_md()
	str_output += "\n"
	str_output += overall_one.export_md()
	with open(filename, "w") as f:
		f.write(str_output)
	return True

'''
update_screen --> updates all the visible data with what is in the datebase
'''
def update_screen():
	conn = create_connection("events.db")
	try:
		ip_res, ip1 = query_top_ten(conn, "ip_address")
		IP_Address.Clear()
		IP_Address.Append(ip_res)

		usr_res, usr1 = query_top_ten(conn, "username")
		User_names.Clear()
		User_names.Append(usr_res)

		pass_res, pass1 = query_top_ten(conn, "password")
		Passwords.Clear()
		Passwords.Append(pass_res)

		user_pass_res, usr_pass_1 = top_ten_user_pass(conn)
		user_and_pass.Clear()
		user_and_pass.Append(user_pass_res)


		#more information needed
		download_res, download1 = query_top_ten(conn, "filename")
		download_file.Clear()
		download_file.Append(download_res)

		country_res, country1 = query_top_ten(conn, "country")
		origin_country.Clear()
		origin_country.Append(country_res)

		sess_res, sess1 = longest_durations()
		session_duration.Clear()
		session_duration.Append(sess_res)

		overall_one.Clear()
		overall_one.Append(f"- ip: {ip1}\n- usr: {usr1}\n- pass: {pass1}\n- User/Pass: {usr_pass_1} \n- Downloads: {download1}\n- Country: {country1}\n- Duration: {sess1}")
	except:
		print("Please Import Data")

'''
The main window!
'''
root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()

E = Events()

'''
Import and Export pop-up window
should be in a client class
'''
import_pop = PopUp(E.get_data, update_data, root, "Import", "Import", "Not a file or directory", "File or directory name: ")

export_pop = PopUp(Export, no_update, root, "Export", "Export", "", "Name of markdown file: ")

'''
Creation of the rows, so it can be organized
'''
first_row = tk.Frame()
first_row.pack(side="top")

second_row = tk.Frame()
second_row.pack(side="top")

'''
Constant variables that control the size of the top 10 boxes
'''
scroll_section_col = 35
scroll_section_row = 10

'''
First row of boxes
'''
IP_Address = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 IP Addresses")
User_names = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 Usernames")
Passwords = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 Passwords")
user_and_pass = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 User/Pass Pairs")

'''
Second row of boxes
'''
download_file = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Top 10 Downloads")
origin_country = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Top 10 Countries")
session_duration = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Top 10 Session Durations")
overall_one = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Overall #1")

'''
Placing the first row in position
'''
IP_Address.Grid(0, 1)
User_names.Grid(0, 2)
Passwords.Grid(0, 3)
user_and_pass.Grid(0,4)

'''
Placing the second row in position
'''
download_file.Grid(0, 0)
origin_country.Grid(0, 1)
session_duration.Grid(0, 2)
overall_one.Grid(0, 3)

'''
Creation of a bottom bar of buttons
'''
BottomBar = tk.Frame(root)
BottomBar.pack(side="bottom")

#Exit button creation and placement
Exit = standardButton(BottomBar, sys.exit, "Exit")
Exit.Pack("right")

#Graph selection creation and button creation
Graph_selection_menu = Selection_menu(root)
Graph_button = standardButton(BottomBar, Graph_selection_menu.Pop, "Graph")
Graph_button.Pack("right")

#Import button and placement
Import = standardButton(BottomBar, import_pop.pop_up, "Import")
Import.Pack("right")

#Export button creation
Export = standardButton(BottomBar, export_pop.pop_up, "Export")
Export.Pack("right")

update_screen()

root.mainloop()
