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

BurberryScarf = "http://www1.bloomingdales.com/shop/search?keyword=burberry+scarf"

BurberryCoat = "http://www1.bloomingdales.com/shop/sale/women/Brand/Burberry?id=3985"

Longchamp = "http://www1.bloomingdales.com/shop/search?keyword=longchamp+le+pilage"

FerragamoBags = "http://www1.bloomingdales.com/shop/sale/handbags/Brand/Salvatore%20Ferragamo?id=5070"
#"http://www1.bloomingdales.com/shop/ferragamo/salvatore-ferragamo-handbags?id=19209"

#MKAva = "http://www1.bloomingdales.com/shop/search?keyword=michael+kors+ava"

Sizes = {"UGG_Bailey_button":['"size": "5"','"size": "6"','"size": "7"'],
		 "UGG_Bailey_bow":['"size": "5"','"size": "6"','"size": "7"']}
Links = {"UGG_Bailey_bow":"http://www1.bloomingdales.com/shop/product/ugg-australia-boots-bailey-bow?ID=1054951&CategoryID=4841&LinkType=#fn=BRAND%3DUGG%AE%20Australia%26SHOE_STYLE%3DBoots%26spp%3D4%26ppp%3D180%26sp%3D1%26rid%3D%26spc%3D6%26pn%3D1",
			"UGG_Bailey_button":"http://www1.bloomingdales.com/shop/product/ugg-australia-boots-bailey-button?ID=1054917&CategoryID=16961#fn=spp%3D10%26ppp%3D180%26sp%3D1%26rid%3D%26spc%3D11%26cm_kws%3Dbailey button %26pn%3D1"}

Pages = [BurberryScarf, BurberryCoat, Longchamp, FerragamoBags]

itemdict = {}
sizedict = {}  # {"UGG_Bailey_button":4"} meaning there are 4 colours with size 6

def getItemList():
	newitemdict ={}
	IDregex = '{"id":"([0-9]*)",'
	#print UriList
	
	for url in Pages:
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
			LinkRegex = ' href="http://www1.bloomingdales.com/shop/product/(.*)?ID='+id+'(.*)">'
			productName = re.search(LinkRegex,source).group(1)
			cat = re.search(LinkRegex,source).group(2)
			#link = re.search(LinkRegex,source).group(3)
			#print productName
			#print cat
			#for pat in Patterns:
			#if pat in productName:
			fulllink = "http://www1.bloomingdales.com/shop/product/"+productName+"ID="+id+cat
			#http://www1.bloomingdales.com/shop/product/burberry-half-mega-check-silk-cashmere-scarf?ID=1216264&CategoryID=3376&cm_kws=1216264
			#print fulllink
			newitemdict[id]=fulllink
		#break
		#print url
		#print len(idList)
	return newitemdict

def getItemCount():
	global sizedict
	newsizedict = {}
	
	for brand in Links.keys():
		url = Links.get(brand)
		IDregexs = Sizes.get(brand)
		newsizedict[brand]= [0] * len(IDregexs)
		req = urllib2.Request(url,headers=hdr)
		response = urllib2.urlopen(req)
		try:
			source = response.read()
		except httplib.IncompleteRead, e:
			source = e.partial
		#source = response.read()
		for i in range(0, len(IDregexs)):
			regex = IDregexs[i]
			#print regex
			idList = re.findall(regex,source)
			#print idList
			#print "idlen ="+str(len(idList))
			#print "sizedict len" + str(sizedict.get(brand))
			# not first time
			if sizedict and sizedict.get(brand) and len(idList) > sizedict.get(brand)[i]:
				print "new colour for "+regex
			#webbrowser.open(url)
				print url
			newsizedict[brand][i] = len(idList)
	
	#print newsizedict
	return newsizedict	
		
def crawlAll():
	itemdict = getItemList()
	#print itemdict.keys()
	sizedict = getItemCount()

	cntr = 0
	flg = True
	while True:
    		if flg:
    			#randomt = random.randint(5,30)
    			#print "sleeping "+ str(randomt)
    			time.sleep(5)
      		try:
      			sizedict = getItemCount()
      			#print sizedict
      			# crawl pages
      			newitemdict = getItemList()
      			new_ids = newitemdict.keys()
      			old_ids = itemdict.keys()
      			add_ids = [i for i in new_ids if not i in old_ids]
      			if len(add_ids):
      				print str(len(add_ids)) + " items!!!"
      				for id in add_ids:
      					link = newitemdict.get(id)
      					webbrowser.open(link)
      					print link
      				itemdict = newitemdict
      		except IOError:
      			print "Error in reading url"
      			flg=False
      			continue 
      		cntr+=1
    		print cntr," times refreshed"
    		flg=True
      		
crawlAll()
