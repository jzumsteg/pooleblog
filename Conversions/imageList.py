#!/usr/bin/env python
''' 

'''

#imports here
import sys
import re
import sqlite3
import requests

# take all the urllib stuff out if no internet access required
import re
import os
from datetime import datetime

def main():
	print("Running...")
	start = datetime.now()
	startTime = start.strftime("%H:%M:%S")
	print("Start Time =", startTime)

	outFile = open('/Volumes/User Drive/Development/Jekyll/chirpy_blog/Conversions/imglist.txt', "w")
	
# code here
	images = []
	xmlPath = "/Volumes/User Drive/Development/Jekyll/chirpy_blog/Conversions/wordpress.xml"
	xmlFile = open(xmlPath,"r")
	xml = xmlFile.read()

	allImages = re.findall('(?<=<guid isPermaLink=\"false\">http://).*?(?=</guid>)', xml, re.DOTALL)
	for img in allImages:
		if "wp-content" in img:
			outFile.write(img + '\n')

	print(len(images))

# close stuff out here and print elapsed time
	outFile.close()
	end = datetime.now()
	endTime = end.strftime("%H:%M:%S")
	print(f"End Time = {endTime} elapsed: {end - start}" )
	

if __name__ == "__main__":
	main()
