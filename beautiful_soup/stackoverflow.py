import requests
from bs4 import BeautifulSoup

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}  # for no dectect like robot
url = "https://www.stackoverflow.com/questions"

# requeriments of the server
respuesta=requests.get(url, headers=encabezado)

# parseo del arbol con beautiful soup
soup=BeautifulSoup(respuesta.text)
container_of_questions=soup.find(id="questions")
list_of_questions=container_of_questions.find_all('div',class_="s-post-summary")


for question in list_of_questions:
    titile_question=question.find('h3').text
    description_question=question.find(class_="s-post-summary--content-excerpt").text
    print(f'Titulo: {titile_question} Text: {description_question}')
