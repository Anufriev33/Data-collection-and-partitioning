import scrapy


class FootbalSpider(scrapy.Spider):
    name = "footbal"
    allowed_domains = ["bombardir.ru"]
    start_urls = ["https://bombardir.ru/england/table"]

    
    

    def parse(self, response):
        for team in response.xpath('//*[@id="main-tab"]//table//tbody//tr'):
            #lebel = team.xpath('.//td[3]//span[1]//img').get(),
            name = team.xpath('.//td[3]//span[2]//a//text()').get(),
            game = team.xpath('.//td[4]//text()').get(),
            win =team.xpath('.//td[5]//text()').get(),
            glasses = team.xpath('.//td[10]//text()').get(),
            
            if name and glasses and game and win:
                yield {
                    #'Эмблема' : lebel,
                    'Команда' : name,
                    'Количество Игр' : game,
                    'Выигранные матчи' : win,
                    'Очки' : glasses
                }
                    
