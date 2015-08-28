import urllib
import time
import os
import re
import smtplib
import winsound, sys
import webbrowser

#ShoesUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418075_sort&Ns=P_306418075_sort&N=306418075%201553+4294957131+1678+1594+1614+1754+1686+4294908031+1574+4294962730+399546193+399546196"

#HandBagUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418110_sort&N=306418110+1553"

ValentinoUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&Ns=P_306418049_sort&N=306418049%201553+4294962730"  #url where result will be declared

#PradaUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&Ns=P_306418049_sort&N=306418049%201553+1686"

#FendiUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&N=306418049%201553+2018"

#GucciUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&N=306418049%201553+1678"

VinceUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306418066_sort&N=1553+1663+306418066"

PhilipUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&N=306418049%201553+4294918077"

ToryUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?Ns=P_306418049_sort&N=306418049%201553+4294950150"

#LongchampUri = "http://www.saksfifthavenue.com/Longchamp/Shoes-and-Handbags/shop/_/N-1z12vg4Z52floh/Ne-6lvnb6"

BVUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306418049_sort&N=1553+1795+306418049"

SFUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306418049_sort&N=1553+1568+306418049"

BurUri = "http://www.saksfifthavenue.com/search/EndecaSearch.jsp?brandLanding=true&Ns=P_306418048_sort&N=1553+4294918681+1585+4294962759+1897+306418048"

#UrlList = {"Valentino":ValentinoUri}
UrlList = {"Valentino":ValentinoUri,"Vince":VinceUri, "Philip": PhilipUri,"Tory":ToryUri,"BV":BVUri, "SF":SFUri, "Burberry":BurUri}

fromaddr = "aliertest238@gmail.com"
toaddr = "zhangai.za@gmail.com"
password = "aliertest"

server = smtplib.SMTP('smtp.gmail.com', 587)

def beep(sound):
        winsound.PlaySound('%s.wav' % sound, winsound.SND_FILENAME)
    
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
	
	#print brandItems
	cntr = 0
	flg = True
	while True:
    		if flg:
      			time.sleep(5)  #refresh every 5 seconds
    		try:
      			for brand in UrlList.keys():
				old_ids = brandItems[brand]
				uri = UrlList.get(brand)
				nw_source = urllib.urlopen(uri).read()
				new_items = getItemList(nw_source)
				new_ids = new_items.keys()
				add_ids = [i for i in new_ids if not i in old_ids ]
				if(len(add_ids)):
					print brand + ":" + str(len(add_ids)) + " items!!!"
					with open("sakslinks.txt", "a") as myfile:
                                                myfile.write(brand + ":" + str(len(add_ids)) + " items!!!\n")
                                        beep(100)
					for id in add_ids:
	  					link = new_items.get(id)
	  					webbrowser.open(link)
						print link
						with open("sakslinks.txt", "a") as myfile:
                                                        myfile.write(link +'\n')
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
