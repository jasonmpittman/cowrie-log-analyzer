from events_class import *
'''
cowrie-log-analyzer: Read Log File

'''

#Opens the file
fileName = "cowrie.json.2020-03-19"

E = Events()
E.getDataFromFile(fileName)
print(E.topTen("src_ip"))










#
