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

PradabagsUri = "http://www.neimanmarcus.com/eSearch.jsp?N=4294914334+&st=s&pageSize=30&Ntt=Prada&_requestid=283851"

#ValentinoUri = "http://www.neimanmarcus.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Valentino"

VshoesUri ="http://www.neimanmarcus.com/eSearch.jsp?N=4294914357&st=s&Ntt=Valentino&from=brSearchExcep&_requestid=284940"
VbagsUri ="http://www.neimanmarcus.com/eSearch.jsp?N=4294914334&st=s&Ntt=Valentino&from=brSearchExcep&_requestid=285151"

PhilipbagsUri = "http://www.neimanmarcus.com/eSearch.jsp?N=4294914334&st=s&Ntt=3.1+Phillip+Lim&from=brSearchExcep&_requestid=285420"

YSLbagsUri = "http://www.neimanmarcus.com/eSearch.jsp?N=4294914334&st=s&Ntt=Saint+Laurent&from=brSearchExcep&_requestid=285635"

SFshoesUri = "http://www.neimanmarcus.com/eSearch.jsp?N=4294914357&st=s&Ntt=Salvatore+Ferragamo&from=brSearchExcep&_requestid=285848"
SFbagsUri = "http://www.neimanmarcus.com/eSearch.jsp?N=4294914334&st=s&Ntt=Salvatore+Ferragamo&from=brSearchExcep&_requestid=286096"

#AlexWangUri = "http://www.neimanmarcus.com/search.jsp?N=0&from=saledi&st=s&rd=1&Ntt=Alexander+Wang"

GuccibagsUri = "http://www.neimanmarcus.com/eSearch.jsp?N=4294914334&st=s&Ntt=Gucci&from=brSearchExcep&_requestid=286272"
#Page1 = "http://www.bergdorfgoodman.com/Handbags/Sale/cat487302_cat257221_cat000000/c.cat"

#Page2 = "http://www.bergdorfgoodman.com/Sale/Shoes/Shop-All-Shoes/cat477621_cat421105_cat205700/c.cat"
UrlList = {
"Prada":PradabagsUri,
"Valentino1":VshoesUri,
"Valentino2":VbagsUri,
"3.1 Philip Lim":PhilipbagsUri, 
"YSL": YSLbagsUri, 
"SF1": SFshoesUri,
"SF2": SFbagsUri,
#"AlexanderWang":AlexWangUri,
"Gucci":GuccibagsUri
}

Patterns = ["Bag","Shoe"]

BlackList=['175280391']

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
	#source = response.read()
	idList = re.findall(IDregex,source)
	#print idList
	for id in idList:
		LinkRegex = 'href=\"/(.*)/prod'+id+'_cat([0-9]*)'+'__/p.prod?(.*)&cmCat=search\">'
		productName = re.search(LinkRegex,source).group(1)
		cat = re.search(LinkRegex,source).group(2)
		link = re.search(LinkRegex,source).group(3)
		#print productName
		#print link
		#for pat in Patterns:
		#if pat in productName:
		fulllink = "http://www.neimanmarcus.com/"+productName+"/prod"+id+"_cat"+cat+"__/p.prod?"+link+"&cmCat=search"
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
    			randomt = random.randint(5,15)
    			print "sleeping "+ str(randomt)
    			time.sleep(randomt)
      		try:
      			#brand = random.choice(UrlList.keys())
      			for brand in UrlList.keys():
					#print "brand: "+brand
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

crawlBrand()
