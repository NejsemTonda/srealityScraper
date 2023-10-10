import scrapy

class srealitySpider(scrapy.Spider):
    name = "sreality"

    def start_requests(self):
        # get all flats from sreality api
        urls = [f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=100&page={x}" for x in range(1,6)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.json()
        flats = data["_embedded"]["estates"]
        
        # find and parse the data to JSON
        for flat in flats:
            name = flat['name']
            img = [x["href"] for x in flat["_links"]["images"]]

            yield {'name' : name, 'imgs' : img}
