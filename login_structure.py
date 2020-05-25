class login_structure:
	def __init__(self, json):
		self.eventid = json["eventid"]
		self.username = json["username"]
		self.timestamp = json["timestamp"]
		self.message = json["message"]
		self.src_ip = json["src_ip"]
		self.session = json["session"]
		self.password = json["password"]
		self.sensor = json["sensor"]

	def printS(self):
		print("eventid: {}".format(self.eventid))
		print("\ttimestamp:")
		print("\t\t{}".format(self.timestamp))
		print("\tmessage:")
		print("\t\t{}".format(self.message))
		print("\tsrc:")
		print("\t\t{}".format(self.src_ip))
		print("\tsession:")
		print("\t\t{}".format(self.session))
		print("\password:")
		print("\t\t{}".format(self.password))
		print("\tsensor:")
		print("\t\t{}\n".format(self.sensor))
