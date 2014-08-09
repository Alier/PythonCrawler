import urllib2
import time
import os
import re
import webbrowser

designerList = ["31_phillip_lim","alexander_mcqueen","alexander_wang","proenza_schouler","saint_laurent","valentino"]

#Uri ="https://www.ssense.com/women/designers/<designer[*]>/bags"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def getItemList():
	itemdict = {}
	
	for designer in designerList:
		#print designer
		url = "https://www.ssense.com/women/designers/"+ designer +"/bags"
		#print url
		req = urllib2.Request(url,headers=hdr)
		try:    
	                response = urllib2.urlopen(req)
        	except urllib2.HTTPError, e:
                	print e.fp.read()
		
		source = response.read()
		IDregex = '<a href="/women/product/'+ designer +'/.*/([0-9]*)">'
		idList = re.findall(IDregex,source)
		#print idList
		
		for id in idList:
			LinkRegex = '/women/product/'+ designer +'/.*/'+id
			linkelem = re.findall(LinkRegex,source)
			fulllink = "https://www.ssense.com"+linkelem[0]
			itemdict[id]=fulllink
	return itemdict

def crawlBrand():
	ids = getItemList().keys()
	#print len(ids)
	#print ids
	cntr = 0
	flg = True
	while True:
    		if flg:
      			time.sleep(5)  #refresh every 5 seconds
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
