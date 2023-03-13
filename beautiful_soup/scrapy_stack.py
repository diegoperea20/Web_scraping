from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader

from bs4 import BeautifulSoup


class Question(Item):
    question = Field()
    description = Field()


class StackSpider(Spider):
    name = "myFirstSpider"
    encabezado = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    }  # for no dectect like robot
    url = "https://www.stackoverflow.com/questions"

    def parse(self,response):
        sel=Selector(response)
        questions=sel.xpath('//div[@id="questions"]/div[@class="s-post-summary--content"]')
        for question in questions:
            item=ItemLoader(Question(),question)
            item.add_xpath('question','.//h3/a/text()')
            item.add_xpath('description','.//div[@class="s-post-summary--content-excerpt"]/text()')

            yield item.load_item()
# console
#scrapy runspider scrapy_stack.py -o result.json -t json