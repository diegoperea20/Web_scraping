from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
#leve open the page
options = Options()
options.add_experimental_option("detach", True)
#---


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# definer pagina a scrapear y ruta donde descargaste chromediver
name="diego ivan perea montealegre"
website = 'https://www.google.com/search?q='+name
driver.get(website)
time.sleep(3)

arrayData  = []
arrayData1 = []
publ=1
""" searchbox2 = driver.find_element(By.XPATH,"//div[contains(@class,'v7W49e')]/div["+str(publ)+"]") """

searchbox2 = driver.find_element(By.XPATH,"//div[contains(@class,'v7W49e')]/div["+str(publ)+"]//div[contains(@class,'Z26q7c UK95Uc jGGQ5e')]/div/a").get_attribute('href')
#searchbox2 =searchbox2.text
print(searchbox2)