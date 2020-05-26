class Event:
	def __init__(self, json):
		self.event = json

	def printEvent(self):
		print(self.event)

	def print_src_ip(self):
		try:
			print(self.event["src_ip"])
		except:
			pass

	def print_src_port(self):
		try:
			print("src_port:", self.event["src_port"])
		except:
			pass
