import json

from session_connect_structure import *

from session_closed_structure import *

from login_structure import *

from command_structure import *

from file_download_structure import *

from file_upload_structure import *

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
		obj = session_connect_structure(json_dict)
		obj.printS()

	elif json_dict["eventid"] == "cowrie.session.closed":
		obj = session_closed_structure(json_dict)
		obj.printS()

	elif json_dict["eventid"] == "cowrie.login.success" or json_dict["eventid"] == "cowrie.login.failed":
		obj = login_structure(json_dict)
		obj.printS()

	elif json_dict["eventid"] == "cowrie.command.input" or json_dict["eventid"] == "cowrie.command.failed":
		obj = command_structure(json_dict)
		obj.printS()

	elif json_dict["eventid"] == "cowrie.client.version":
		print("put data into client-version structure")

	elif json_dict["eventid"] == "cowrie.client.kex":
		print("put data into kex structure")

	elif json_dict["eventid"] == "cowrie.log.closed":
		print("put data into log-closed structure")

	elif json_dict["eventid"] == "cowrie.session.params":
		print("put data into session-params structure")

	elif json_dict["eventid"] == "cowrie.session.file_upload":
		obj = file_upload_structure(json_dict)
		obj.printS()

	elif json_dict["eventid"] == "cowrie.session.file_download":
		obj = file_download_structure(json_dict)
		obj.printS()

	else:
		print("MISSING: {}".format(json_dict["eventid"]))









#
