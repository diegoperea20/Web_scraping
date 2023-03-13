from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

website="https://www.thesun.co.uk/sport/football/"
path="C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe"

# website driver chromedriver.chromium.org/downloads

# HEADLESS-MODE
options=Options()
options.headless=True

service=Service(executable_path=path)
driver = webdriver.Chrome(service=service , options=options)
driver.get(website)

containers=driver.find_elements(by="xpath" , value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []


for container in containers:
    titile=container.find_element(by="xpath", value='./a/h3').text
    subttitle=container.find_element(by="xpath", value='./a/p').text
    link=container.find_element(by="xpath", value='./a').get_attribute('href')
    titles.append(titile)
    subtitles.append(subttitle)
    links.append(link)

my_dict={'title':titles,'subtitle':subtitles,'link':links}
df_healines=pd.DataFrame(my_dict).to_csv('thesun-head-mode.csv')

driver.quit()