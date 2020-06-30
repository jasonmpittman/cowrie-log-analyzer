import tkinter as tk

from PIL import ImageTk, Image

import sys

import matplotlib

import pandas as pd

matplotlib.use("TkAgg")

from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

from events_database import *

'''
A button class with basic functionality
'''
class standardButton:
	def __init__(self, parent, commandFunction, buttonText):
		self.button = tk.Button(parent, text=buttonText, command=commandFunction, width=10)

	def Grid(self, r, c, px=10, py=10):
		self.button.grid(row=r, column=c, padx=px, pady=py)

	def Pack(self, Side, px=10, py=10):
		self.button.pack(side=Side, padx=px, pady=py)


'''
These are the boxes that display the top 10 information
	- The functions were made to save time
'''
class ScrollSection:
	def __init__(self, parent, h, w, title, px=10, py=10):
		self.scrollFrame = tk.Frame(parent, bg="white", bd=5, relief="groove", width=w, height=h)
		self.title = tk.Label(self.scrollFrame, text=title)
		self.title.pack(side="top", padx=10, pady=2)
		self.scroll = tk.Scrollbar(self.scrollFrame)
		self.scrollText = tk.Text(self.scrollFrame, yscrollcommand=self.scroll.set, height=h, width=w)
		self.scrollText.configure(state="disabled")
		self.scrollText.pack(side="left", padx=5, pady=10)

	def Grid(self, r, c, px=10, py=10):
		self.scrollFrame.grid(row=r, column=c, padx=px, pady=py)

	def Pack(self, Side, px=10, py=10):
		self.scrollFrame.pack(side=Side, padx=px, pady=py)

	def Append(self, text):
		self.scrollText.configure(state="normal")
		self.scrollText.insert(tk.END, text)
		self.scrollText.configure(state="disabled")

	def Clear(self):
		self.scrollText.configure(state="normal")
		self.scrollText.delete("1.0", tk.END)
		self.scrollText.configure(state="disabled")

	def export_md(self):
		string = "## " + self.title["text"] + "\n"
		string += self.scrollText.get("1.0", tk.END)
		return string

'''
This allows for the creation and drawing of graphs (bar and histograms)
'''
class Graph:
	def __init__(self, parent, widthIn, heightIn, xLabel, yLabel, title="Title"):
		self.data = []
		self.figure = Figure(figsize=(widthIn, heightIn), dpi=100)
		self.figure.tight_layout()
		self.canvas = FigureCanvasTkAgg(self.figure, parent)
		self.graph = self.figure.add_subplot(1, 1, 1, label=title)
		self.Widget = self.canvas.get_tk_widget()
		self.title = title
		self.xLabel = xLabel
		self.yLabel = yLabel
		matplotlib.rc('xtick', labelsize=10)

	def Grid(self, r, c, colSpan=2, px=10, py=10):
		self.Widget.grid(row=r, column=c, columnspan=colSpan, padx=px, pady=py)

	def Pack(self, Side, px=10, py=10):
		self.Widget.pack(side=Side, padx=px, pady=py)

	def draw(self):
		self.graph.cla()
		self.graph.set_xticklabels(self.data[0], rotation=70)
		self.graph.bar(self.data[0], self.data[1])
		self.figure.set_tight_layout(tight=True)
		self.graph.set_title(self.title)
		self.graph.set_xlabel(self.xLabel)
		self.graph.set_ylabel(self.yLabel)

	def draw_histogram(self):
		self.graph.cla()
		# self.graph.set_xticklabels(rotation=70)
		self.graph.hist(self.data[0], bins=5)
		self.figure.set_tight_layout(tight=True)
		self.graph.set_title(self.title)
		self.graph.set_xlabel(self.xLabel)
		self.graph.set_ylabel(self.yLabel)


	def pd_data(self, col):
		conn = create_connection()
		sql = f"""SELECT {col},COUNT({col}) AS cnt FROM events
				WHERE {col} NOT IN ('-')
				GROUP BY {col}
				ORDER BY cnt DESC;"""
		self.data = pd.read_sql(sql, conn).head(10)
		x_list = self.data.iloc[:,0].tolist()
		y_list = self.data.cnt.tolist()
		self.data = [x_list, y_list]

	def graph_export(self, filename):
		self.figure.savefig(filename)
		return True

'''
This is used to allow the user to input things into the program
'''
class Text_Input_Section:
	def __init__(self, parent, label_text):
		self.frame = tk.Frame(parent)
		self.label = tk.Label(self.frame, text=label_text)
		self.label.pack(side="left")
		self.text = tk.Entry(self.frame, bd=2)
		self.text.focus_set()
		self.text.pack(side="left", padx=5)

	def Pack(self, Side, px=0, py=0):
		self.frame.pack(side=Side, padx=px, pady=py)

	def Grid(self, r, c, px=0, py=0):
		self.frame.grid(row=r, column=c, padx=px, pady=py)

	def Get(self):
		return self.text.get()

'''
A class that handles all of the pop-up boxes and deals with all of that functionality (in partuclare the popups where the user types information in)
'''
class PopUp:
	def __init__(self, cmd, update, parent, title, action_name, error_message, label_text):
		self.cmd = cmd
		self.update = update
		self.parent = parent
		self.title = title
		self.action_name = action_name
		self.error_message = error_message
		self.input_text = ""
		self.label_text = label_text

	def pop_up(self):
		self.window = tk.Toplevel(self.parent)
		self.window.title(self.title)
		self.window.bind('<Return>', self.btn_cmd)
		self.input_box = Text_Input_Section(self.window, self.label_text)
		self.input_box.Pack("top", 20, 30)
		self.cancel = standardButton(self.window, self.window.destroy, "Cancel")
		self.cancel.Pack("right")
		self.error_message = tk.StringVar()
		self.error_message.set("")
		self.error_label = tk.Label(self.window, textvariable=self.error_message)
		self.button = standardButton(self.window, self.btn_cmd, self.action_name)
		self.button.Pack("right")
		self.error_label.pack(side="bottom")


	def btn_cmd(self, event=None):
		self.input_text = self.input_box.Get()
		succ = self.cmd(self.input_text)
		if succ:
			self.update()
			self.window.destroy()
		else:
			self.error_message.set(self.error_message)

'''
The selection menu for the graphs
'''
class Selection_menu:
	def __init__(self, parent):
		self.parent = parent

	def Pack(self, side="top"):
		self.menu.pack(side=side, padx=0, pady=0)

	def Grid(self, r, c):
		self.menu.grid(row=r, column=c, padx=0, pady=0)

	def Graph_It(self):
		#duration is going to change
		self.dict = {"IP Address": {"category": "ip_address", "x_label": "IP Addresses", "y_label": "Frequency", "title": "IP Address Graph"},
					"Countries": {"category": "country", "x_label": "Country", "y_label": "Frequency", "title": "Country Graph"},
					"Session Duration": {"category": "duration", "x_label": "Time(s)", "y_label": "Longest Durations", "title": "Time Duration Graph"}}
		graph_type = self.string_var.get()
		print(graph_type)
		graphWindow(self.parent, self.dict[graph_type]["category"], self.dict[graph_type]["x_label"], self.dict[graph_type]["y_label"], self.dict[graph_type]["title"])

	def Pop(self):
		self.window = tk.Toplevel(self.parent)
		self.string_var = tk.StringVar(self.window)
		self.menu = tk.OptionMenu(self.window, self.string_var, "IP Address", "Countries", "Session Duration")
		self.menu.config(width=16)
		self.menu.pack(side="top")
		self.button_bar = tk.Frame(self.window)
		self.button_bar.pack(side="bottom")

		self.button = standardButton(self.button_bar, self.Graph_It, "Graph it!")
		self.button.Pack("right")
		self.cancel = standardButton(self.button_bar, self.window.destroy, "Cancel")
		self.cancel.Pack("right")

'''
A fuction that does nothing (so it can be passed to a class in the event nothing needs to be done)
'''
def no_update():
	print("")

'''
Everything the graph window needs to be shown is done in here
'''
def graphWindow(parent, category, x_label, y_label, title):
	graphW = tk.Toplevel(parent)

	graphW.title("Graph")
	bar = tk.Frame(graphW)
	bar.pack(side="bottom")

	#self.window.destroy()
	Exit_button = standardButton(bar, graphW.destroy, "Exit")
	Exit_button.Pack("right")


	G = Graph(graphW, 8, 5, x_label, y_label, title)
	G.pd_data(category)
	G.Pack("top")
	if category == "duration":
		G.draw_histogram()
	else:
		G.draw()

	graph_export_popup = PopUp(G.graph_export, no_update, graphW, "Export Graph", "Export", "", "Name of PNG file")

	Export_graph = standardButton(bar, graph_export_popup.pop_up, "Export")
	Export_graph.Pack("right")


#
