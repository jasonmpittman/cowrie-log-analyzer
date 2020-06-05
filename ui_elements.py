import tkinter as tk

from PIL import ImageTk, Image

import sys

from matplotlib import pyplot as plt

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
		self.scrollText.pack(side="left", padx=5, pady=10)

	def Grid(self, r, c, px=10, py=10):
		self.scrollFrame.grid(row=r, column=c, padx=px, pady=py)

	def Pack(self, Side, px=10, py=10):
		self.scrollFrame.pack(side=Side, padx=px, pady=py)

	def Append(self, text):
		self.scrollText.insert(tk.END, text + "\n")
