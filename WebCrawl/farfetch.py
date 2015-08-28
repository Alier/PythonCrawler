import urllib
import time
import os
import re
import webbrowser

ChloeUri = "http://www.farfetch.com/pk/shopping/women/search/items.aspx?q=chloe%20drew#ps=1&pv=60&oby=5"
BlackList = [] 

#UrlList = {"Valentino":ValentinoUri}
UrlList = {
"Chloe":ChloeUri}

def getItemList(sourceStr):
	itemRegex = 'data-item-id=\"([0-9]*)\"'
	itemdict = {}
	allitems = re.findall(itemRegex,sourceStr)
	#print allitems
	for item in allitems:
		linkRegex = 'href=\"(.*)-'+item+'.aspx?(.*)\" class=\"blankLink\">'
		linkpart1 = re.search(linkRegex,sourceStr).group(1)
		linkpart2 = re.search(linkRegex,sourceStr).group(2)
		fulllink = "http://www.farfetch.com/pk/shopping/women/"+linkpart1+"-"+item+".aspx?"+linkpart2
		#print fulllink
		itemdict[item]=fulllink
	#print itemdict
	return itemdict

def crawlBrand():
	brandItems = {}
	for brand in UrlList.keys():
		uri = UrlList.get(brand)
		source = urllib.urlopen(uri).read()
		ids = getItemList(source).keys()
		brandItems[brand] = ids		
	
	print brandItems
	cntr = 0
	flg = True
	while True:
		if flg:
			time.sleep(5)	#refresh every 5 seconds
		try:
			for brand in UrlList.keys():
				old_ids = brandItems[brand]
				uri = UrlList.get(brand)
				nw_source = urllib.urlopen(uri).read()
				new_items = getItemList(nw_source)
				new_ids = new_items.keys()
				add_ids = [i for i in new_ids if not i in old_ids]
				#print add_ids
				if (len(add_ids)):
					print brand + ":" + str(len(add_ids)) + " items!!!"
					for id in add_ids:
						if id not in BlackList:
						#print add_ids
						    link = new_items.get(id)
						    webbrowser.open(link)
						    print link
				#print old_ids
				#print new_ids
				brandItems[brand] = new_ids
				
		except IOError:
			print "Error in reading url"
			flg=False
			continue 
		cntr+=1
		print cntr," times refreshed"
		flg=True

#LoginEmail()
crawlBrand()
