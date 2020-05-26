class Event:
	def __init__(self, json):
		self.event = json

	def printEvent(self):
		print(self.event)

	def print_src_ip(self):
		print(self.event["src_ip"])
