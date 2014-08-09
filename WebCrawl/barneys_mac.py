import urllib
import time
import os
import re
import webbrowser

Page1="http://www.barneys.com/on/demandware.store/Sites-BNY-Site/default/Search-Show?cgid=womens-bags&prefn1=onSale&prefv1=true"

Page2="http://www.barneys.com/on/demandware.store/Sites-BNY-Site/default/Search-Show?cgid=womens-bags&prefn1=onSale&prefv1=true&start=48&sz=48#"

UriList = [Page1,Page2]

def getItemList():
	itemdict = {}
	IDregex = '<span class="id">([0-9]*)</span>'
	#IDregex = '<div id="fashion_([0-9]*)" data-style-number'
	for uri in UriList:
		source = urllib.urlopen(uri).read()
		idList = re.findall(IDregex,source)
		for id in idList:
			LinkRegex = 'pid='+id+'&cgid=womens-bags&index=([0-9]*)</span>'
			index = re.findall(LinkRegex,source)[0]
			fulllink = "http://www.barneys.com/on/demandware.store/Sites-BNY-Site/default/Product-Show?pid="+id+"&cgid=womens-bags&index="+index
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
			add_ids = [i for i in new_ids if not i in ids]
      			if(len(add_ids)):
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
