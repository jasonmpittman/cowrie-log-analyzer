from events_class import *

from ui_elements import *

import sys

def exitFunction():
	sys.exit()

def graphWindow():
	graphW = tk.Toplevel(root)
	graphW.title("Graph")

def update_screen():
	IP_Address.Append(E.topTen("src_ip"))
	User_names.Append(E.topTen("username"))
	Passwords.Append(E.topTen("password"))
	user_and_pass.Append(E.topTen("username", "password"))

	#more information needed
	download_file.Append(E.topTen("destfile"))
	origin_country.Append("CO\nCO\nCO\nCO\nCO\nCO\nCO\nCO\nCO\nCO")
	session_duration.Append("SD\nSD\nSD\nSD\nSD\nSD\nSD\nSD\nSD\nSD")
	overall_one.Append("1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.")

root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()



fileName = "cowrie.json.2020-03-19"

E = Events()
#E.getDataFromFile(fileName)

import_pop = Import_Popup(E, update_screen, root)

first_row = tk.Frame()
first_row.pack(side="top")

second_row = tk.Frame()
second_row.pack(side="top")


IP_Address = ScrollSection(first_row, 10, 25, "Top 10 IP Addresses")
User_names = ScrollSection(first_row, 10, 25, "Top 10 Usernames")
Passwords = ScrollSection(first_row, 10, 25, "Top 10 Passwords")
user_and_pass = ScrollSection(first_row, 10, 25, "Top 10 User/Pass Pairs")

download_file = ScrollSection(second_row, 10, 25, "Top 10 Downloads")
origin_country = ScrollSection(second_row, 10, 25, "Top 10 Countries")
session_duration = ScrollSection(second_row, 10, 25, "Top 10 Session Durations")
overall_one = ScrollSection(second_row, 10, 25, "Overall #1")

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

Exit = standardButton(BottomBar, exitFunction, "Exit")
Exit.Pack("right")

Graph = standardButton(BottomBar, graphWindow, "Graph")
Graph.Pack("right")

Import = standardButton(BottomBar, import_pop.import_popup, "Import")
Import.Pack("right")

root.mainloop()
