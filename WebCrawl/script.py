import urllib
import time
import os
import re
import smtplib

HandBagUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418110_sort&N=306418110+1553"

ValentinoUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&Ns=P_306418049_sort&N=306418049%201553+4294962730"  #url where result will be declared

PradaUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&Ns=P_306418049_sort&N=306418049%201553+1686"

fromaddr = "aliertest238@gmail.com"
toaddr = "zhangai.za@gmail.com"
password = "aliertest"

server = smtplib.SMTP('smtp.gmail.com', 587)
 
def LoginEmail():
	global server
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(fromaddr,password)

def sendEmail(text):
	global server
	server.sendmail(fromaddr, toaddr, text)

def getItemList(sourceStr):
	totalRegex = '<a id=\"image-url-.*\" href=\"http://.*\">'
	allitems = re.findall(totalRegex,sourceStr)
	linkRegex = 'href=\"(.*)\"'
	itemRegex = 'id=\"image-url-([0-9]*)\"'
	itemdict = {}
	for item in allitems:
		link = re.search(linkRegex,item).group(1)
		itemid = re.search(itemRegex,item).group(1)
		itemdict[itemid]=link
	return itemdict

def crawlBrand(Branduri):
	uri = Branduri
	source = urllib.urlopen(uri).read()

	ids = getItemList(source).keys()
	new_ids = ids
	cntr = 0
	flg = True
	while True:
    		if flg:
      			time.sleep(5)  #refresh every 5 seconds
    		try:
      			nw_source = urllib.urlopen(uri).read()
      			new_items = getItemList(nw_source)
      			new_ids = new_items.keys()
			add_ids = [i for i in new_ids if not i in ids ]
			if(len(add_ids)):
				print str(len(add_ids)) + " items!!!"
				for id in add_ids:
	  				link = new_items.get(id)
					print link
				#sendEmail(str(links))
      			ids = new_ids
    		except IOError:
      			print "Error in reading url"
      			flg=False
      			continue 
    		cntr+=1
    		print cntr," times refreshed"
    		flg=True

#LoginEmail()
#crawlBrand(PradaUri)
crawlBrand(HandBagUri)
