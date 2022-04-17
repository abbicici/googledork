import scrapy
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings

inputt=input("What will you search:")

class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['www.google.com']
    
    start_urls = [f'https://www.google.com/search?q=site:anonfiles.com+{inputt}&start=10',
                f'https://www.google.com/search?q=site:dosya.co+{inputt}&start=10',
                f'https://www.google.com/search?q=site:t.me+{inputt}&start=10'
                ]

    def parse(self, response):
        for i in response.xpath("//div[@class='ZINbbc xpd O9g5cc uUPGi']"):
            yield{
                "baslik":i.xpath(".//div[@class='BNeawe vvjwJb AP7Wnd']/text()").get(),
                "url":i.xpath(".//div[@class='kCrYT']/a/@href").get(),
                "tarih":i.xpath(".//span[@class='xUrNXd UMOHqf']/text()").get()
            }
        next_page2=response.xpath("//a[@class='nBDE1b G5eFlf'][contains(@style,'text-align:left')]/@href").get()
        before_page=response.xpath("//a[@class='nBDE1b G5eFlf'][contains(@style,'text-align:right')]/@href").get()
        
        if before_page:
            before_href = before_page
            before_page_url = 'http://www.google.com' + before_href
            request = scrapy.Request(url=before_page_url)
            yield request
        
        if next_page2:
            next_href = next_page2
            next_page_url = 'http://www.google.com' + next_href
            request = scrapy.Request(url=next_page_url)
            yield request



s = get_project_settings()
s['FEED_FORMAT'] = 'json'
s['LOG_LEVEL'] = 'INFO'
s['FEED_URI'] = 'result.json'
s['LOG_FILE'] = 'Q1.log'
s['FEED_EXPORT_ENCODING'] = 'utf-8'
process = CrawlerProcess(s)
process.crawl(GoogleSpider)
process.start()

# VEYA AŞŞAĞIDAKİ PROCESS KULLANILABİLİR WİNDOWS'TA ÇALIŞMADI ANCAK LİNUXTA ÇALIŞTI



#process = CrawlerProcess(get_project_settings())
#process.crawl(GoogleSpider)
#process.start()

