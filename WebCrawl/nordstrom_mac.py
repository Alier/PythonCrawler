import urllib
import time
import os
import re
import webbrowser

Page1="http://shop.nordstrom.com/c/sale-designer-handbags-accessories?page=1"
Page2="http://shop.nordstrom.com/c/sale-designer-handbags-accessories?page=2"

UriList = [Page1,Page2]

def getItemList():
	itemdict = {}
	IDregex = '<div id="fashion_([0-9]*)" data-style-number'
	for uri in UriList:
		source = urllib.urlopen(uri).read()
		idList = re.findall(IDregex,source)
		for id in idList:
			LinkRegex = '<a href="/s/(.*)'+id+'.* class=\"title\">'
			link = re.search(LinkRegex,source).group(1)
			fulllink = "http://shop.nordstrom.com/s/"+link+id+"?origin=category"
			itemdict[id]=fulllink
	return itemdict

def crawlBrand():
	ids = getItemList().keys()
	cntr = 0
	flg = True
	while True:
    		if flg:
      			time.sleep(10)  #refresh every 5 seconds
    		try:
      			new_items = getItemList()
      			new_ids = new_items.keys()
			add_ids = [i for i in new_ids if not i in ids ]
      			if(len(add_ids)):
				print str(len(add_ids)) + " items!!!"
				for id in add_ids:
	  				link = new_items.get(id)
			  		webbrowser.open(link)
					print link
      			ids = new_ids
    		except IOError:
      			print "Error in reading url"
      			flg=False
      			continue 
    		cntr+=1
    		print cntr," times refreshed"
    		flg=True

crawlBrand()
