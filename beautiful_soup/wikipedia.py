import requests
from lxml import html

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}  # for no dectect like robot
url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezado)

# print(respuesta.text)

parser = html.fromstring(respuesta.text)

spanish = parser.get_element_by_id("js-link-box-es")
print(f'Forma Completa: {spanish.text_content()}')

forma_dos = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
print(f'Forma especifica: {forma_dos}')


idiomas=parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
print(f'Forma automaizada: {idiomas}')