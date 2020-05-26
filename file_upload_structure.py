class file_upload_structure:
	def __init__(self, json):
		self.eventid = json["eventid"]
		self.shasum = json["shasum"]
		self.timestamp = json["timestamp"]
		self.message = json["message"]
		self.filename = json["filename"]
		self.src_ip = json["src_ip"]
		self.outfile = json["outfile"]
		self.session = json["session"]
		self.sensor = json["sensor"]

	def printS(self):
		print("eventid: {}".format(self.eventid))
		print("\tshasum:")
		print("\t\t{}".format(self.shasum))
		print("\ttimepstamp:")
		print("\t\t{}".format(self.timestamp))
		print("\tmessage:")
		print("\t\t{}".format(self.message))
		print("\tfilename:")
		print("\t\t{}".format(self.filename))
		print("\tsrc:")
		print("\t\t{}".format(self.src_ip))
		print("\toutfile:")
		print("\t\t{}".format(self.outfile))
		print("\tsession:")
		print("\t\t{}".format(self.session))
		print("\tsensor:")
		print("\t\t{}\n".format(self.sensor))
