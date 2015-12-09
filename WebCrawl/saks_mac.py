import urllib2
import time
import os
import re
import webbrowser
import random

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
       
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

MCMUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?N=1553+4294919520&brandLanding=true"

KSUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?N=1553+4294911028&brandLanding=true"

#BlackList = ['0468237205542','0408845359084','0434011446517','0439028154349','0400086591391','0439008487726','0442314060279','0437837644402','0400087298267','0468299952729','0468237202756','0468237212601','0434036987934','0437837655125','0452428806540','0452435882087','0419713461297','0452469153498','0452446211630','0437837659383','0400087297670','0468237235105','0468295269371','0468248698340','0434044608272','0468239126272','0468248709947','0468248211792','0468248699156','0468237222693','0452446216987','0454318301210','0468237220927','0468230247259','0468238903829','0468248710905','0468237218153','0414923887806','0442314047157','0414936894815','0454318311141','0414313053477','0442370450397','0442127697655','0400086710411','0419713581155', '0415233143262', '0419713580899','0442314080819','0442127694579','0439028152468'] 
#BlackList = ['0400086706170','0400086723567','0400086723513','0400086645149']

#UrlList = {"Valentino":ValentinoUri}
UrlList = {
#"Longchamp":LongChampUri,#"AlexanderMcqueen":AlexanderUri,
"Valentino":ValentinoUri,
"Philip": PhilipUri,
#"Tory":ToryUri,
#"BV":BVUri, 
"SF":SFUri, 
"Burberry":BurberryUri,
"Prada":PradaUri,
"Gucci":GucciUri,
"MB":MBUri,
"MCM":MCMUri,
"AlexanderWang":AlexanderUri
#"KS":KSUri
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
		req = urllib2.Request(uri,headers=hdr)
		source = urllib2.urlopen(req).read()
		#source = urllib.urlopen(uri).read()
		ids = getItemList(source).keys()
		brandItems[brand] = ids		
	
	print brandItems
	cntr = 0
	flg = True
	#windowsOpen = False
	
	while True:
		if flg:
			randomt = random.randint(5,30)
			print "sleeping "+ str(randomt)
			time.sleep(randomt)	#refresh every 5 seconds
		try:
			count = 0
			#print brandItems["Tory"]
			brand = random.choice(UrlList.keys())
			if brand in UrlList.keys():
				print "brand = " +brand
				old_ids = brandItems[brand]
				uri = UrlList.get(brand)
				new_req = urllib2.Request(uri,headers=hdr)
				nw_source = urllib2.urlopen(new_req).read()
				new_items = getItemList(nw_source)
				new_ids = new_items.keys()
				add_ids = [i for i in new_ids if not i in old_ids]
				#print add_ids
				if (len(add_ids)):
					print brand + ":" + str(len(add_ids)) + " items!!!"
					for id in add_ids:
					#if id not in BlackList:
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
