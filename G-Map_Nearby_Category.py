from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs

def browser_open():
    print('Browser Open....')
    global browser
    global action
    try:
        browser=webdriver.Chrome()
    except:
        print('Installing New Driver......')
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.set_page_load_timeout(30)
    action = ActionChains(browser)
    
def scroll():
    try:
        action = ActionChains(browser)
        action.send_keys(Keys.TAB*10).perform()
        for i in range(30):
            action.send_keys(Keys.END).perform()
            sleep(1)
    except:
        pass
        
def data(ca,lat,lon):
    n=1
    while n<5:
        try:
            browser.get(f"https://www.google.com/maps/search/{ca}/@{lat},{lon},16z/data=!4m7!2m6!3m4!2s{lat},{lon}!4m2!1d{lon}!2d{lat}!6e5?entry=ttu")
            #action = ActionChains(browser)
            sleep(1)
            scroll()
            s1 = bs(browser.page_source,'html.parser')
            break
        except:
            browser.quit()
            browser_open()
            n+=1
    eol = "NA"
    try:
        eol = s1.find('span',{'class':'HlvSq'}).text
    except:pass
    s2 = s1.findAll('a',{'class':'hfpxzc'})
    for x in s2:
            print(f"{ca}\t{lat}\t{lon}\t{x['href']}\t{len(s2)}\t{eol}\n")

ca = 'Computer Course'
browser_open()
lat,lon = 10.855770010345443, 79.48106467251476
data(ca,lat,lon)
print ("Done>>>>>>>>>>>>>>>>>>>>>>>>>")
browser.close()
