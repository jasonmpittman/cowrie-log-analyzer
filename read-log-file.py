import json

'''
cowrie-log-analyzer: Read Log File

'''
#As more files will be added, this will be useful
#if __name__ == '__main__':

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

print(json_list)
