#!usr/bin/env

# Code by Stephen Palagi 2017
# For personal use only, do not distribute

# imports
from Application import *

"""
Entry: defines entry point
"""

# entry point
if __name__ == "__main__":
	
	# create Application() instance
	app = Application()
	app.master.title("SoulSave")

	app.mainloop()