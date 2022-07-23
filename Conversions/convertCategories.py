#!/usr/bin/env python
''' 

'''

#imports here
import sys
import re
import sqlite3
import requests

# take all the urllib stuff out if no internet access required
import os
import re
from datetime import datetime

def main():
	print("Running...")
	start = datetime.now()
	startTime = start.strftime("%H:%M:%S")
	print("Start Time =", startTime)

# code here
	baseUrl = "/Volumes/User Drive/Development/Jekyll/convertedPosts/"
	mdFiles = os.listdir(baseUrl)
	# mdFiles = ['pt one md file here  and un-comment']
	for mdFile in mdFiles[0:]:
		f = open(f'{baseUrl}{mdFile}', 'r')
		mdStr = f.read()
		f.close()


		x = open(f'{baseUrl}{mdFile}', "w")
		x.write(mdStr)
		x.close()
	print('Done...')



# close stuff out here and print elapsed time
	end = datetime.now()
	endTime = end.strftime("%H:%M:%S")
	print(f"End Time = {endTime} elapsed: {end - start}" )
	

if __name__ == "__main__":
	main()
