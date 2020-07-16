import events_class
import events_database
import sys
import log

system_logger = log.Logger("system")

class logic:
	def __init__(self):
		self.events_object = events_class.Events()

	def get_data(self, name):
		system_logger.info(self.__class__.__name__, self.get_data.__name__, "get_data called")
		return self.events_object.get_data(name)

	def update_database(self):
		system_logger.info(self.__class__.__name__, self.update_database.__name__, "update_database called")
		conn = events_database.create_connection("events.db")
		config_dict = events_database.get_config()
		test = True
		for event in self.events_object.events:
			res = events_database.add_event(conn, event)
			if not res:
				test = False

		conn.commit()
		conn = events_database.create_connection("events.db")

		return test

	def no_update(self):
		pass

	def exit(self):
		system_logger.info(self.__class__.__name__, self.exit.__name__, "exit called")
		sys.exit()
