import scrapy
from ..items import ItcastItem


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
        title = context.extract_first()  # 提取网站标题
        print(title)

        # 提取教师信息
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

        # 直接返回最后数据
        return items
