import tkinter as tk

import ui_class

import logging

def main():
	logging.basicConfig(level=logging.DEBUG)
	root = tk.Tk()
	logging.info("Root window created")
	root.resizable(False, False)
	root.title("Cowrie Log Analyzer")
	root.configure()


	user_interface = ui_class.ui(root)
	logging.info("UI created")
	user_interface.start_up()
	logging.info("UI drawn")
	root.mainloop()

if __name__ == '__main__':
	main()
