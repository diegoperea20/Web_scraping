from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

# execution the code every day no manually

application_path= os.path.dirname(sys.executable)

now=datetime.now()
year_moth_day=now.strftime("%Y-%m-%d")


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
df_healines=pd.DataFrame(my_dict)


file_name=f'thesun--{year_moth_day}.csv'
final_path=os.path.join(application_path,file_name)

df_healines.to_csv(final_path)

driver.quit()

#for exeecute any time do:
"""
1.pip install pyinstaller
2.pyinstaller --onefile name_file.py
3.folder named 'dist' and execute the file  in the terminal
 """