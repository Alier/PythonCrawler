import urllib2
import time
import os
import re
import webbrowser

#import windowsSound

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

Page1 = "http://www.neimanmarcus.com/Sale/Handbags/cat46520737_cat980731_cat980731/c.cat"
Page2 = "http://www.neimanmarcus.com/Sale/Handbags/cat46520737_cat980731_cat980731/c.cat#userConstrainedResults=true&refinements=&page=2&pageSize=30&sort=PCS_SORT&definitionPath=/nm/commerce/pagedef_rwd/template/EndecaDrivenHome&locationInput=&radiusInput=100&onlineOnly=&allStoresInput=false&rwd=true&catalogId=cat46520737"

UriList = [Page1, Page2]

def getItemList():
	global testcontent
	itemdict = {}
	IDregex = ' product_id="prod([0-9]*)"'
	for url in UriList:
		print url
		req = urllib2.Request(url,headers=hdr)
		response = urllib2.urlopen(req)
		source = response.read()
		idList = re.findall(IDregex,source)
		print idList
		for id in idList:
			LinkRegex = 'href=\"/(.*)/prod'+id+'_cat46520737__/p.prod?(.*)&eItemId=prod'+id+'&cmCat=product\">'
			productName = re.search(LinkRegex,source).group(1)
			link = re.search(LinkRegex,source).group(2)
			#print productName
			#print link
			if "Shirt" or "Pant" or "Jacket" or "Dress" in productName:
				idList.remove(id)
			else:
				fulllink = "http://www.neimanmarcus.com/"+productName+"/prod"+id+"_cat46520737__/p.prod?"+link+"&eItemId=prod"+id+"&cmCat=product"
			#print fulllink
				itemdict[id]=fulllink
	return itemdict

def crawlBrand():
	ids = getItemList().keys()
	print len(ids)
	print ids
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
				#windowsSound.beep(100)
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
