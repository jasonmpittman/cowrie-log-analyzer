import facade

import tkinter as tk

root = tk.Tk()
root.title("Cowrie Log Analyzer")
root.configure()

F = facade.Facade(root)
F.start_up()

root.mainloop()
