#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "tkinter, sys, matplotlib, pandas, events_database, log"

import tkinter as tk

from tkinter import ttk

import sys

import matplotlib

import pandas as pd

matplotlib.use("TkAgg")

from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

from Events import events_database

from Log import log

ui_logger = log.Logger("ui_elements")

class StandardButton:
	"""
	A button class with basic functionality and consistent look.

	Attributes
	----------
	_button_text : str
	_palette : color object
	_style : ttk.Style object
	_button : ttk.Button object
	"""
	def __init__(self, parent, command_function, button_text, palette):
		"""
		Sets up the style, color, and the button.
		Parameters
		----------
		parent : tk container object (tk.Frame)
		command_function : function
		button_text : str
		palette : color object
		"""
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
		"""
		Places the button in the grid style.
		Parameters
		----------
		r : int
		c : int
		px : int
		py : int
		"""
		self._button.grid(row=r, column=c, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"{self._button_text}: Button placed")

	def pack(self, Side, px=10, py=10):
		"""
		Places the button in the pack style.
		Parameters
		----------
		Side : str
		px : int
		py : int
		"""
		self._button.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"{self._button_text}: Button placed")


class InfoBox:
	"""
	These are the boxes that display the top 10 information
		- Init --> creates the box
		- Pack and grid --> for placement
		- Append --> add text to the box (at the end)
		- Clear --> remove text from the box
		- export_md --> returns a string with the data from the box

		Attributes
		----------
		_palette : color object
		_title_text : str
		_info_frame : tk.Frame object
		_box_text : tk.Text
	"""
	def __init__(self, parent, h, w, title, palette, px=10, py=10):
		"""
		Creates the the conponents for the InfoBox.

		Parameters
		----------
		parent : parent container (tk.Frame)
		h : int
		w : int
		title : str
		palette : color object
		px : int
		py : int

		"""
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
		"""
		Places the button in the grid style.
		Parameters
		----------
		r : int
		c : int
		px : int
		py : int
		"""
		self._info_frame.grid(row=r, column=c, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"{self._title_text}: InfoBox placed")

	def pack(self, Side, px=10, py=10):
		"""
		Places the button in the pack style.
		Parameters
		----------
		Side : str
		px : int
		py : int
		"""
		self._info_frame.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"{self._title_text}: InfoBox placed")

	def append(self, text):
		"""
		Adds text to the the end of the InfoBox.

		Parameters
		----------
		text : str
		"""
		self._box_text.configure(state="normal")
		self._box_text.insert(tk.END, text)
		self._box_text.configure(state="disabled")
		ui_logger.info(self.__class__.__name__, self.append.__name__, f"{self._title_text}: text has been appended")

	def clear(self):
		"""
		Empties the text out of the InfoBox.
		"""
		self._box_text.configure(state="normal")
		self._box_text.delete("1.0", tk.END)
		self._box_text.configure(state="disabled")
		ui_logger.info(self.__class__.__name__, self.clear.__name__, f"{self._title_text} has been cleared")

	def export_md(self):
		"""
		Returns a string to be used for text export.
		"""
		string = "## " + self._title_text + "\n"
		string += self._box_text.get("1.0", tk.END)
		ui_logger.info(self.__class__.__name__, self.export_md.__name__, f"{self._title_text} has been exported")
		return string


class Graph:
	"""
	This allows for the creation and drawing of graphs (bar and histograms)
		- init --> initializes variables
		- grid and Pack --> allow for placement
		- draw --> actually draws the graph with labels
		- draw_histogram --> draws a histogram with the data instead of a bar graph
		- pd_data --> loads the data from the database
		- graph_export --> saves the graph as a .png

		Attributes
		----------
		palette : color object
		_graph_background : str (hex color value)
		_graph_bar_color : str (hex color value)
		_graph_label_color : str (hex color value)
		_graph_figure_color : str (hex color value)
		_data : list
		_figure : matplotlib.figure.Figure object
		_canvas : matplotlib.backends.backend_tkagg.FigureCanvasTkAgg object
		_graph : matplotlib.subplot object
		_widget : tk_widget object
		_title : str
		_xLabel : str
		_yLabel : str
	"""
	def __init__(self, parent, widthIn, heightIn, xLabel, yLabel, palette, title="Title"):
		"""
		Creates and configures the graph.

		Parameters
		----------
		parent : tk.Frame object
		widthIn : int
		heightIn : int
		xLabel : str
		yLabel : str
		palette : color object
		title : str
		"""
		self._parent = parent
		self.palette = palette
		self._graph_background = self.palette.secondary_a
		self._graph_bar_color = self.palette.secondary_b
		self._graph_label_color = self.palette.accent_a
		self._graph_figure_color = self.palette.primary
		self._data = []
		self._figure = Figure(figsize=(widthIn, heightIn), dpi=100)
		self._figure.patch.set_facecolor(self._graph_figure_color)
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

		matplotlib.rc('xtick', labelsize=10, color=self._graph_label_color)

	def grid(self, r, c, colSpan=2, px=10, py=10):
		"""
		Places the button in the grid style.
		Parameters
		----------
		r : int
		c : int
		px : int
		py : int
		"""
		self._widget.grid(row=r, column=c, columnspan=colSpan, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"graph placed")


	def pack(self, Side, px=10, py=10):
		"""
		Places the button in the pack style.
		Parameters
		----------
		Side : str
		px : int
		py : int
		"""
		self._widget.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"graph placed")

	def draw(self):
		"""
		Draws and places all of the elements for a bar graph.
		"""
		self._graph.cla()
		self._graph.set_xticklabels(self._data[0], rotation=70)
		# self._graph.set_yticklabels()
		self._graph.tick_params(axis='x', colors=self._graph_label_color)
		self._graph.tick_params(axis='y', colors=self._graph_label_color)
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"label format set")
		self._graph.bar(self._data[0], self._data[1], color=self._graph_bar_color)
		self._graph.set_facecolor(self._graph_background)
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"bar graph is drawn")
		self._figure.set_tight_layout(tight=True)
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"set figure layout")
		self._graph.set_title(self._title, color=self._graph_label_color)
		self._graph.set_xlabel(self._xLabel)
		self._graph.set_ylabel(self._yLabel)
		self._graph.xaxis.label.set_color(self._graph_label_color)
		self._graph.yaxis.label.set_color(self._graph_label_color)
		ui_logger.info(self.__class__.__name__, self.draw.__name__, f"graph title, x-labels, and y-labels are drawn onto the graph")

	def draw_histogram(self):
		"""
		Draws and places all of the elements for a histogram.
		"""
		self._graph.cla()
		# self._graph.set_xticklabels(rotation=70)
		self._graph.tick_params(axis='x', colors=self._graph_label_color)
		self._graph.tick_params(axis='y', colors=self._graph_label_color)

		self._graph.hist(self._data[0], bins=5, color=self._graph_bar_color)
		self._graph.set_facecolor(self._graph_background)
		ui_logger.info(self.__class__.__name__, self.draw_histogram.__name__, f"histogram drawn")
		self._figure.set_tight_layout(tight=True)
		ui_logger.info(self.__class__.__name__, self.draw_histogram.__name__, f"figure's layout is set")
		self._graph.set_title(self._title, color=self._graph_label_color)
		self._graph.set_xlabel(self._xLabel)
		self._graph.set_ylabel(self._yLabel)
		self._graph.xaxis.label.set_color(self._graph_label_color)
		self._graph.yaxis.label.set_color(self._graph_label_color)
		ui_logger.info(self.__class__.__name__, self.draw_histogram.__name__, f"histogram title, x-labels, and y-labels are drawn onto the histogram")


	def pd_data(self, col):
		"""
		Collects the data from database (x and y data) and adds it to the _data list.

		Parameters
		----------
		col : str
		"""
		conn = events_database.create_connection()
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
		"""
		Exports the graph to the given filename (with extention correction)

		Parameters
		----------
		filename : str
		"""
		self.graph_export_alert = alert_window(self._parent, self.palette)
		try:
			extention = filename[-4::]
			if extention != ".png":
				filename = filename + ".png"
				ui_logger.info(self.__class__.__name__, self.graph_export.__name__, ".png extention added to file name")
			self._figure.savefig(filename)
			ui_logger.info(self.__class__.__name__, self.graph_export.__name__, f"Graph exported as {filename}")
			self.graph_export_alert.pop_up(f"Export to {filename} successful")
			return True
		except:
			print("graph failed to export")
			ui_logger.info(self.__class__.__name__, self.graph_export.__name__, f"Graph failed to export as {filename}")
			self.graph_export_alert.pop_up(f"Export to {filename} failed")
			return False


class TextInputSection:
	"""
	This is used to allow the user to input things into the program.
		- init --> initializes the pop-up box and places everything in it
		- Pack and grid --> for placement
		- Get --> returns the text that was typed into the textbox

		Attributes
		----------
		_label_text : str
		_palette : color object
		_frame : tk.Frame object
		_label : tk.Label object
		_text : tk.Entry object
	"""
	def __init__(self, parent, label_text, palette):
		"""
		Creates and places elements into the TextInputSection object.

		Parameters
		----------
		parent : tk.Frame object
		label_text : str
		palette : color object
		"""
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
		"""
		Places the button in the pack style. Places the actual TextInputSection object.
		Parameters
		----------
		Side : str
		px : int
		py : int
		"""
		self._frame.pack(side=Side, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"{self._label_text}: placed")

	def grid(self, r, c, px=0, py=0):
		"""
		Places the button in the grid style. Places the actual TextInputSection object.
		Parameters
		----------
		r : int
		c : int
		px : int
		py : int
		"""
		self._frame.grid(row=r, column=c, padx=px, pady=py)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"{self._label_text}: placed")

	def get(self):
		"""
		Returns what is in the text feild.
		"""
		ui_logger.info(self.__class__.__name__, self.get.__name__, f"{self._label_text}: text returned")
		return self._text.get()


class PopUp:
	"""
	A class that handles all of the pop-up boxes and deals with all of that functionality (in partuclare the popups where the user types information in).
		- init --> initializes variables
		- pop_up_box --> creates the pop-up box
		- btn_cmd --> when the button is pressed this is what runs

	Attributes
	----------
	_palette : color object
	_cmd : function
	_update : function
	_parent : tk.Frame object
	_title : str
	_action_name : str
	_error_message : tk.StringVar object
	_error_message_on_screen : str
	_label_text : str
	"""
	def __init__(self, cmd, update, parent, title, action_name, error_message, label_text, palette):
		"""
		Sets all the variables the object needs.

		Parameters
		----------
		cmd : function
		update : function
		parent : tk.Frame object
		title : str
		action_name : str
		error_message : str
		label_text : str
		palette : color object
		"""
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
		"""
		Pops the box up with all the needed elements based on what was inputted on the creation of the object.
		"""
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
		"""
		Calling of the button command.
		event : event object (required for use of clicking button and pressing enter)
		"""
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


class SelectionMenu:
	"""
	The selection menu for the graphs
		- init --> keeps track of the parent
		- Pack and grid --> for placement
		- graph_it --> determines what graph to draw and then calls the needed functions to do so
		- pop --> this is the pop-up menu with the options

		Attributes
		----------
		_parent : tk.Frame object
		_palette : color object
		window : tk.toplevel object
		string_var : tk.StringVar object
		menu : tk.OptionMenu object
		button_bar : tk.Frame object
		button : StandardButton object
		cancel : StandardButton object


	"""
	def __init__(self, parent, palette):
		"""
		Sets attribute variables.

		Parameters
		----------
		parent : tk.Frame object
		palette : color object
		"""
		self._parent = parent
		self._palette = palette
		ui_logger.info(self.__class__.__name__, self.__init__.__name__, f"Initialized")

	def pack(self, side="top"):
		"""
		Places the button in the pack style.
		Parameters
		----------
		Side : str
		px : int
		py : int
		"""
		self.menu.pack(side=side, padx=0, pady=0)
		ui_logger.info(self.__class__.__name__, self.pack.__name__, f"Placed")

	def grid(self, r, c):
		"""
		Places the button in the grid style.
		Parameters
		----------
		r : int
		c : int
		px : int
		py : int
		"""
		self.menu.grid(row=r, column=c, padx=0, pady=0)
		ui_logger.info(self.__class__.__name__, self.grid.__name__, f"Placed")

	def graph_it(self):
		"""
		Creates graph based on the user selection.
		"""
		self.dict = {"IP Address": {"category": "ip_address", "x_label": "IP Addresses", "y_label": "Frequency", "title": "IP Address Graph"},
					"Countries": {"category": "country", "x_label": "Country", "y_label": "Frequency", "title": "Country Graph"},
					"Session Duration": {"category": "duration", "x_label": "Time(s)", "y_label": "Longest Durations", "title": "Time Duration Graph"}}
		graph_type = self.string_var.get()
		ui_logger.info(self.__class__.__name__, self.graph_it.__name__, f"{graph_type} selected")
		print(graph_type)
		graph_window(self._parent, self.dict[graph_type]["category"], self.dict[graph_type]["x_label"], self.dict[graph_type]["y_label"], self.dict[graph_type]["title"], self._palette)
		ui_logger.info(self.__class__.__name__, self.graph_it.__name__, f"{graph_type} graphed")

	def pop(self):
		"""
		Pops window out with the selection menu on it.
		"""
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

class alert_window:
	"""
	Pops up a window to let the user know information.

	Attributes
	----------
	_parent : tk.Frame object
	_palette : color object
	_window : tk.Toplevel object
	_label : tk.Label object
	_button : StandardButton object
	"""
	def __init__(self, parent, palette):
		"""
		Sets attributes

		Parameters
		----------
		parent : tk.Frame object
		palette : color object
		"""
		self._parent = parent
		self._palette = palette

	def pop_up(self, message):
		"""
		Pops up a box with the provided message in order to give the user information.

		Parameters
		----------
		message : str
		"""
		self._window = tk.Toplevel(self._parent)
		self._window.configure(bg=self._palette.secondary_b)
		self._window.resizable(False, False)
		ui_logger.info(self.__class__.__name__, alert_window.__name__, f"Alert window configured and displaying")
		self._label = tk.Label(self._window, text=message, bg=self._palette.secondary_b, fg=self._palette.secondary_a)
		self._label.pack(side="top")
		self._button = StandardButton(self._window, self._window.destroy, "Ok", self._palette)
		self._button.pack("bottom")


def no_update():
	"""
	A fuction that does nothing (so it can be passed to a class in the event nothing needs to be done)
	"""
	pass


def graph_window(parent, category, x_label, y_label, title, palette):
	"""
	Everything the graph window needs to be shown is done in here

	Parameters
	----------
	parent : tk.Frame object
	category : str
	x_label : str
	y_label : str
	title : str
	palette : color object
	"""
	graphW = tk.Toplevel(parent)
	graphW.resizable(False, False)
	graphW.title("Graph")
	graphW.configure(background=palette.primary)
	ui_logger.info("", graph_window.__name__, f"graph_window created and displayed")

	bar = tk.Frame(graphW)
	bar.configure(background=palette.primary)
	bar.pack(side="bottom")

	#self.window.destroy()
	exit_button = StandardButton(bar, graphW.destroy, "Cancel", palette)
	exit_button.pack("right")
	ui_logger.info("", graph_window.__name__, f"buttons and button bar created and placed")

	G = Graph(graphW, 8, 5, x_label, y_label, palette, title)
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
