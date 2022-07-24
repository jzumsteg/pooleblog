#!/usr/bin/env python
import re
import os
from os.path import exists
import shutil

def main():
	print("Starting...")
	destBaseDir = "/Volumes/User Drive/Development/Jekyll/pooleblog/_posts/"
	files = listFiles(destBaseDir)
	if files != None:
		for f in files:
			print(f)
			if f[-2:] == 'md':
				# get the file
				fyle = open(f, 'r')
				readStr = fyle.read()
				fstr = str(readStr)
				fyle.close()
				# parse images strings
				images = parseImageStrings(fstr)

				for img in images:
					print(img)

					srcFile = f'/Volumes/User Drive/Development/Jekyll/centrarium/{img}'
					destFile = f'/Volumes/User Drive/Development/Jekyll/pooleblog/{img}'

					if exists(srcFile):
						os.makedirs(os.path.dirname(destFile), exist_ok=True)
						shutil.copy(srcFile, destFile)

	print("Done..")


def listFiles(filepath):
	fname = []	
	for root,d_names,f_names in os.walk(filepath):
		for f in f_names:
			fname.append(os.path.join(root, f))

		# print("fname = %s" %fname)
	return fname

def parseImageStrings(s):
	retList = []
	imgStrs = re.findall('/assets/images/.*?.jpg', s, re.DOTALL)
	if len(imgStrs) > 0:
		for st in imgStrs:
			retList.append(st)

	return retList

if __name__ == "__main__":
	main()