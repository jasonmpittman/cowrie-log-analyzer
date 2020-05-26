class file_download_structure:
	def __init__(self, json):
		self.eventid = json["eventid"]
		self.shasum = json["shasum"]
		self.url = json["url"]
		self.timestamp = json["timestamp"]
		self.destfile = json["destfile"]
		self.src_ip = json["src_ip"]
		self.outfile = json["outfile"]
		self.session = json["session"]
		self.message = json["message"]
		self.sensor = json["sensor"]

	def printS(self):
		print("eventid: {}".format(self.eventid))
		print("\tshasum:")
		print("\t\t{}".format(self.shasum))
		print("\turl:")
		print("\t\t{}".format(self.url))
		print("\ttimepstamp:")
		print("\t\t{}".format(self.timestamp))
		print("\tdestfile:")
		print("\t\t{}".format(self.destfile))
		print("\tsrc:")
		print("\t\t{}".format(self.src_ip))
		print("\toutfile:")
		print("\t\t{}".format(self.outfile))
		print("\tsession:")
		print("\t\t{}".format(self.session))
		print("\tmessage:")
		print("\t\t{}".format(self.message))
		print("\tsensor:")
		print("\t\t{}\n".format(self.sensor))
