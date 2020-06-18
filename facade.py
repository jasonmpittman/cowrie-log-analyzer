'''
TODO:
	- get the download file names --> thing at the end of the path
	- top 10 countries
	- fix date time
	- rework database stuff


'''


from events_class import *

from ui_elements import *

# from country_database_functions import *

from events_database import *

import sys

def graphWindow():
	graphW = tk.Toplevel(root)
	graphW.title("Graph")


def update_data():
	conn = create_connection("events.db")
	config_dict = get_config()
	for event in E.events:
		add_event(conn, event)

	conn.commit()
	conn = create_connection("events.db")
	update_screen()

def update_screen():
	conn = create_connection("events.db")

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

	sess_res, sess1 = query_top_ten(conn, "duration")
	session_duration.Clear()
	session_duration.Append(sess_res)

	overall_one.Clear()
	overall_one.Append(f"ip: {ip1}\nusr: {usr1}\npass: {pass1}\nUser/Pass: {usr_pass_1} \nDownloads: {download1}\nCountry: {country1}")



root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()



fileName = "cowrie.json.2020-03-19"

E = Events()
#E.getDataFromFile(fileName)

import_pop = PopUp(E.get_data, update_data, root, "Import", "Import", "Not a file or directory", "File or directory name: ")

first_row = tk.Frame()
first_row.pack(side="top")

second_row = tk.Frame()
second_row.pack(side="top")

scroll_section_col = 29
scroll_section_row = 10

IP_Address = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 IP Addresses")
User_names = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 Usernames")
Passwords = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 Passwords")
user_and_pass = ScrollSection(first_row, scroll_section_row, scroll_section_col, "Top 10 User/Pass Pairs")

download_file = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Top 10 Downloads")
origin_country = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Top 10 Countries")
session_duration = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Top 10 Session Durations")
overall_one = ScrollSection(second_row, scroll_section_row, scroll_section_col, "Overall #1")

#in first_row
IP_Address.Grid(0, 1)
User_names.Grid(0, 2)
Passwords.Grid(0, 3)
user_and_pass.Grid(0,4)

#in second_row
download_file.Grid(0, 0)
origin_country.Grid(0, 1)
session_duration.Grid(0, 2)
overall_one.Grid(0, 3)

#bottom buttons
BottomBar = tk.Frame(root)
BottomBar.pack(side="bottom")

Exit = standardButton(BottomBar, sys.exit, "Exit")
Exit.Pack("right")

Graph = standardButton(BottomBar, graphWindow, "Graph")
Graph.Pack("right")

Import = standardButton(BottomBar, import_pop.pop_up, "Import")
Import.Pack("right")

update_screen()

# Export = standardButton(BottomBar, , "Export")

root.mainloop()
