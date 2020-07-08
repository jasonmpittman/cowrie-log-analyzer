class Event:
	def __init__(self, json):
		self.event = json

	def printEvent(self):
		print(self.event)

	'''
	returns the value for the given key or "-" if it does not have one
	'''

	def get(self, key):
		try:
			return self.event[key]
		except:
			return "-"
