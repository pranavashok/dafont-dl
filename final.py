#! /usr/bin/python

# Name: dafont.com Bulk Download Tool
# Summary: A tool for downloading top 20 fonts of each sub-category of dafont.com
# License: BSD
# Author: Pranav Ashok
# Author-email: iam@pranavashok.com
# Author-homepage: http://pranavashok.com/blog
# Support: http://pranavashok.com/blog/2010/05/script-to-download-fonts-in-bulk-from-dafont-com
# Support: Twitter (@pranavashok)

from BeautifulSoup import BeautifulSoup
import re
import os
import commands
import string

for cat in range(101, 119): #ID Range 101-119
	url = 'http://www.dafont.com/theme.php?cat=%d&nb_ppp=20' % cat
	contents = commands.getoutput("curl -s '"+url+"'")

	w = open('downloader.sh', 'a')
	
	soup = BeautifulSoup(contents)
	directory = soup.find('title').contents
	wholeTag = soup.findAll('a', {"class" : "dl"})
	directory[0] = string.rstrip(directory[0], " | dafont.com</title>")
	fontCat, useless, subCat = directory[0].partition(" &gt; ")
	
	w.write('mkdir \"%s\"\n' % fontCat)
	w.write('cd \"%s\"\n' % fontCat)

	w.write('mkdir \"%s\"\n' % subCat)
	w.write('cd \"%s\"\n' % subCat)
	for link in wholeTag:
		name = os.path.basename(link['href'])
		fileName, fileExt = os.path.splitext(name)
		fileName = string.lstrip(fileName, "?f=")
		w.write('wget -c -O \"%s.zip\" \"%s\" \n' % (fileName, link['href']))
	w.write('cd ..\n')
	w.write('cd ..\n')
	w.close()

exit()
