import urllib
import time
import os
import re
import webbrowser
#import smtplib

#ShoesUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418075_sort&Ns=P_306418075_sort&N=306418075%201553+4294957131+1678+1594+1614+1754+1686+4294908031+1574+4294962730+399546193+399546196"

#HandBagUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418110_sort&N=306418110+1553"

ValentinoUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?N=1553+4294962730&brandLanding=true"

GucciUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&N=1553+1678+306622828"

#ChloeUri = "http://www.saksfifthavenue.com/Chloe/Handbags/shop/_/N-1z12st3Z52jzot/Ne-6lvnb5"

MBUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?N=1553+4294962707&brandLanding=true"
#BagsUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306622828_sort&Ns=P_306622828_sort&N=306622828%201553"
PradaUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?&N=1553+1686"

#FendiUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&N=306418049%201553+2018"

#GucciUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&N=306418049%201553+1678"

#VinceUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&N=1553+1663"

PhilipUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306622828_sort&N=1553+4294918077+306622828"

ToryUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306622397_sort&N=1553+4294950150+306622397"

#LongchampUri = "http://www.saksfifthavenue.com/Longchamp/Shoes-and-Handbags/shop/_/N-1z12vg4Z52floh/Ne-6lvnb6"

#BVUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?N=1553+1795&brandLanding=true"

#SFUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306418049_sort&N=1553+1568+306418049"

SFUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?N=1553+1568&brandLanding=true"

BurberryUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306418048_sort&N=1553+1585+4294918681+4294962759+1897+306418048"

AlexanderUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?N=1553+4294957131&brandLanding=true"

LongChampUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&N=1553+1714"

BlackList = ['0414923887806','0442314047157','0414936894815','0454318311141','0414313053477','0442370450397','0442127697655','0400086710411','0419713581155', '0415233143262', '0419713580899','0442314080819','0442127694579','0439028152468'] 

#UrlList = {"Valentino":ValentinoUri}
UrlList = {
"Longchamp":LongChampUri,#"AlexanderMcqueen":AlexanderUri,
"Valentino":ValentinoUri,
"Philip": PhilipUri,
"Tory":ToryUri,
#"BV":BVUri, 
"SF":SFUri, 
#"Burberry":BurberryUri,
"Prada":PradaUri,
"Gucci":GucciUri,
"MB":MBUri
}

fromaddr = "aliertest238@gmail.com"
toaddr = "zhangai.za@gmail.com"
password = "aliertest"

#server = smtplib.SMTP('smtp.gmail.com', 587)
 
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
