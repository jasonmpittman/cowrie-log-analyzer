import tkinter as tk

from tkinter import ttk

import sys

import matplotlib

import pandas as pd

matplotlib.use("TkAgg")

from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

from events_database import *

import log

ui_logger = log.Logger("ui_elements")
'''
A button class with basic functionality
'''
class StandardButton:
	def __init__(self, parent, command_function, button_text, palette):
		self._button_text = button_text
		self._palette = palette
		self._style = ttk.Style()
		self._style.theme_use('classic')
		self._style.map("Accent.TButton",
	    foreground=[('pressed', '!disabled', self._palette.accent_a), ('active', self._palette.accent_a)],
	    background=[('pressed', '!disabled', self._palette.accent_b), ('active', self._palette.accent_b)],
		relief=[('pressed', 'flat'), ('!pressed', 'flat')]
		)
		self._style.configure("Accent.TButton", background=self._palette.accent_a, foreground=self._palette.accent_b, relief="flat", borderwidth=0, font=('Helvetica', 14, 'bold'))
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._button_text}: Visual Design Configured")
		self._button = ttk.Button(parent, text=self._button_text, command=command_function, width=10, style="Accent.TButton")
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._button_text}: Button initialized")
	def grid(self, r, c, px=10, py=10):
		self._button.grid(row=r, column=c, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"{self._button_text}: Button placed")

	def pack(self, Side, px=10, py=10):
		self._button.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"{self._button_text}: Button placed")

'''
These are the boxes that display the top 10 information
	- Init --> creates the box
	- Pack and grid --> for placement
	- Append --> add text to the box (at the end)
	- Clear --> remove text from the box
	- export_md --> returns a string with the data from the box
'''
class InfoBox:
	def __init__(self, parent, h, w, title, palette, px=10, py=10):
		self._palette = palette
		self._title_text = title
		self._info_frame = tk.Frame(parent, bg=self._palette.secondary_b, bd=5, relief="groove", width=w, height=h)
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._title_text}: Information Frame created")
		self._title = tk.Label(self._info_frame, text=title, bg=self._palette.secondary_b, fg=self._palette.secondary_a, font=('Helvetica', 16, 'bold'))
		self._title.pack(side="top", padx=10, pady=2)
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._title_text}: Title created and drawn")
		self._box_text = tk.Text(self._info_frame, height=h, width=w, bg=self._palette.secondary_b, fg=self._palette.secondary_a, highlightbackground=self._palette.secondary_b, font=('Helvetica', 14,))
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._title_text}: Textbox created")
		self._box_text.configure(state="disabled")
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._title_text}: Textbox configured")
		self._box_text.pack(side="left", padx=5, pady=10)
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._title_text}: Textbox placed")

	def grid(self, r, c, px=10, py=10):
		self._info_frame.grid(row=r, column=c, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"{self._title_text}: InfoBox placed")

	def pack(self, Side, px=10, py=10):
		self._info_frame.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"{self._title_text}: InfoBox placed")

	def append(self, text):
		self._box_text.configure(state="normal")
		self._box_text.insert(tk.END, text)
		self._box_text.configure(state="disabled")
		ui_logger.info(self.__class__.__name__, self.append.__name__, f"{self._title_text}: text has been appended")

	def clear(self):
		self._box_text.configure(state="normal")
		self._box_text.delete("1.0", tk.END)
		self._box_text.configure(state="disabled")
		ui_logger.info(self.__class__.__name__, self.clear.__name__, f"{self._title_text} has been cleared")

	def export_md(self):
		string = "## " + self._title_text + "\n"
		string += self._box_text.get("1.0", tk.END)
		ui_logger.info(self.__class__.__name__, self.export_md.__name__, f"{self._title_text} has been exported")
		return string

'''
This allows for the creation and drawing of graphs (bar and histograms)
	- init --> initializes variables
	- grid and Pack --> allow for placement
	- draw --> actually draws the graph with labels
	- draw_histogram --> draws a histogram with the data instead of a bar graph
	- pd_data --> loads the data from the database
	- graph_export --> saves the graph as a .png
'''
class Graph:
	def __init__(self, parent, widthIn, heightIn, xLabel, yLabel, title="Title"):
		self._data = []
		self._figure = Figure(figsize=(widthIn, heightIn), dpi=100)
		self._figure.tight_layout()
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"figure created and layout set")
		self._canvas = FigureCanvasTkAgg(self._figure, parent)
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"canvas created")
		self._graph = self._figure.add_subplot(1, 1, 1, label=title)
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"subplot created (the actual graph)")

		self._widget = self._canvas.get_tk_widget()
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"tk graph widget created")

		self._title = title
		self._xLabel = xLabel
		self._yLabel = yLabel
		matplotlib.rc('xtick', labelsize=10)

	def grid(self, r, c, colSpan=2, px=10, py=10):
		self._widget.grid(row=r, column=c, columnspan=colSpan, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"graph placed")


	def pack(self, Side, px=10, py=10):
		self._widget.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"graph placed")

	def draw(self):
		self._graph.cla()
		self._graph.set_xticklabels(self._data[0], rotation=70)
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"label format set")
		self._graph.bar(self._data[0], self._data[1])
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"bar graph is drawn")
		self._figure.set_tight_layout(tight=True)
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"set figure layout")
		self._graph.set_title(self._title)
		self._graph.set_xlabel(self._xLabel)
		self._graph.set_ylabel(self._yLabel)
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"graph title, x-labels, and y-labels are drawn onto the graph")

	def draw_histogram(self):
		self._graph.cla()
		# self._graph.set_xticklabels(rotation=70)
		self._graph.hist(self._data[0], bins=5)
		ui_logger.info(self.__class__.__name__, self.draw_histogram.__name__, f"histogram drawn")
		self._figure.set_tight_layout(tight=True)
		ui_logger.info(self.__class__.__name__, self.draw_histogram.__name__, f"figure's layout is set")
		self._graph.set_title(self._title)
		self._graph.set_xlabel(self._xLabel)
		self._graph.set_ylabel(self._yLabel)
		ui_logger.info(self.__class__.__name__, self.draw_histogram.__name__, f"histogram title, x-labels, and y-labels are drawn onto the histogram")


	def pd_data(self, col):
		conn = create_connection()
		sql = f"""SELECT {col},COUNT({col}) AS cnt FROM events
				WHERE {col} NOT IN ('-')
				GROUP BY {col}
				ORDER BY cnt DESC;"""
		self._data = pd.read_sql(sql, conn).head(10)
		ui_logger.info(self.__class__.__name__, self.pd_data.__name__, f"{col}: data fetched")
		x_list = self._data.iloc[:,0].tolist()
		y_list = self._data.cnt.tolist()
		self._data = [x_list, y_list]
		ui_logger.info(self.__class__.__name__, self.pd_data.__name__, f"{col}: data set")

	def graph_export(self, filename):
		extention = filename[-4::]
		if extention != ".png":
			filename = filename + ".png"
			ui_logger.info(self.__class__.__name__, self.graph_export.__name__, ".png extention added to file name")
		self._figure.savefig(filename)
		ui_logger.info(self.__class__.__name__, self.graph_export.__name__, f"Graph exported as {filename}")
		return True

'''
This is used to allow the user to input things into the program
	- init --> initializes the pop-up box and places everything in it
	- Pack and grid --> for placement
	- Get --> returns the text that was typed into the textbox
'''
class TextInputSection:
	def __init__(self, parent, label_text, palette):
		self._label_text = label_text
		self._palette = palette
		self._frame = tk.Frame(parent)
		self._frame.configure(bg=self._palette.secondary_b)
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{label_text}: Text input frame created and configured")
		self._label = tk.Label(self._frame, text=label_text, bg=self._palette.secondary_b, fg=self._palette.primary)
		self._label.pack(side="left")
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{label_text}: Text input label created and configured")
		self._text = tk.Entry(self._frame, bd=2, bg=self._palette.accent_a, fg=self._palette.primary)
		self._text.focus_set()
		self._text.pack(side="left", padx=5)
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{label_text}: Text entry created, focus set, and placed")

	def pack(self, Side, px=0, py=0):
		self._frame.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"{self._label_text}: placed")

	def grid(self, r, c, px=0, py=0):
		self._frame.grid(row=r, column=c, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"{self._label_text}: placed")

	def get(self):
		ui_logger.info(self.__class__.__name__, self.get.__name__, f"{self._label_text}: text returned")
		return self._text.get()

'''
A class that handles all of the pop-up boxes and deals with all of that functionality (in partuclare the popups where the user types information in)
	- init --> initializes variables
	- pop_up_box --> creates the pop-up box
	- btn_cmd --> when the button is pressed this is what runs
'''
class PopUp:
	def __init__(self, cmd, update, parent, title, action_name, error_message, label_text, palette):
		self._palette = palette
		self._cmd = cmd
		self._update = update
		self._parent = parent
		self._title = title
		self._action_name = action_name
		self._error_message = tk.StringVar()

		self._error_message_on_screen = error_message
		self._label_text = label_text
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"{self._title} - initial variables setup")

	def pop_up_box(self):
		self._error_message.set("")
		self.window = tk.Toplevel(self._parent)
		ui_logger.info(self.__class__.__name__, self.pop_up_box.__name__, f"{self._title} - window popped up")
		self.window.configure(bg=self._palette.secondary_b)
		self.window.resizable(False, False)
		self.window.title(self._title)
		self.window.bind('<Return>', self.btn_cmd)
		ui_logger.info(self.__class__.__name__, self.pop_up_box.__name__, f"{self._title} - window configured")
		self.input_box = TextInputSection(self.window, self._label_text, self._palette)
		self.input_box.pack("top", 20, 30)
		ui_logger.info(self.__class__.__name__, self.pop_up_box.__name__, f"{self._title} - imput box created and placed")
		self.cancel = StandardButton(self.window, self.window.destroy, "Cancel", self._palette)
		self.cancel.pack("right")
		self.error_label = tk.Label(self.window, textvariable=self._error_message, bg=self._palette.secondary_b)
		self.button = StandardButton(self.window, self.btn_cmd, self._action_name, self._palette)
		self.button.pack("right")
		ui_logger.info(self.__class__.__name__, self.pop_up_box.__name__, f"{self._title} - cancel and action button created and placed")
		self.error_label.pack(side="bottom")
		ui_logger.info(self.__class__.__name__, self.pop_up_box.__name__, f"{self._title} - error label placed")


	def btn_cmd(self, event=None):
		ui_logger.info(self.__class__.__name__, self.pop_up_box.__name__, f"{self._title}: Button command running")
		input_text = self.input_box.get()
		succ = self._cmd(input_text)
		if succ:
			self._update()
			self.window.destroy()
			ui_logger.info(self.__class__.__name__, self.pop_up_box.__name__, f"{self._title}: bnt_cmd was successful")
		else:
			ui_logger.warning(self.__class__.__name__, self.pop_up_box.__name__, f"Failed: UI served warning --> {self._error_message_on_screen}")
			self._error_message.set(self._error_message_on_screen)

'''
The selection menu for the graphs
	- init --> keeps track of the parent
	- Pack and grid --> for placement
	- graph_it --> determines what graph to draw and then calls the needed functions to do so
	- pop --> this is the pop-up menu with the options
'''
class SelectionMenu:
	def __init__(self, parent, palette):
		self._parent = parent
		self._palette = palette
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"Initialized")

	def pack(self, side="top"):
		self.menu.pack(side=side, padx=0, pady=0)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"Placed")

	def grid(self, r, c):
		self.menu.grid(row=r, column=c, padx=0, pady=0)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"Placed")

	def graph_it(self):
		#duration is going to change
		self.dict = {"IP Address": {"category": "ip_address", "x_label": "IP Addresses", "y_label": "Frequency", "title": "IP Address Graph"},
					"Countries": {"category": "country", "x_label": "Country", "y_label": "Frequency", "title": "Country Graph"},
					"Session Duration": {"category": "duration", "x_label": "Time(s)", "y_label": "Longest Durations", "title": "Time Duration Graph"}}
		graph_type = self.string_var.get()
		ui_logger.info(self.__class__.__name__, self.graph_it.__name__, f"{graph_type} selected")
		print(graph_type)
		graph_window(self._parent, self.dict[graph_type]["category"], self.dict[graph_type]["x_label"], self.dict[graph_type]["y_label"], self.dict[graph_type]["title"], self._palette)
		ui_logger.info(self.__class__.__name__, self.graph_it.__name__, f"{graph_type} graphed")

	def pop(self):
		self.window = tk.Toplevel(self._parent)
		self.window.configure(bg=self._palette.secondary_b)
		self.window.resizable(False, False)
		ui_logger.info(self.__class__.__name__, self.pop.__name__, f"Selection Menu pop-up configured and displaying")
		self.string_var = tk.StringVar(self.window)
		self.menu = tk.OptionMenu(self.window, self.string_var, "IP Address", "Countries", "Session Duration")
		self.menu.config(width=16, bg=self._palette.secondary_b)
		self.menu.pack(side="top")
		ui_logger.info(self.__class__.__name__, self.pop.__name__, f"Option menu created, configured, and placed")
		self.button_bar = tk.Frame(self.window)
		self.button_bar.configure(bg=self._palette.secondary_b)
		self.button_bar.pack(side="bottom")
		self.button = StandardButton(self.button_bar, self.graph_it, "Graph it!", self._palette)
		self.button.pack("right")
		self.cancel = StandardButton(self.button_bar, self.window.destroy, "Cancel", self._palette)
		self.cancel.pack("right")
		ui_logger.info(self.__class__.__name__, self.pop.__name__, f"Option menu created buttons and button bar created and displayed")

'''
A fuction that does nothing (so it can be passed to a class in the event nothing needs to be done)
'''
def no_update():
	print("")

'''
Everything the graph window needs to be shown is done in here
'''
def graph_window(parent, category, x_label, y_label, title, palette):
	graphW = tk.Toplevel(parent)
	graphW.resizable(False, False)
	graphW.title("Graph")
	ui_logger.info("", graph_window.__name__, f"graph_window created and displayed")

	bar = tk.Frame(graphW)
	bar.pack(side="bottom")

	#self.window.destroy()
	exit_button = StandardButton(bar, graphW.destroy, "Cancel", palette)
	exit_button.pack("right")
	ui_logger.info("", graph_window.__name__, f"buttons and button bar created and placed")

	G = Graph(graphW, 8, 5, x_label, y_label, title)
	G.pd_data(category)
	G.pack("top")
	ui_logger.info("", graph_window.__name__, f"Graph created")
	if category == "duration":
		G.draw_histogram()
	else:
		G.draw()

	graph_export_popup = PopUp(G.graph_export, no_update, graphW, "Export Graph", "Export", "", "Name of PNG file", palette)

	export_graph = StandardButton(bar, graph_export_popup.pop_up_box, "Export", palette)
	export_graph.pack("right")
	ui_logger.info("", graph_window.__name__, f"graph export pop-up displayed and button created")


#
