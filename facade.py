from events_class import *

from ui_elements import *

root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()

fileName = "cowrie.json.2020-03-19"

E = Events()
E.getDataFromFile(fileName)
print(E.topTen("src_ip"))

Command = ScrollSection(root, 10, 20, "Top 10 Commands")
IP_Address = ScrollSection(root, 10, 20, "Top 10 IP Addresses")
User_names = ScrollSection(root, 10, 20, "Top 10 Usernames")
Passwords = ScrollSection(root, 10, 20, "Top 10 Passwords")

Command.Grid(0, 0)
IP_Address.Grid(0, 1)
User_names.Grid(0, 2)
Passwords.Grid(0, 3)

IP_Address.Append(E.topTen("src_ip"))
User_names.Append(E.topTen("username"))
Passwords.Append(E.topTen("password"))

root.mainloop()
