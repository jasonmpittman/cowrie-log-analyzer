class Events:
	def __init__(self, events):
		self.events = events

	def printEvents(self):
		for event in self.events:
			event.printEvent()

	def print_all_src_ips(self):
		for event in self.events:
			event.print_src_ip()

	def print_all_src_ports(self):
		for event in self.events:
			event.print_src_port()


	def topTen(self, category):
		totals = {}
		for event in self.events:
			res = event.getEventValue(category)
			if res != "":
				if res not in totals:
					totals.update({res : 1})
				else:
					totals[res] += 1

		sortedDictionary = sorted(totals.items(), key = lambda x : x[1], reverse=True)

		i = 0
		strReturn = ""
		while i < 10:
			key, value = sortedDictionary[i]
			if i == 9:
				strReturn += str(i + 1) + ". " + key + "\n"
			else:
				strReturn += str(i + 1) + ".  " + key + "\n"
			i += 1
		return strReturn



#
