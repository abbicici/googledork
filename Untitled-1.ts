

paket=response.xpath("//*[@class='ZINbbc xpd O9g5cc uUPGi']") 

baslik=product[1].xpath("//div[@class='BNeawe vvjwJb AP7Wnd']/text()").get()

url=product[1].xpath("//div[@class='kCrYT']/a/@href").get()

 tarih=product[1].xpath("//span[@class='xUrNXd UMOHqf']/text()").get()


        for paket in response.xpath("//div[@class='ZINbbc xpd O9g5cc uUPGi']"):
            yield{
                "baslik":paket.xpath(".//div[@class='BNeawe vvjwJb AP7Wnd']/text()").get(),
                "url":paket.xpath(".//div[@class='kCrYT']/a/@href").get(),
                "tarih":paket.xpath(".//span[@class='xUrNXd UMOHqf']/text()").get()
            }
