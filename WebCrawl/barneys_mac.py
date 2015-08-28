import urllib
import time
import os
import re
import webbrowser

Page1="http://www.barneys.com/barneys-new-york/women/bags?prefn1=onSale&prefv1=Sale#prefn1=brand&prefn2=onSale&prefv2=Sale&sz=85&prefv1=3.1%20Phillip%20Lim%7CAlexander%20McQueen%7CAlexander%20Wang%7CBottega%20Veneta%7CChlo%C3%A9%7CGivenchy%7CFendi%7CSaint%20Laurent&pageviewchange=true"

#Page2="http://www.barneys.com/barneys-new-york/women/shoes?prefn1=onSale&prefv1=Sale#prefn1=brand&prefn2=onSale&prefv2=Sale&prefv1=Manolo%20Blahnik%7CMiu%20Miu%7CRag%20%2526%20Bone%7CSaint%20Laurent"

UriList = [Page1]#,Page2]

def getItemList():
	itemdict = {}
	IDregex = ' data-itemid="([0-9]*)">'
	#IDregex = '<div id="fashion_([0-9]*)" data-style-number'
	for uri in UriList:
		source = urllib.urlopen(uri).read()
		idList = re.findall(IDregex,source)
		for id in idList:
			LinkRegex = ' href="http://www.barneys.com/(.*)-'+id+'.html" title='
			item = re.findall(LinkRegex,source)[0]
			fulllink = "http://www.barneys.com/"+item+"-"+id+".html"
			itemdict[id]=fulllink
        return itemdict

def crawlBrand():
	ids = getItemList().keys()
    	cntr = 0
	flg = True
        print ids
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
