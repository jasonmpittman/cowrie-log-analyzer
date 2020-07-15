import system
import log

facade_logger = log.Logger("facade")
class event_handler:
	def __init__(self, update_screen, export):
		self.logic = system.logic()
		self.update_screen = update_screen
		self.export = export
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
