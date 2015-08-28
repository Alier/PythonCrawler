import urllib2
import time
import os
import re
import webbrowser

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

Page1 = "http://www.bergdorfgoodman.com/Handbags/Sale/cat487302_cat257221_cat000000/c.cat"

#Page1 = "http://www.bergdorfgoodman.com/Sale/Handbags/cat421106_cat205700_cat000000/c.cat#userConstrainedResults=true&refinements=61,605,&page=1&pageSize=30&sort=PCS_SORT&definitionPath=/nm/commerce/pagedef/template/EndecaDriven&allStoresInput=false"

#Page2 = "http://www.bergdorfgoodman.com/Sale/Shoe-Salon/cat421105_cat205700_cat000000/c.cat?icid=SC3_3_Sale_ShoeSalon_US&cmCat=cat000000cat205700#endecaDrivenSiloRefinements=icid%3DSC3_3_Sale_ShoeSalon_US&userConstrainedResults=true&refinements=417,605,&page=1&pageSize=30&sort=&definitionPath=/nm/commerce/pagedef/template/EndecaDriven&allStoresInput=false"

#Page3 = "http://www.bergdorfgoodman.com/Mansur-Gavriel/Designers-A-Z/cat439100_cat000001/c.cat?navAction=index"

TestPage = "http://www.bergdorfgoodman.com/Sale/Shoe-Salon/cat421105_cat205700_cat000000/c.cat#userConstrainedResults=true&refinements=4294929541,299,4294954849,4294932388,605,&page=1&pageSize=120&sort=&definitionPath=/nm/commerce/pagedef/template/EndecaDriven&allStoresInput=false&onlineOnly="

#UriList = [Page1,Page2]
UriList = [Page1]

def getItemList():
	global testcontent
	itemdict = {}
	IDregex = ' product_id="prod([0-9]*)"'
	for url in UriList:
		req = urllib2.Request(url,headers=hdr)
		response = urllib2.urlopen(req)
		source = response.read()
		idList = re.findall(IDregex,source)
		#print idList
		for id in idList:
			LinkRegex = 'href=\"/(.*)/prod'+id+'_cat([0-9]*)__/p.prod?(.*)\">'
			match = re.search(LinkRegex,source)
			#print match
			productName = match.group(1)
			catId = match.group(2)
			link = match.group(3)
			#print productName
			#print catId
			#print link
			fulllink = "http://www.bergdorfgoodman.com/"+productName+"/prod" + id + "_cat" + catId +"__/p.prod?"+link
			#print fulllink
			itemdict[id]=fulllink
	#print itemdict
	return itemdict

def crawlBrand():
	ids = getItemList().keys()
	print len(ids)
	print ids
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
