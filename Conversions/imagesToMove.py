#!/usr/bin/env python
import os
from os.path import exists
import re
import shutil

def main():
	print("Starting...")
	xmlPath = "/Volumes/User Drive/Development/Jekyll/chirpy_blog/Conversions/wp_posts_export.xml"
	# xmlPath = "/Volumes/User Drive/Development/Jekyll/chirpy_blog/wp_images/wordpress.xml"
	xmlFile = open(xmlPath,"r")
	xml = xmlFile.read()

	outfile = open('/Volumes/User Drive/Development/Jekyll/chirpy_blog/Conversions/filesToMove.txt', "w")
	sourceBaseDir = "/Volumes/User Drive/Development/Jekyll/chirpy_blog/wp_images/"
	destBaseDir = "/Volumes/User Drive/Development/Jekyll/chirpy_blog/assets/images/"
	# createDirectories(destBaseDir)

	imgCount = 0


	items = re.findall("<item>.*?</item>", xml, re.DOTALL)
	for item in items:
		content = getElement(item, "content:encoded")
		imagesToMove = getImages(item)
		if len(imagesToMove) > 0:
			for image in imagesToMove:
				sourcePath = f'{sourceBaseDir}{image}'
				destFileName  = image[8:]
				destPath = f'{destBaseDir}{destFileName}'

				print(f'Moving from {sourcePath} to {destPath}')

				if exists(sourcePath):
					imgCount += 1
					shutil.copyfile(sourcePath, destPath)

	
	print(f"Done... found {imgCount} images to move")

def getElement(s, element):
	reStr = f'(?<=<{element}>).*?(?=</{element}>)'
	match = re.search(reStr, s, re.DOTALL)
	if match != None:
		returnStr = match.group(0)
	else:
		returnStr = ''
	return returnStr

def createDirectories(baseDir):
	for year in range(2013, 2025):
		newDir = f'{year}'
		yearPath = os.path.join(baseDir, newDir)
		os.mkdir(yearPath)

		for mon in range(1,13):
			monPath = os.path.join(yearPath, f"{mon:02d}")
			os.mkdir(monPath)


def getImages(s):
	regStr = '(?<=uploads/).*?.jpg|.jpeg|.JPG|.JPEG'
	imagePaths = re.findall(regStr, s, re.DOTALL)
	# for imagePath in imagePaths:
	# 	imagePath = f'/Volumes/User Drive/Development/Jekyll/chirpy_blog/wp_images/{imagePath}'
	return imagePaths
	

if __name__ == "__main__":
	main()