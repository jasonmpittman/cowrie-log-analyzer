from events_class import *

from ui_elements import *

fileName = "cowrie.json.2020-03-19"

E = Events()
E.getDataFromFile(fileName)
print(E.topTen("src_ip"))
