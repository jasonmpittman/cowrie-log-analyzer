class event_class:
	def __init__(self, json):
		self.eventid = json["eventid"]
		self.src_ip = json["src_ip"]
		self.timestamp = json["timestamp"]
		self.message = json["message"]
		self.session = json["session"]
		self.sensor = json["sensor"]

	def printEvent(self):
		print("eventid:", self.eventid)
		print("src_ip:", self.src_ip)
		print("timestamp:", self.timestamp)
		print("message:", self.message)
		print("session:", self.session)
		print("sensor:", self.sensor, "\n")


#eventid
#src_ip
#timestamp
#message
#session
#sensor
