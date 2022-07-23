#!/usr/bin/env python
import re
import os

def main():
	print("Starting...")
	baseUrl = "/Volumes/User Drive/Development/Jekyll/convertedPosts/"
	mdFiles = os.listdir(baseUrl)
	# mdFiles = ['pt one md file here  and un-comment']
	for mdFile in mdFiles[0:]:
		f = open(f'{baseUrl}{mdFile}', 'r')
		mdStr = f.read()
		f.close()
		if 'caption' in mdStr:
			mdStr = processCaptionedImage(mdStr)
		# else:
		# 	mdStr = processImage(mdStr)

		x = open(f'{baseUrl}{mdFile}', "w")
		x.write(mdStr)
		x.close()
	print('Done...')

def processCaptionedImage(st):
	retStr = st
	# first, get strings that are captioned images
	captionedStrs = re.findall('\[caption.*?\[/caption]', st, re.DOTALL)
	if len(captionedStrs) == 0:
		return st

	# there is at least one captioned str
	for capSt in captionedStrs:
		origStr = capSt
		urlStr = re.search('\/assets.*?jpg|jpeg', capSt, re.DOTALL)
		if urlStr != None:
			imageURL = urlStr.group()
			# get the caption
			captionStr = re.search('(?<=</a>).*?(?=\[/caption])', capSt, re.DOTALL)
			if captionStr != None:
				captionOnlyStr = captionStr.group().strip()


		# else:
		# 	print(f'Error: {capStr}')


				# okay have a address string and a caption string
				string1 = '<figure>\n\t<img src="{{site.url}}'
				markdownString = string1 + f"{imageURL}" + (f'"/>\n\t<figcaption><em>{captionOnlyStr}</em></figcaption>\n</figure>\n\n')
				print(f'{markdownString} - {captionOnlyStr}')
				retStr = retStr.replace(origStr, markdownString)

				print(retStr)

		else:
			print('No images in some post')

	return retStr

if __name__ == "__main__":
	main()


# <figure>
#   <img src="{{site.url}}/assets/images/2021/09/DSC01354.jpg" alt="my alt text"/>
#   <figcaption><em>The front of the Chateau. The symmetry and clean ornamentation mark it as Renaissance.</em></figcaption>
# </figure>