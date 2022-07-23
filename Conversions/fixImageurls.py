#!/usr/bin/env python
import re
import os

def main():
	print("Starting...")

	baseUrl = "/Volumes/User Drive/Development/Jekyll/pooleblog/_posts/"
	mdFiles = os.listdir(baseUrl)
	# mdFiles = ['2021-10-19-chateau-fontainebleu---inside.md']
	for mdFile in mdFiles:
		if mdFile[-2:] == 'md':
			print(f'Processing {mdFile}')
			f = open(f'{baseUrl}{mdFile}', 'r')
			mdStr = f.read()
			f.close()

			imageStrings = re.findall('(?<=<img src=).*?>', mdStr, re.DOTALL)
			for imgstr in imageStrings:
				# parse the url out
				urlGrp = re.search('/assets/images.*?(?=/>)', imgstr, re.DOTALL)
				if urlGrp != None:
					assetStr = urlGrp.group()

					brackets = "{{"
					newStr = f'<img src= "{brackets} "{assetStr} | prepend: site.baseurl | prepend: site.url}}" alt="Image" />'
					print(newStr)
					
					mdStr = mdStr.replace(imgstr, newStr)

		f = open(f'{baseUrl}{mdFile}', 'w')
		f.write(mdStr)
		f.close()

if __name__ == "__main__":
	main()


	# <img src="{{site.url}}/assets/images/2016/07/160519-josephine-baker-01.jpg"/>
	# <img src="{{ "/assets/images/2022/01/image-3.jpg" | prepend: site.baseurl | prepend: site.url}}" alt="Fambly" />