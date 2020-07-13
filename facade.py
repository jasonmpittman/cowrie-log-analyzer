from system import *
from ui_class import *

class event_handler:
	def __init__(self, update_screen, export):
		self.logic = logic()
		self.update_screen = update_screen
		self.export = export

	def import_pop_get_data(self, name):
		return self.logic.get_data(name)

	def import_pop_update_database(self):
		res = self.logic.update_database()
		self.update_screen()

	def export_pop_export_data(self, filename):
		return self.export(filename)

	def export_pop_no_update(self):
		self.logic.no_update()
		return True

	def exit_button_press(self):
		self.logic.exit()

	# def update_screen(self):
	# 	self.logic.update_screen()

'''
Maybe system can hand through facade the update screen function to the UI using
another event_handler.
'''
