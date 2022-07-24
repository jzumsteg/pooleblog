#!/usr/bin/env python
import os
from os.path import exists
import re
import shutil

def main():
	destBaseDir = "/Volumes/User Drive/Development/Jekyll/pooleblog/assets/images/"
	files = listFiles(destBaseDir)
	if files != None:
		# print(f'files: {files}\n')
		for f in files:
			print(f)
			if deleteIt(f) == True :
				os.remove(f)



def listFiles(filepath):
	fname = []	
	for root,d_names,f_names in os.walk(filepath):
		for f in f_names:
			fname.append(os.path.join(root, f))

		# print("fname = %s" %fname)
	return fname

def deleteIt(fname):
	if 'x' in fname:
		return True
	else:
		return False

if __name__ == "__main__":
	main()