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

SFbags = "http://www1.bloomingdales.com/shop/ferragamo/salvatore-ferragamo-handbags?id=19209"

#MKAva = "http://www1.bloomingdales.com/shop/search?keyword=michael+kors+ava"

SFShoes = "http://www1.bloomingdales.com/shop/ferragamo/salvatore-ferragamo-shoes?id=19210"

MCM = "http://www1.bloomingdales.com/shop/mcm/handbags-wallets?id=1003796"

TBShoes = "http://www1.bloomingdales.com/shop/tory-burch/tory-burch-shoes?id=1002729"

Singles = {"SFVarina":'"color": "Oxford Blue", "size": "(\d+(\.\d+)?)", "type":'}
'''
        "UGG_Bailey_button":'"size": "',
         "UGG_Bailey_bow":'"size": "',
         "BBRPuffShort":'<li title=',
         "BBRParka":'<li title=',
         "BBRTrench":'<li title=',
         "BBRPuffLong":'<li title=',
         "BBRWoolCoatGrey":'<li title=',
         "BBRWoolCoatCamel":'<li title=',
         "BBRQuilt":'<li title=',
         "BBRPuffLong2":'<li title=',
         "BBRScarfSquare":'<li title=',
         "BBRNeedlethorpe":'<li title=',
         "ToryBurchFlat":'"size": "',
         "ToryBurchReva":'"size": "',
         "BBRTrench2":'<li title=',
         "SFGinny":'<li title=',
         "CashWrap":'<li title=',
         "SFWallet":'"color":',
         "SFMissVara":'"color":',
         "SFCarla":'<li title=',}
'''
         
Links = {
"SFVarina":"http://www1.bloomingdales.com/shop/product/salvatore-ferragamo-ballet-flats-varina?ID=1066212&CategoryID=16961#fn=ppp%3D180%26spp%3D7%26sp%3D1%26rid%3D%26spc%3D8%26cm_kws%3Dferragamo",
}
'''       
"SFCarla":"http://www1.bloomingdales.com/shop/product/salvatore-ferragamo-carla-suede-mid-heel-pumps?ID=1427321&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283506815",
"SFMissVara":"http://www1.bloomingdales.com/shop/product/salvatore-ferragamo-mini-bag-miss-vara-bow?ID=1181504&CategoryID=16958#fn=spp%3D5%26ppp%3D180%26sp%3D1%26rid%3D%26spc%3D18%26cm_kws%3Dvara%20%26pn%3D1",
"SFWallet":"http://www1.bloomingdales.com/shop/product/salvatore-ferragamo-gancini-icona-vitello-continental-wallet?ID=1586642&CategoryID=16958#fn=spp%3D49%26ppp%3D180%26sp%3D1%26rid%3D%26spc%3D51%26cm_kws%3Dferragamo%20gancini%20%26pn%3D1",
"CashWrap":"http://www1.bloomingdales.com/shop/product/c-by-bloomingdales-fringed-cashmere-travel-wrap?ID=1405248&CategoryID=2910&LinkType=prodrec_pdpza&RecProdZonePos=prodrec-2&RecProdZoneDesc=RR-CMIO-RT-POC%7CRR-CMIO%7Cprodrec_pdpza%7CRR&choiceId=",
"SFGinny":"http://www1.bloomingdales.com/shop/product/salvatore-ferragamo-crossbody-ginny-mini?ID=1585021&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283406107",
"BBRTrench2":"http://www1.bloomingdales.com/shop/product/burberry-brit-balmoral-trench-coat?ID=818693&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283396784",   
"ToryBurchReva":"http://www1.bloomingdales.com/shop/product/tory-burch-ballet-flats-reva-patent?ID=1358940&CategoryID=16961&cm_kws=1358940",
"ToryBurchFlat":"http://www1.bloomingdales.com/shop/product/tory-burch-ballet-flats-mini-miller?ID=1297609&CategoryID=1002729&brandIndex=1#fn=spp%3D36%26ppp%3D180%26sp%3D1%26rid%3D%26spc%3D90%26pn%3D1",
"BBRWoolCoatCamel":"http://www1.bloomingdales.com/shop/product/burberry-brit-rushfield-wool-blend-coat?ID=1586669&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283350223",
"BBRNeedlethorpe":"http://www1.bloomingdales.com/shop/product/burberry-brit-needlethorpe-double-breasted-coat?ID=1392849&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283360233",
"BBRScarfSquare":"http://www1.bloomingdales.com/shop/product/burberry-overdyed-chambray-check-square-scarf?ID=1066135&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283369502",
"BBRPuffLong2":"http://www1.bloomingdales.com/shop/product/burberry-brit-allerdale-mid-length-down-puffer-coat?ID=1497784&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283393479",
"BBRQuilt":"http://www1.bloomingdales.com/shop/product/burberry-brit-ashurst-quilted-jacket?ID=1283874&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283376390",
"BBRWoolCoatGrey":"http://www1.bloomingdales.com/shop/product/burberry-brit-rushfield-wool-blend-coat?ID=1392816&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283369576",
"BBRPuffLong":"http://www1.bloomingdales.com/shop/product/burberry-brit-finsbridge-coat?ID=1283922&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283360374",
"BBRTrench":"http://www.bloomingdales.com/shop/product/?ID=1583660&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283350276",
"BBRParka":"http://www1.bloomingdales.com/shop/product/burberry-brit-fenstone-parka-with-warmer-lining?ID=1283875&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283380160",
"BBRPuffShort":"http://www1.bloomingdales.com/shop/product/burberry-brit-dalesbury-down-jacket?ID=1158386&FromWishList=My%20Wish%20List&listType=WISH_LIST&listItemId=283380161",
"UGG_Bailey_bow":"http://www1.bloomingdales.com/shop/product/ugg-australia-boots-bailey-bow?ID=1054951&CategoryID=4841&LinkType=#fn=BRAND%3DUGG%AE%20Australia%26SHOE_STYLE%3DBoots%26spp%3D4%26ppp%3D180%26sp%3D1%26rid%3D%26spc%3D6%26pn%3D1",
"UGG_Bailey_button":"http://www1.bloomingdales.com/shop/product/ugg-australia-boots-bailey-button?ID=1054917&CategoryID=16961#fn=spp%3D10%26ppp%3D180%26sp%3D1%26rid%3D%26spc%3D11%26cm_kws%3Dbailey button %26pn%3D1"}
'''
Pages = [BurberryScarf, 
        BurberryCoat, 
        #Longchamp, 
        #SFbags, 
        SFShoes, 
        #MKAva, 
        MCM,
        TBShoes]

itemdict ={}
sizedict ={}  
# {"UGG_Bailey_button":4"} meaning there are 4 colours with size 6

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
	#print source
        idList = re.findall(IDregex,source)
        #print idList
        for id in idList:
            LinkRegex = ' href="http://www1.bloomingdales.com/shop/product/(.*)?ID='+id+'(.*)" class'
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
        IDregex = Singles.get(brand)
        #print IDregex
        req = urllib2.Request(url,headers=hdr)
        response = urllib2.urlopen(req)
        try:
            source = response.read()
        except httplib.IncompleteRead, e:
            source = e.partial
        #source = response.read()
        #for i in range(0, len(IDregexs)):
            #print regex
        idList = re.findall(IDregex,source)
        sizes = [size for (size, t) in idList] 
        #print idList
        #print sizes
            #print "idlen ="+str(len(idList))
            #print "sizedict len" + str(sizedict.get(brand))
            # not first time
        if sizedict and sizedict.get(brand) and len(sizes) > sizedict.get(brand):
            print "new for "+regex
            #webbrowser.open(url)
            print url
        newsizedict[brand] = sizes
    
    print newsizedict
    return newsizedict  
        
def crawlAll():
    itemdict = getItemList()
    print itemdict.keys()
    #sizedict = getItemCount()
    #print sizedict
    
    cntr = 0
    flg = True
    while True:
            if flg:
                #randomt = random.randint(5,10)
                randomt = 5
                #print "sleeping "+ str(randomt)
                time.sleep(randomt)
            try:
                #sizedict = getItemCount()
                #print newsizedict.keys()
                # print sizedict
                # crawl pages
                newitemdict = getItemList()
                new_ids = newitemdict.keys()
                old_ids = itemdict.keys()
                add_ids = [i for i in new_ids if not i in old_ids]
                if len(add_ids):
                    print str(len(add_ids)) + " items!!!"
                    for id in add_ids:
                        link = newitemdict.get(id)
                        #webbrowser.open(link)
                        print link
                    itemdict = newitemdict
                #for size in newsizedict
            except IOError:
                print "Error in reading url"
                flg=False
                continue 
            cntr+=1
            print cntr," times refreshed"
            flg=True
            
crawlAll()
