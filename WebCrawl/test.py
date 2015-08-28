#import mechanize

#import testPrint

#import webbrowser

url = "http://www.neimanmarcus.com/Gucci-Zebra-Print-Silk-Strapless-Gown-Gucci/prod172220493_cat980731__/p.prod??icid=&searchType=SALE&rte=%252Fsearch.jsp%253FN%253D0%2526from%253Dsaledi%2526st%253Ds%2526rd%253D1%2526Ntt%253DGucci&eItemId=prod172220493&cmCat=search"

url2 = "http://www.neimanmarcus.com/Jimmy-Choo-Deckle-Double-Band-Leather-Slide-Black-Shoes/prod174060361_cat46590745__/p.prod?icid=&searchType=EndecaDrivenCat&rte=%252Fcategory.jsp%253FitemId%253Dcat46590745%2526pageSize%253D120%2526No%253D0%2526refinements%253D&eItemId=prod174060361&cmCat=product"

url3 = "http://www.neimanmarcus.com/Gucci-Bamboo-Large-Shopper-Tote-Bag-Nero-Gucci/prod167820056___/p.prod?icid=&searchType=MAIN&rte=%252Fsearch.jsp%253FN%253D4294914334%2526from%253Dsaledi%2526rd%253D1%2526Ntt%253DGucci&eItemId=prod167820056&cmCat=search"

UrlList =[url,url2,url3]

patterns = ["Bag","Shoe"]

for url in UrlList:
	if patterns[0] in url or patterns[1] in url:
		print url
#webbrowser.open(url)
#testPrint.Print("hello")
#url = "http://www.neimanmarcus.com/Sale/Handbags/cat46520737_cat980731_cat000000/c.cat?icid=SiloMain4_3_Sale_Handbags_US"

#hh = mechanize.HTTPHandler()  # you might want HTTPSHandler, too
#hh.set_http_debuglevel(1)
#opener = mechanize.build_opener(hh)
#response = opener.open(url)

#import urllib2

#req = urllib2.Request(url)
#response = urllib2.urlopen(req)
#the_page = response.read()


#print the_page
