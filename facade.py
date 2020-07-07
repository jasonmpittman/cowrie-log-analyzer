from system import *
# from client import *

class event_handler:
	def __init__(self):
		self.logic = logic()

	def import_pop_get_data(self):
		return self.logic.get_data()

	def import_pop_update_database(self):
		return self.logic.update_database

	def export_pop_export_data(self):
		return self.logic.export

	def export_pop_no_update(self):
		return self.logic.no_update

	def exit_button_press(self):
		return self.logic.exit()


'''
Maybe system can hand through facade the update screen function to the UI using
another event_handler.
'''
