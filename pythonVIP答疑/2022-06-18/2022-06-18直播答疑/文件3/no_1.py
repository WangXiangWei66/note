import requests
import re

'''
            <!--图-->
            <div class="image">
                <a target="_blank" href="http://finance.eastmoney.com/a/202206142412311033.html">
                    <img src="//dfscdn.dfcfw.com/download/D25094984650326653414_w210h154.jpg">
                </a>
            </div>
        <!--文-->
        <div class="text">
            <p class="title">
                <a href="http://finance.eastmoney.com/a/202206142412311033.html" target="_blank">
                    龙虎榜：6.54亿抢筹长安汽车 外资净买3股 机构净买20股
                </a>
            </p>

                <p class="info" title="6月14日，三大指数先抑后扬，截止收盘，沪指涨1.02%，报收3288点；深成指涨0.2%，报收12023点；创业板指涨0.07%，报收2548点。板块方面，证券、汽车整车、石油等板块涨幅居前，半导体、航天航空、教育等板块跌幅居前。龙虎榜净流入TOP206月14日，上榜龙虎榜个股中，资金净流入最多的是长安汽车，三日净流入6.54亿元。">
                    6月14日，三大指数先抑后扬，截止收盘，沪指涨1.02%，报收3288点；深成指涨0.2%，报收12023点；创业板指涨0.07%，报收2548点。板块方面，证...
                </p>
            <p class="time">
                06月14日 17:56
            </p>
        </div>
        <!--分享-->
        <!--
        <div class="share">
            <span class="shareIco"></span>
            <div class="shareContent">
                <div id='bdshare' class="bdshare_t bds_tools get-codes-bdshare" data="{'url':'http://finance.eastmoney.com/a/202206142412311033.html',text:'龙虎榜：6.54亿抢筹长安汽车 外资净买3股 机构净买20股'}">
                    <a class="bds_iguba" title="分享到股吧"></a>
                    <a class="bds_tsina" title="分享到新浪微博"></a>
                    <a class="bds_qzone" title="分享到QQ空间"></a>
                    <a class="bds_tqq" title="分享到腾讯微博"></a>
                </div>
            </div>
        </div>
        -->
    '''
def getHTMLtext(url):
    """请求获得网页内容"""
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        res = r.text
        print("成功访问")
        return res
    except:
        print("访问错误")
        return " "

url = 'https://stock.eastmoney.com/a/cscsj.html'
html = getHTMLtext(url)
print(html)
#开始爬取数据

    # 这个是我自己打的，如何分开爬取链接和文本？？还有除掉获取的数据中的\r和\n
    #data = re.compile(f'<li id="newsTr{i}">.*?src="(.*?)".*?>.*?title"(.*?)</p>',re.S)

#下面这个是老师帮忙改的正则表达式看不懂，理解不了
data = re.compile(f'get-codes-bdshare" data=.*?:(.*?),text:(.*?)"', re.S)

items = re.findall(data,html)
#print(items)
for item in items:
        dict = {
            'link' : item[0],
            'title' : item[1],

        }
        print(dict)


