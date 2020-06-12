import tkinter as tk

from PIL import ImageTk, Image

import sys

import matplotlib

matplotlib.use("TkAgg")

from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class standardButton:
	def __init__(self, parent, commandFunction, buttonText):
		self.button = tk.Button(parent, text=buttonText, command=commandFunction, width=10)

	def Grid(self, r, c, px=10, py=10):
		self.button.grid(row=r, column=c, padx=px, pady=py)

	def Pack(self, Side, px=10, py=10):
		self.button.pack(side=Side, padx=px, pady=py)

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

class Graph:
	def __init__(self, parent, widthIn, heightIn, xLabel, yLabel, title="Title"):
		self.data = []
		self.figure = Figure(figsize=(widthIn, heightIn), dpi=100)
		self.graph = self.figure.add_subplot(1, 1, 1, label=title)
		self.canvas = FigureCanvasTkAgg(self.figure, parent)
		self.Widget = self.canvas.get_tk_widget()
		self.title = title
		self.xLabel = xLabel
		self.yLabel = yLabel
		# xlabel=axisLabel[0], ylabel=axisLabel[1]

	def Grid(self, r, c, colSpan=2, px=10, py=10):
		self.Widget.grid(row=r, column=c, columnspan=colSpan, padx=px, pady=py)

	def Pack(self, Side, px=10, py=10):
		self.Widget.pack(side=Side, padx=px, pady=py)

	def Data(self, data): #add labels as well
		if len(data) < 2 or not isinstance(data[0], list):
			print("Needs more than one axis in order to draw the graph")
			return
		self.data = data

	def draw(self):
		self.graph.cla()
		xAxis = self.data.pop(0)
		for axis in self.data:
			self.graph.plot(xAxis)
		self.graph.set_title(self.title)
		self.graph.set_xlabel(self.xLabel)
		self.graph.set_ylabel(self.yLabel)

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

class Import_Popup:
	def __init__(self, E, lus, parent):
		self.file_name = ""
		self.E = E
		self.lambda_update_screen = lus
		self.parent = parent

	def import_popup(self):
		self.import_window = tk.Toplevel(self.parent)
		self.import_window.title("Import")
		self.import_window.bind('<Return>', self.import_cmd)
		self.input_box = Text_Input_Section(self.import_window, "File or directory name: ")
		self.input_box.Pack("top", 20, 30)
		self.cancel = standardButton(self.import_window, self.import_window.destroy, "Cancel")
		self.cancel.Pack("right")
		self.error_message = tk.StringVar()
		self.error_message.set("")
		self.error_label = tk.Label(self.import_window, textvariable=self.error_message)
		self.import_button = standardButton(self.import_window, self.import_cmd, "Import")
		self.import_button.Pack("right")
		self.error_label.pack(side="bottom")

	def import_cmd(self, event=None):
		self.file_name = self.input_box.Get()
		succ = self.E.get_data(self.file_name)
		if succ:
			pass
			self.lambda_update_screen()
			self.import_window.destroy()
		else:
			self.error_message.set("Not a file or directory")



#
