from bs4 import BeautifulSoup

import requests

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}  # for no dectect like robot


html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=' , headers=encabezado).text

soup=BeautifulSoup(html_text,'lxml')
# way singularity ,1 thing
""" job=soup.find('li',class_='clearfix job-bx wht-shd-bx')
company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','') 
skills=job.find('span',class_='srp-skills').text.replace(' ','') 
time_for=job.find('span',class_='sim-posted').text 
print(f'''
company name: {company_name} 
skills :{skills}
time:{time_for}''') """
# way plural,many things all
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','') 
    skills=job.find('span',class_='srp-skills').text.replace(' ','') 
    time_for=job.find('span',class_='sim-posted').text 
    more_info=job.header.h2.a['href']
    print(f'''
    company name: {company_name} 
    skills :{skills}
    time:{time_for}
    info:{more_info}
    ''')
    print("".center(50, "-"))


# automatizaion 
""" 
for job in jobs:
    time_for=job.find('span',class_='sim-posted').text
    if "few" in time_for:
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','') 
        skills=job.find('span',class_='srp-skills').text.replace(' ','') 
        
        print(f'''
        company name: {company_name} 
        skills :{skills}
        time:{time_for}
        ''')
        print("".center(50, "-")) """
     