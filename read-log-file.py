import json

'''
cowrie-log-analyzer: Read Log File

'''
#As more files will be added, this will be useful
#if __name__ == '__main__':

#Opens the file
fileName = "cowrie.json.2020-03-19"
file = open(fileName, "r")

#Gets the lines from the log file
lines = []
lines = file.readlines()

#Converts each line from string of json to a python dictionary
#then puts each line into a list
json_list = []

for line in lines:
	json_line_dict = json.loads(line)
	json_list.append(json_line_dict)


for json_dict in json_list:
	if json_dict["eventid"] == "cowrie.session.connect":
		print("put data into session-connect structure")

	elif json_dict["eventid"] == "cowrie.session.closed":
		print("put data into session-closed structure")

	elif json_dict["eventid"] == "cowrie.login.success":
		print("put data into login structure")

	elif json_dict["eventid"] == "cowrie.login.failed":
		print("put data into login structure")

	elif json_dict["eventid"] == "cowrie.command.input":
		print("put data into command structure")

	elif json_dict["eventid"] == "cowrie.command.failed":
		print("put data into command structure")

	elif json_dict["eventid"] == "cowrie.client.version":
		print("put data into client-version structure")

	elif json_dict["eventid"] == "cowrie.client.kex":
		print("put data into kex structure")

	else:
		print("MISSING: {}".format(json_dict["eventid"]))









#
