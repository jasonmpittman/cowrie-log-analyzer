from events_class import *
from events_database import *
import sys

class logic:
	def __init__(self):
		self.events_object = Events()

	def get_data(self, name):
		return self.events_object.get_data(name)

	def update_database(self):
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
		sys.exit()
