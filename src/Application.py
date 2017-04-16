#!usr/bin/env

# Code by Stephen Palagi 2017
# For personal use only, do not distribute

# imports
import tkinter
from pathlib import Path
from win32com.shell import shell, shellcon
import os
from shutil import copyfile
"""
Application: defines the Application() class
"""

# defines click behavior for the find saves button
def find_saves(stat_text, saves):
	# first update status text
	print("----------------------------")
	stat_text.set("Status: Finding saves...")
	saves_found = 0
	# look for dark souls 1 save
	print("Finding save for Dark Souls 1")
	docs_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	ds1_save = Path(docs_path+"/nbgi/DRAKS0005.sl2")
	if ds1_save.is_file():
		print("Found save for Dark Souls 1")
		saves[0] = ds1_save
		saves_found+=1
	else:
		print("Could not find save for Dark souls 1")
	print("----------------------------")
	# look for dark souls 2 save
	print("Finding save for Dark Souls 2: SOFS")
	appdata_path = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, None, 0)
	ds2_save = Path(appdata_path+"/DarkSoulsII/0110000104becd96/DS2SOFS0000.sl2")
	if ds2_save.is_file():
		print("Found save for Dark Souls 2: SOFS")
		saves[1] = ds2_save
		saves_found+=1
	else:
		print("Could not find save for Dark souls 2: SOFS")
	print("----------------------------")
	# look for dark souls 3 save
	print("Finding save for Dark Souls 3")
	ds3_save = Path(appdata_path+"/DarkSoulsIII/0110000104becd96/DS30000.sl2")
	if ds3_save.is_file():
		print("Found save for Dark Souls 3")
		saves[2] = ds3_save
		saves_found+=1
	else:
		print("Could not find save for Dark Souls 3")
	print("----------------------------")
	stat_text.set("Satus: Finished - found" + " " + str(saves_found) + " " + "saves")

# defines click behavior for the upl_local button
def upl_local(stat_text, saves):
	print("Storing saves locally...")
	stat_text.set("Storing locally Documents\SSBackups")
	docs_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	save_path = docs_path+"/SSBackups"
	# check if directory exists, if yes
	if os.path.exists(save_path):
		print("Saving...")
		if saves[0]:
			copyfile(saves[0], save_path+"/DRAKS0005.sl2")
		if saves[1]:
			copyfile(saves[1], save_path+"/DS2SOFS0000.sl2")
		if saves[2]:
			copyfile(saves[2], save_path+"/DS30000.sl2")
		print("Saves copied")
		print("----------------------------")
	# if no
	else:
		print("Creating save directory...")
		os.makedirs(save_path)
		print("Saving...")
		if saves[0]:
			copyfile(saves[0], save_path+"/DRAKS0005.sl2")
		if saves[1]:
			copyfile(saves[1], save_path+"/DS2SOFS0000.sl2")
		if saves[2]:
			copyfile(saves[2], save_path+"/DS30000.sl2")
		print("Saves copied")
		print("----------------------------")
	stat_text.set("Saves backed up to Documents\SSBackups")

# defines click behavior for the upl_gdrive button
def upl_gdrive():
	print("Uploading saves to google drive...")

# inherits tkinter.Frame class
class Application(tkinter.Frame):

	def __init__(self, master=None):
		# call parent constructor
		tkinter.Frame.__init__(self, master)
		# grid it
		self.grid()
		# add widgets to grid
		self.createWidgets()
		# list for storing save files
		# 0=ds1, 1=ds2, 2=ds3
		self.saves = [None] * 3

	def createWidgets(self):
		# create object for top level window
		# make the rows and cols of top level window stretchable
		top_w = self.winfo_toplevel()
		top_w.minsize(width=500, height=250)
		top_w.rowconfigure(0, weight=1)
		top_w.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		# status text label
		stat_text = tkinter.StringVar()
		self.status = tkinter.Label(self, textvariable=stat_text)
		self.status.grid(row=0, column= 0)
		stat_text.set("Status:")
		
		# find saves button, use lambda: for parameters
		self.find_saves = tkinter.Button(self, text="Locate saves", width=10, command=lambda: find_saves(stat_text, self.saves))
		self.find_saves.grid(row=1, column=0)

		# store locally button
		self.upl_local = tkinter.Button(self, text="Backup locally", width=10, command=lambda: upl_local(stat_text, self.saves))
		self.upl_local.grid(row=2, column=0)

		# upload to google drive button
		self.upl_gdrive = tkinter.Button(self, text="Upload to google drive", width=20, command=upl_gdrive)
		self.upl_gdrive.grid(row=3, column=0)