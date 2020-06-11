from events_class import *

from ui_elements import *

import sys

def exitFunction():
	sys.exit()

def graphWindow():
	graphW = tk.Toplevel(root)
	graphW.title("Graph")

def import_cmd():
	file_name = input_box.Get()
	E.getDataFromFile(file_name)
	E.print_all_src_ips()
	import_window.destroy()

def importWindow():
	global import_window
	import_window = tk.Toplevel(root)
	import_window.title("Import Window")
	global input_box
	input_box = Text_Imput_Section(import_window, "File or directory name: ")
	input_box.Pack("top", 20, 30)
	cancel = standardButton(import_window, exitFunction, "Cancel")
	cancel.Pack("right")
	import_button = standardButton(import_window, import_cmd, "Import")
	import_button.Pack("right")


root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()



fileName = "cowrie.json.2020-03-19"

E = Events()
#E.getDataFromFile(fileName)

first_row = tk.Frame()
first_row.pack(side="top")

second_row = tk.Frame()
second_row.pack(side="top")


IP_Address = ScrollSection(first_row, 10, 20, "Top 10 IP Addresses")
User_names = ScrollSection(first_row, 10, 20, "Top 10 Usernames")
Passwords = ScrollSection(first_row, 10, 20, "Top 10 Passwords")
user_and_pass = ScrollSection(first_row, 10, 20, "Top 10 Username \nPassword Pairs")

download_file = ScrollSection(second_row, 10, 20, "Top 10 Downloads")
origin_country = ScrollSection(second_row, 10, 20, "Top 10 Countries")


#in first_row
IP_Address.Grid(0, 1)
User_names.Grid(0, 2)
Passwords.Grid(0, 3)
user_and_pass.Grid(0,4)

#in second_row
download_file.Grid(0,0)
origin_country.Grid(0,1)


IP_Address.Append(E.topTen("src_ip"))
User_names.Append(E.topTen("username"))
Passwords.Append(E.topTen("password"))
user_and_pass.Append(E.topTen("username", "password"))

#more information needed
download_file.Append(E.topTen("destfile"))
# origin_country.Append()


#bottom buttons
BottomBar = tk.Frame(root)
BottomBar.pack(side="bottom")

Exit = standardButton(BottomBar, exitFunction, "Exit")
Exit.Pack("right")

Graph = standardButton(BottomBar, graphWindow, "Graph")
Graph.Pack("right")

Import = standardButton(BottomBar, importWindow, "Import")
Import.Pack("right")

root.mainloop()
