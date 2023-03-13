from bs4 import BeautifulSoup

import requests

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}  # for no dectect like robot

print('Put some skill that you are not familiar with')
unfamiliar_skill=input('>')
print(f'filtering out :{unfamiliar_skill}')

def find_job():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=' , headers=encabezado).text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index ,job in enumerate(jobs):
        time_for=job.find('span',class_='sim-posted').text 
        if 'few' in time_for:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','') 
            skills=job.find('span',class_='srp-skills').text.replace(' ','') 
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                #create your folder 'posts' for yourself
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'''
                    company name: {company_name.strip()} \n
                    skills :{skills.strip()}\n
                    info:{more_info.strip()}\n
                    ''')
                    #other format of see en .txt
                    """
                    f.write(f"company name: {company_name.strip()} \n")
                    f.write(f"skills :{skills.strip()} \n")
                    f.write(f"info:{more_info.strip()} \n")
                    """
                print(f'File saved: {index}')

if __name__ =='__main__':
    while True:
        find_job()
        