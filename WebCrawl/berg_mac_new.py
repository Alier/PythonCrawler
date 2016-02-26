import urllib2
import time
import os
import re
import webbrowser
import httplib
import random

#import windowsSound

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

PradaUri = "http://www.bergdorfgoodman.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Prada"

ValentinoUri = "http://www.bergdorfgoodman.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Valentino"

PhilipUri = "http://www.bergdorfgoodman.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=3.1+Phillip+Lim"

YSLUri = "http://www.bergdorfgoodman.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Saint+Laurent"

SFUri = "http://www.bergdorfgoodman.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Salvatore+Ferragamo"

AlexWangUri = "http://www.bergdorfgoodman.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Alexander+Wang"

GucciUri = "http://www.bergdorfgoodman.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Gucci"
#Page1 = "http://www.bergdorfgoodman.com/Handbags/Sale/cat487302_cat257221_cat000000/c.cat"

#Page2 = "http://www.bergdorfgoodman.com/Sale/Shoes/Shop-All-Shoes/cat477621_cat421105_cat205700/c.cat"
UrlList = {
"Prada":PradaUri,
"Valentino":ValentinoUri,
"3.1 Philip Lim":PhilipUri, 
"YSL": YSLUri, 
"SF": SFUri,
"AlexanderWang":AlexWangUri,
"Gucci":GucciUri
}

Patterns = ["Bag","Shoe"]

BlackList=['108320139','105270083','105270088','107430109','103960039','103960040','104650142']

def getItemList(url):
	global testcontent
	itemdict = {}
	IDregex = ' product_id="prod([0-9]*)"'
	#print UriList
	
	req = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	try:
		source = response.read()
	except httplib.IncompleteRead, e:
		source = e.partial
	idList = re.findall(IDregex,source)
	#print idList
	for id in idList:
		LinkRegex = 'href=\"/(.*)/prod'+id+'_cat([0-9]*)'+'__/p.prod?(.*)&cmCat=(.*)\">'
		productName = re.search(LinkRegex,source).group(1)
		cat = re.search(LinkRegex,source).group(2)
		link = re.search(LinkRegex,source).group(3)
		cmCat = re.search(LinkRegex,source).group(4)
		#print productName
		#print link
		#for pat in Patterns:
		#if pat in productName:
		fulllink = "http://www.bergdorfgoodman.com/"+productName+"/prod"+id+"_cat"+cat+"__/p.prod?"+link+"&cmCat="+cmCat
		#print fulllink
		itemdict[id]=fulllink
		#break
	return itemdict

def crawlBrand():
	brandItems = {}
	for brand in UrlList.keys():
		uri = UrlList.get(brand)
		ids = getItemList(uri).keys()
		brandItems[brand] = ids		
	
	print brandItems
	cntr = 0
	flg = True
	while True:
    		if flg:
    			randomt = random.randint(5,30)
      			time.sleep(randomt)  #refresh every 5 seconds
      		
      		try:
      			brand = random.choice(UrlList.keys())
      			print "brand :" + brand
      			if True:
					old_ids = brandItems[brand]
					uri = UrlList.get(brand)
					new_items = getItemList(uri)
					new_ids = new_items.keys()
					add_ids = [i for i in new_ids if not i in old_ids]
					#print add_ids
					if (len(add_ids)):
						print str(len(add_ids)) + " items!!!"
						for id in add_ids:
							if id not in BlackList:
								link = new_items.get(id)
						    	#webbrowser.open(link)
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

crawlBrand()
