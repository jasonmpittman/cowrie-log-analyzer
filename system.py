from events_class import *
from events_database import *
import sys
import log

system_logger = log.Logger("system")

class logic:
	def __init__(self):
		self.events_object = Events()

	def get_data(self, name):
		system_logger.info(self.__class__.__name__, self.get_data.__name__, "get_data called")
		return self.events_object.get_data(name)

	def update_database(self):
		system_logger.info(self.__class__.__name__, self.update_database.__name__, "update_database called")
		conn = create_connection("events.db")
		config_dict = get_config()
		test = True
		for event in self.events_object.events:
			res = add_event(conn, event)
			if not res:
				test = False

		conn.commit()
		conn = create_connection("events.db")

		return test

	def no_update(self):
		pass

	def exit(self):
		system_logger.info(self.__class__.__name__, self.exit.__name__, "exit called")
		sys.exit()
