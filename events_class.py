class Events:
	def __init__(self, events):
		self.events = events

	def printEvents(self):
		for event in self.events:
			event.printEvent()

	def print_all_src_ips(self):
		for event in self.events:
			event.print_src_ip()
