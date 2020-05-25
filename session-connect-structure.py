
class session_connect_structure:
	def __init__(self, json):
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
		print("src:")
		print("\t{}\n\t{}".format(self.src_ip, self.src_port))
