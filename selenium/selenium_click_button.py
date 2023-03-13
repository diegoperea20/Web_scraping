from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

website="https://es.stackoverflow.com/"
path="C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe"

# website driver chromedriver.chromium.org/downloads
#leve open the page
options = Options()
options.add_experimental_option("detach", True)
#---
service=Service(executable_path=path)

driver = webdriver.Chrome(service=service,options=options)

driver.get(website)

containers=driver.find_element(by="xpath" , value='//div[@class="ml12 aside-cta flex--item print:d-none"]/a').click()
print("boton encontrado")
close_x=driver.find_element(by="xpath" , value='//a[@class="s-modal--close s-btn s-btn__muted js-modal-close js-last-tabbable js-gps-track"]').click()
print("boton x encontrado")
titulo=driver.find_element(by="xpath" , value='//input[@id="title"]').send_keys("test")
print("titulo encontrado")

div_google=driver.find_element(by="xpath" , value='//div[@class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon google-login"]')
print("div google encontrado")


close_cookies=driver.find_element(by="xpath" , value='//button[@class="flex--item6 s-btn s-btn__primary js-accept-cookies js-consent-banner-hide"]').click()
print("boton cookies encontrado")

div_google.click()
print("div click google encontrado")
""" titulo=driver.find_element(by="xpath", value='//input[@id="title"]')
if titulo:
    titulo.send_keys("test")
    print("bueno")
else:
    print("No se pudo encontrar el elemento.") """