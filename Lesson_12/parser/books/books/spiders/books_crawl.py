import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksCrawlSpider(CrawlSpider):
    name = "books_crawl"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
    )

    def parse_item(self, response):
        item = {}
        item ["title"]= response.xpath('//div[contains(@class, "product_main")]/h1/text()').get()
        item["price"] = response.xpath('//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').get()
        # item["image"] = "http://books.toscrape.com/" + response.xpath(
        #     '//div[@id="product_gallery"]/div[@class="thumbnail"]/div[@class="carousel-inner"]/div[contains(@class, "item")]/img/@src').get()
        # item["description"] = response.xpath('//div[@id="product_description"]/../p/text()').get()
        # item["upc"] = response.xpath('//th[contains(text(), "UPC")]/../td/text').get()
        return item
# scrapy crawl books_crawl -o books.json