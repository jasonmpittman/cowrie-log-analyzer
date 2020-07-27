class Event:
	"""
	This is the event class which holds the data for an event
	Properties
	----------
	event : python dictionary
	"""
	def __init__(self, json):
		"""
		Parameters
		----------
		json : python dictionary
		"""
		self.event = json

	def printEvent(self):
		print(self.event)

	'''
	Get function:
	returns the value for the given key or "-" if it does not have one, otherwise it returns the event key
	'''
	def get(self, key):
		"""
		Parameters
		----------
		key : str
		"""
		try:
			return self.event[key]
		except:
			return "-"
