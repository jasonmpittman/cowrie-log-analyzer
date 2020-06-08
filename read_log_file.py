from events_class import *
'''
cowrie-log-analyzer: Read Log File

'''
#As more files will be added, this will be useful
#if __name__ == '__main__':

#Opens the file
fileName = "cowrie.json.2020-03-19"

E = Events()
E.getDataFromFile(fileName)
print(E.topTen("src_ip"))










#
