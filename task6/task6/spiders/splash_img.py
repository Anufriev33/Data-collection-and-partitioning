import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SplashImgSpider(CrawlSpider):
    name = "splash_img"
    allowed_domains = ["www.unsplash.com"]
    start_urls = ["https://unsplash.com/s/photos/%D1%81%D0%BF%D0%BE%D1%80%D1%82"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@id=":r6:"]/div/div/div[1]/figure'), callback="parse_item", follow=True),
        )
    

    def parse_item(self, response):
        loader = ItemLoader(item)
        
# //*[@id=":Rslltp:"]/div/div/div[1]/figure[1]/div/div[1]/div/div/a/div/div[2]
# //*[@id=":Rslltp:"]/div/div/div[1]
# //*[@id=":Rslltp:"]/div/div/div[2]
        
        #//div[@class="MorZF"]