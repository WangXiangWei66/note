import requests
import parsel
import time


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',}
def parse(new_url):
    html_data = requests.get(url=new_url,headers=headers,timeout=30).text  ### 解析数据
    #print(html_data)
    sel = parsel.Selector(html_data)    ### 转parsel 对象
    lis = sel.css('.nl_con>ul>li')
    before_list = []

    for li in lis:
        time.sleep(1)
        time.sleep(0.5)
        prodect_id = li.css('.nlcd_name a::text').get()
        if prodect_id:
            prodect_id = prodect_id.strip()
        sale = li.css('.fangyuan span::text').get()
        if sale:
            sale = sale.strip()
        print(prodect_id,sale)

        before_list.append([prodect_id,sale])

    next_page = sel.xpath("//a[@class='next'][contains(text(), '下一页')]/@href").get()  ##获取下一页链接
    # print(next_page)
    ### 如果有下一页 就构建 url 继续执行 解析数据，然后继续拿到下一页的链接
    if next_page:
        next_url = 'https://aj.newhouse.fang.com' +next_page   ## 构建url
        print(next_url)

        print(next_page)
        parse(next_url)
    return before_list