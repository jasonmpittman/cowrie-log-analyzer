import tkinter as tk

import ui_class

def main():
	root = tk.Tk()
	root.title("Cowrie Log Analyzer")
	root.configure()

	user_interface = ui_class.ui(root)
	
	user_interface.start_up()

	root.mainloop()

if __name__ == '__main__':
	main()
