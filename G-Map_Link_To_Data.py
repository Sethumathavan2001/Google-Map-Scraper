from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
import datetime


browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
url = "https://www.google.com/maps/place/ASM+Browsing+%26+Computer+Course+Center/data=!4m7!3m6!1s0x3a5537951c8e0ab9:0xf5d03f6fd26fadcd!8m2!3d10.8102399!4d79.4704467!16s%2Fg%2F11sbwwcqn3!19sChIJuQqOHJU3VToRza1v0m8_0PU?authuser=0&hl=en&rclk=1"
n=1
while n<5:
    try:
        browser.get(url)
        sleep(4)
        s1 = bs(browser.page_source,'html.parser')
        break
    except:
        browser.quit()
        browser = webdriver.Chrome()
        browser.set_page_load_timeout(30)
name = sname = star = rating = ca = a_name = review = address = address2 = status = phone = lat = long = img_name = 'NA'
try:name = s1.find('h1',{'class':'DUwDvf lfPIob'}).text.encode('ascii','ignore').decode()
except:pass
try:sname = s1.find('h2',{'class':'bwoZTb'}).text.encode('ascii','ignore').decode()
except:pass
try:
    star,rating = map(lambda x:x.replace(',','').replace(')',''),s1.find('div',{'class':'F7nice'}).text.split('('))
    review = f"{star}/({rating})"
except:pass
try:
    ca = s1.findAll('button',{'class':'DkEaL'})[0].text.encode('ascii','ignore').decode()
    #print(ca)
except:pass
try:
    img_link = s1.find('button',{'class':['aoRNLd','kn2E5e','NMjTrf','lvtCsd']}).find('img')['src']
    a_name = img_link.rsplit('/',1)[1].replace("=","_")+".png"
    img_name = str(datetime.datetime.now()).replace("-","_").replace(":","_").replace(".","_").replace("__","_")+".png"
except: pass
try:address2 = s1.find('button',{'data-item-id':'oloc'}).text.encode('ascii','ignore').decode()
except:
    try:
        ad = s1.find('button',{'data-tooltip':'Copy address'}).text.encode('ascii','ignore').decode()
        if ad[4]=='+':
            address2=ad
            no_ad = 0
    except:pass
try:
    if no_ad:
        address = s1.find('button',{'data-tooltip':'Copy address'}).text.encode('ascii','ignore').decode()
except:pass
try:
    status = s1.find('span',{'class':'ZDu9vd'}).text.encode('ascii','ignore').decode()
    
except:pass
try:phone = s1.find('button',{'data-tooltip':'Copy phone number'}).text.encode('ascii','ignore').decode()
except:pass
try:lat,long = map(lambda x:x.split('!')[0],browser.current_url.split('!3d')[1].split('!4d'))
except:pass
output = {'Name': name,
 'Second_Name': sname,
 'Category': ca,
 'Review': review,
 'Address':address,
 'Address2': address2,
 'Phone': phone,
 'Latitude': lat,
 'Longitude': long,
 'Status': status,
 'Image': a_name
 }
print(output)

browser.quit()
