class command_structure:
	def __init__(self, json):
		self.eventid = json["eventid"]
		self.timestamp = json["timestamp"]
		self.message = json["message"]
		self.session = json["session"]
		self.input = json["input"]
		self.sensor = json["sensor"]

	def printS(self):
		print("eventid: {}".format(self.eventid))
		print("\ttimestamp:")
		print("\t\t{}".format(self.timestamp))
		print("\tmessage:")
		print("\t\t{}".format(self.message))
		print("\tsession:")
		print("\t\t{}".format(self.session))
		print("\tinput:")
		print("\t\t{}".format(self.input))
		print("\tsensor:")
		print("\t\t{}\n".format(self.sensor))
