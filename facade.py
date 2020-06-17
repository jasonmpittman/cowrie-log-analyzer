'''
TODO:
	- get the download file names --> thing at the end of the path
	- top 10 countries


'''


from events_class import *

from ui_elements import *

from country_database_functions import *

from events_database_functions import *
import sys


def graphWindow():
	graphW = tk.Toplevel(root)
	graphW.title("Graph")

def update_screen():
	ip_res, ip1 = E.topTen("src_ip")
	IP_Address.Append(ip_res)

	usr_res, usr1 = E.topTen("username")
	User_names.Append(usr_res)

	pass_res, pass1 = E.topTen("password")
	Passwords.Append(pass_res)

	user_pass_res, usr_pass_1 = E.topTen("username", "password")
	user_and_pass.Append(user_pass_res)

	#more information needed
	download_res, download1 = E.topTen("destfile")
	download_file.Append(download_res)

	country_res, country1 = ("CO\nCO\nCO\nCO\nCO\nCO\nCO\nCO\nCO\nCO", "CO1")
	origin_country.Append(country_res)

	sess_res, sess1 = E.topTen("duration")
	session_duration.Append(sess_res)

	overall_one.Append(f"ip: {ip1}\nusr: {usr1}\npass: {pass1}\nUser/Pass: {usr_pass_1} \nDownloads: {download1}\nCountry: {country1}")
	config_dict = get_config()

	for e in E.events:
		get_type(e.event["eventid"], config_dict)


root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()



fileName = "cowrie.json.2020-03-19"

E = Events()
#E.getDataFromFile(fileName)

import_pop = PopUp(E.get_data, update_screen, root, "Import", "Import", "Not a file or directory", "File or directory name: ")

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

# Export = standardButton(BottomBar, , "Export")

root.mainloop()
