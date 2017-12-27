from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4



path1 = r'C:\Python27\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(path1)
browser.get('https://www.quora.com/What-are-the-best-Python-scripts-youve-ever-written')

time.sleep(5)
i=0
count = 0

SCROLL_PAUSE_TIME = 0.2
last_time = 0
count = 0

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    count = count + 1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height != last_height:
        last_time = count
    elif count-last_time==20:
        break
    last_height = new_height

print count

'''
#2
while(count!=430):
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #browser.find_element_by_xpath('//*[@id="Div1"]/div/partner-data/div[3]/div['+ str(11+i*9)+']/div[1]/a/span').click()
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #browser.find_element_by_xpath('//*[@id="PartnerProfilles"]/div['+str(10+i*9)+']/div[1]/a/span').click()
    except Exception, err:
        i=i-1
        print Exception, err
        time.sleep(3)
    #browser.find_element_by_css_selector('#PartnerProfilles > div.row.col-lg-10 > div:nth-child(1) > a > span').click()
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.2)
    i=i+1
    count = count+1



elem3 = browser.page_source
#print elem3.text

f = open("D:\kaaka\search_new\NewProfiles.txt","w+")
# + creates a file if its not there
f1 = open("D:\kaaka\search_new\Profiles.txt","ab+")
str = f1.read()
f1.seek(0,2)

soup = bs4.BeautifulSoup(elem3,'html.parser')
for a in soup.findAll('p',{"class" : "label_check pull-left clearfix"}):
        #print a.text
        if a.text.strip() not in str:
            f.write(a.text.strip()+'\n')
            f1.write(a.text.strip()+'\r\n' )
            #or print a.string
'''
