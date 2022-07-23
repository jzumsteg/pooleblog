#!/usr/bin/env python
import xml.etree.ElementTree as ET
import re

def main():
	print("Starting...")

	posts = parseXML()

	print("done...")
	pass

def parseXML():
	# read the xmlfile
	xmlPath = "/Volumes/User Drive/Development/Jekyll/chirpy_blog/Conversions/wp_posts_export.xml"
	# xmlPath = "/Volumes/User Drive/Development/Jekyll/jekyll-theme-chirpy-master/Conversions/wordpress.xml"
	xmlFile = open(xmlPath,"r")
	xml = xmlFile.read()

	items = re.findall("<item>.*?</item>", xml, re.DOTALL)
	if items != None:
		for item in items:
			titles = re.findall('<title>.*?</title>', item, re.DOTALL)
			titleStr = extractCDATA(titles[0])
			if '.jpg' in titleStr:
				print(f'image, titleStr: {titleStr}')
				processImage(item)
			else:
				print(f'{titleStr} is something else')
				processPost(item, titleStr)


def extractCDATA(s):
	return s.replace('<![CDATA[','').replace(']]>','')

def processImage(s):
	print('Processing image item')


def processPost(s, titleStr):
	print(f'Processing an item titled {titleStr}')
	postTitle = extractCDATA(titleStr)
	postTitle = postTitle.replace('<title>','').replace('</title>','')

	postDate = getElement(s, "wp:post_date")
	postDate = extractCDATA(postDate)[0:10]
	noSpaceTitleStr = postTitle.replace(' ','-')
	noSpaceTitleStr = cleanup(noSpaceTitleStr)
	fileName = f'/Volumes/User Drive/Development/Jekyll/convertedPosts/{postDate}-{noSpaceTitleStr.lower()}.md'

	#extract and write the post in markdown format
	mdFile = open(fileName, 'w')
	mdFile.write('---\n')
	mdFile.write(f'title: {postTitle}' + '\n')
	mdFile.write('author: John Zumsteg\n')

	# get the date
	pubDate = getElement(s, 'pubDate')
	mdFile.write(f'date: {pubDate}\n')
	mdFile.write(f'category: tbd\n')
	mdFile.write('math: true\n')
	mdFile.write('mermaid: true\n')
	mdFile.write('---\n')

	content = getElement(s, 'content:encoded')
	if content != '':
		contentStr = extractCDATA(content)
		contentStr = processImages(contentStr)
		contentStr = cleanup(contentStr)
		contentStr = convertImageLocations(contentStr)
		mdFile.write(f'{contentStr}\n')


	mdFile.close()

# title: Introduction to Our New Blog
# author: John Zumsteg
# date: 2019-08-08 11:33:00 +0800
# categories: [Blogging, Travel]
# tags: [introduction]
# math: true
# mermaid: true

def processImages(st):
	# first, process any images that have a caption
	# get an array of all the images with a caption
	captionImages = re.findall('\[caption.*?\[/caption]', st, re.DOTALL)
	if len(captionImages) > 0:
		for imageStr in captionImages:
			replStr = getMarkdownAddressStr(imageStr)
			imageAddrStr = 
			print(replStr)
				

	return st

def getMarkdownAddressStr(st):
	addrStrs = re.findall("(?<=href=htt[:\").*?.jpeg|.jpg", st, re.DOTALL)
	addrStr = addrStrs[0]


def convertImageLocations(cStr):
	retStr = cStr.replace('/zumsteg.us/wp-content/uploads/', 'assets/images/')
	return retStr


def cleanup(s):
	# make changes in content string
	retStr = s.replace('$','\\\\$')
	retStr = retStr.replace('<em>','').replace('</em>','')
	retStr = retStr.replace('<i>','').replace('</i>', '')
	return retStr

def getElement(s, element):
	reStr = f'(?<=<{element}>).*?(?=</{element}>)'
	match = re.search(reStr, s, re.DOTALL)
	if match != None:
		returnStr = match.group(0)
	else:
		returnStr = ''
	return returnStr

if __name__ == "__main__":
	main()