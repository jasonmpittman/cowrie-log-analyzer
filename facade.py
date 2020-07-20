import system
import log
import tkinter as tk

facade_logger = log.Logger("facade")

class event_handler:
	def __init__(self, update_screen, export, alert_window):
		self.logic = system.logic()
		self.update_screen = update_screen
		self.export = export
		self._alert_window = alert_window
		facade_logger.info(self.__class__.__name__, self.__init__.__name__, "Initialized")

	'''
	All of these functions are handed over to to buttons to be called. The buttons call these functions.
	Requirements: Must return True or False in the context of the function being successful in its execution or not successful.
	'''
	def import_pop_get_data(self, name):
		facade_logger.info(self.__class__.__name__, self.import_pop_get_data.__name__, "import_pop_get_data running")
		return self.logic.get_data(name)

	def import_pop_update_database(self):
		facade_logger.info(self.__class__.__name__, self.import_pop_update_database.__name__, "import_pop_update_database running")
		res = self.logic.update_database()
		self.update_screen()
		return True

	def import_files(self):
		filenames = tk.filedialog.askopenfilenames(initialdir="/import")
		if filenames == "":
			print("Cancel Selected!")
		else:
			filenames_list = list(filenames)
			for filename in filenames_list:
				self.logic.get_data(filename)
			result, count = self.logic.update_database()
			if not result:
				print(f"{count} rows of data not inserted because it is repeated data already in the database")
				self._alert_window(f"{count} rows of data not inserted because \nit is repeated data already in the database")

	def export_pop_export_data(self, filename):
		facade_logger.info(self.__class__.__name__, self.export_pop_export_data.__name__, "export_pop_export_data running")
		return self.export(filename)

	def export_pop_no_update(self):
		facade_logger.info(self.__class__.__name__, self.export_pop_no_update.__name__, "export_pop_no_update running")
		self.logic.no_update()
		return True

	def exit_button_press(self):
		facade_logger.info(self.__class__.__name__, self.exit_button_press.__name__, "exit_button_press running")
		self.logic.exit()
		return True
