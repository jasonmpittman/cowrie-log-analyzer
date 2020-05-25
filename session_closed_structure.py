class session_closed_structure:
	def __init__(self, json):
		self.eventid = json["eventid"]
		self.timestamp = json["timestamp"]
		self.message = json["message"]
		self.src_ip = json["src_ip"]
		self.duration = json["duration"]
		self.session = json["session"]
		self.sensor = json["sensor"]

	def printS(self):
		print("eventid: {}".format(self.eventid))
		print("\ttimestamp:")
		print("\t\t{}".format(self.timestamp))
		print("\tmessage:")
		print("\t\t{}".format(self.message))
		print("\tsrc:")
		print("\t\t{}".format(self.src_ip))
		print("\tduration:")
		print("\t\t{}".format(self.duration))
		print("\tsession:")
		print("\t\t{}".format(self.session))
		print("\tsensor:")
		print("\t\t{}\n".format(self.sensor))
