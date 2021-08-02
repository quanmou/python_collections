import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    # start_urls = ['http://itcast.cn/']
    start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)

    def parse(self, response):
        # 保存页面的html内容
        # filename = "teacher.html"
        # with open(filename, "w") as f:
        #     f.write(response.body.decode())

        # 获取网站标题
        context = response.xpath('/html/head/title/text()')

        # 提取网站标题
        title = context.extract_first()
        print(title)
