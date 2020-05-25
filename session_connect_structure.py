
class session_connect_structure:
	def __init__(self, json):
		self.eventid = json["eventid"]
		self.src_ip = json["src_ip"]
		self.src_port = json["src_port"]

		self.dst_ip = json["dst_ip"]
		self.dst_port = json["dst_port"]

		self.timestamp = json["timestamp"]
		self.message = json["message"]
		self.protocol = json["protocol"]
		self.session = json["session"]
		self.sensor = json["sensor"]

	def printS(self):
		print("eventid: {}".format(self.eventid))
		print("\tsrc:")
		print("\t\t{}\n\t{}".format(self.src_ip, self.src_port))
		print("\tdst:")
		print("\t\t{}\n\t{}".format(self.dst_ip, self.dst_port))
		print("\ttimestamp:")
		print("\t\t{}".format(self.timestamp))
		print("\tmessage:")
		print("\t\t{}".format(self.message))
		print("\tprotocol:")
		print("\t\t{}".format(self.protocol))
		print("\tsensor:")
		print("\t\t{}\n".format(self.sensor))
