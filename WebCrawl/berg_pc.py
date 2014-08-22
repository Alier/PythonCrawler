import urllib2
import time
import os
import re
import webbrowser

import windowsSound

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#Page1 ="http://www.bergdorfgoodman.com/Sale/Handbags/cat421106_cat205700_cat000000/c.cat#userConstrainedResults=true&refinements=75,142,4294963929,4294932388,605,&page=1&pageSize=30&sort=PCS_SORT&definitionPath=/nm/commerce/pagedef/template/EndecaDriven&allStoresInput=false"

#Page2 = "http://www.bergdorfgoodman.com/Sale/Shoe-Salon/cat421105_cat205700_cat000000/c.cat?icid=SC3_3_Sale_ShoeSalon_US&cmCat=cat000000cat205700#endecaDrivenSiloRefinements=icid%3DSC3_3_Sale_ShoeSalon_US&userConstrainedResults=true&refinements=4294948822,417,4294932388,578,605,&page=1&pageSize=30&sort=PCS_SORT&definitionPath=/nm/commerce/pagedef/template/EndecaDriven&allStoresInput=false"

Valentino = "http://www.bergdorfgoodman.com/Valentino/Shoes/cat204600_cat20062_cat000001/c.cat#refinements=&page=1&pageSize=120&sort=&definitionPath=/nm/commerce/pagedef/template/EndecaDriven&allStoresInput=false"

PhilipLim = "http://www.bergdorfgoodman.com/3.1-Phillip-Lim/Handbags/cat406323_cat406310_cat000001/c.cat"

ValentinoNM = "http://www.neimanmarcus.com/Valentino/Shoes/cat15450749_cat6060749_cat000730/c.cat?cmCat=cat000000cat000730cat6060749"
PhilipLimNM = "http://www.neimanmarcus.com/3.1-Phillip-Lim/Handbags/cat40480733_cat32780732_cat000730/c.cat"

UriListBG = [Valentino,PhilipLim]
UriListNM = [ValentinoNM,PhilipLimNM]

def getItemList(NM_flag):
        #print NM_flag
	global testcontent
	itemdict = {}
	UriList = []
	linkprefix = ""
	if NM_flag == True:
                UriList = UriListNM
                linkprefix = "http://www.neimanmarcus.com/"
        else:
                UriList = UriListBG
                linkprefix = "http://www.bergdorfgoodman.com/"

	IDregex = '<div product_id="prod([0-9]*)"'
	#print UriList
	for url in UriList:
		req = urllib2.Request(url,headers=hdr)
		response = urllib2.urlopen(req)
		source = response.read()
		idList = re.findall(IDregex,source)
		#print idList
		for id in idList:
			LinkRegex = 'href=\"/(.*)/prod'+id+'_cat([0-9]*)__/p.prod?(.*)\">'
			match = re.search(LinkRegex,source)
			productName = match.group(1)
			catId = match.group(2)
			link = match.group(3)
			#print productName
			#print catId
			#print link
			fulllink = linkprefix+productName+"/prod" + id + "_cat" + catId +"__/p.prod?"+link
			#print fulllink
			itemdict[id]=fulllink
			
	return itemdict

def crawlBrand():
	BG_ids = getItemList(False).keys()
	print len(BG_ids)
	print BG_ids
	NM_ids = getItemList(True).keys()
	print len(NM_ids)
	print NM_ids
	cntr = 0
	flg = True
	while True:
    		if flg:
      			time.sleep(5)  #refresh every 5 seconds
    		try:
      			BG_new_items = getItemList(False)
      			BG_new_ids = BG_new_items.keys()
			BG_add_ids = [i for i in BG_new_ids if not i in BG_ids ]
      			if(len(BG_add_ids)):
				windowsSound.beep(50)
				print str(len(BG_add_ids)) + " items!!!"
				for id in BG_add_ids:
	  				link = BG_new_items.get(id)
					webbrowser.open(link)
			  		print link
      			BG_ids = BG_new_ids

                        NM_new_items = getItemList(True)
      			NM_new_ids = NM_new_items.keys()
			NM_add_ids = [i for i in NM_new_ids if not i in NM_ids ]
      			if(len(NM_add_ids)):
                        	windowsSound.beep(50)
				print str(len(NM_add_ids)) + " items!!!"
				for id in NM_add_ids:
	  				link = NM_new_items.get(id)
					webbrowser.open(link)
			  		print link
      			NM_ids = NM_new_ids
      			
    		except IOError:
      			print "Error in reading url"
      			flg=False
      			continue 
    		cntr+=1
    		print cntr," times refreshed"
    		flg=True

crawlBrand()
