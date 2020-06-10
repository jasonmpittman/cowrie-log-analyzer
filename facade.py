from events_class import *

from ui_elements import *

import sys

def exitFunction():
	sys.exit()

def graphWindow():
	graphW = tk.Toplevel(root)
	graphW.title("Graph")

root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()

fileName = "cowrie.json.2020-03-19"

E = Events()
E.getDataFromFile(fileName)

first_row = tk.Frame()
first_row.pack(side="top")

second_row = tk.Frame()
second_row.pack(side="top")


IP_Address = ScrollSection(first_row, 10, 20, "Top 10 IP Addresses")
User_names = ScrollSection(first_row, 10, 20, "Top 10 Usernames")
Passwords = ScrollSection(first_row, 10, 20, "Top 10 Passwords")
user_and_pass = ScrollSection(second_row, 10, 20, "Top 10 Username \nPassword Pairs")


#in first_row
IP_Address.Grid(0, 1)
User_names.Grid(0, 2)
Passwords.Grid(0, 3)

#in second_row
user_and_pass.Grid(0,0)


IP_Address.Append(E.topTen("src_ip"))
User_names.Append(E.topTen("username"))
Passwords.Append(E.topTen("password"))
user_and_pass.Append(E.topTen("username", "password"))

BottomBar = tk.Frame(root)
BottomBar.pack(side="bottom")

Exit = standardButton(BottomBar, exitFunction , "Exit")
Exit.Pack("right")

Graph = standardButton(BottomBar, graphWindow, "Graph")
Graph.Pack("right")


root.mainloop()
