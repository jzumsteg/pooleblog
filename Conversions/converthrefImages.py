#!/usr/bin/env python
import re
import os

def main():
	print("Starting...")

	baseUrl = "/Volumes/User Drive/Development/Jekyll/pooleblog/_posts/"
	mdFiles = os.listdir(baseUrl)
	# mdFiles = ['2022-01-10-christmas-in-st.-louis.md']
	for mdFile in mdFiles:
		if mdFile[-2:] == 'md':
			print(f'Opening {mdFile}')
			f = open(f'{baseUrl}{mdFile}', 'r')
			mdStr = f.read()
			f.close()

			hrefImages = re.findall('<a href.*?</a>', mdStr, re.DOTALL)
			for img in hrefImages:
				print(img)
				# get the image source
				src = re.search('(?<=src=\"http:).*?(?=\")', img, re.DOTALL)
				if src != None:
					imageURL = src.group()
					string1 = '<figure>\n\t<img src="{{site.url}}'
					markdownString = string1 + f"{imageURL}" + (f'"/>\n\t<figcaption></figcaption>\n</figure>\n\n')
					mdStr = mdStr.replace(img, markdownString)

			url = f'{baseUrl}{mdFile}'
			x = open(url, "w")
			x.write(mdStr)
			x.close()
	print('Done...')

if __name__ == "__main__":
	main()


# <figure>
#   <img src="{{site.url}}/assets/images/2021/09/DSC01354.jpg" alt="my alt text"/>
#   <figcaption><em>The front of the Chateau. The symmetry and clean ornamentation mark it as Renaissance.</em></figcaption>
# </figure>