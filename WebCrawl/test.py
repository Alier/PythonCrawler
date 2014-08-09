#import mechanize

import testPrint

testPrint.Print("hello")
url = "http://www.neimanmarcus.com/Sale/Handbags/cat46520737_cat980731_cat000000/c.cat?icid=SiloMain4_3_Sale_Handbags_US"

#hh = mechanize.HTTPHandler()  # you might want HTTPSHandler, too
#hh.set_http_debuglevel(1)
#opener = mechanize.build_opener(hh)
#response = opener.open(url)

#import urllib2

#req = urllib2.Request(url)
#response = urllib2.urlopen(req)
#the_page = response.read()

import webbrowser

webbrowser.open(url)

#print the_page
