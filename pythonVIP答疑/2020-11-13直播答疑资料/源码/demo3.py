# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
import  requests
from fake_useragent import  UserAgent
ua=UserAgent()

headers={'User-Agent': ua.random,
         'cookie': 'mars_pid=0; vip_address=%257B%2522pid%2522%253A%2522101101%2522%252C%2522cid%2522%253A%2522101101101%2522%252C%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522cname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%257D; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_code=101101101; vip_wh=VIP_BJ; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; mst_csrf_key=30e3d630451e7ce36514b0c7a0e85c09; user_class=a; mars_sid=7d3cb235b135f813bb76a95f920170a4; visit_id=CED73F4D350A3468120D072DE76AE3A8; vip_tracker_source_from=; pg_session_no=5; mars_cid=1590739236554_cefdddd2b0d6b6e4ba352949c1901cef',
         'referer': 'https://detail.vip.com/'}
url='https://mapi.vip.com/vips-mobile/rest/content/reputation/queryBySpuId_for_pc?callback=getCommentDataCb&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1590739236554_cefdddd2b0d6b6e4ba352949c1901cef&wap_consumer=a&spuId=1451080430681767936&brandId=1711246852&page=1&pageSize=10&timestamp=1605270866000&keyWordNlp=%E5%85%A8%E9%83%A8&_=1605270862082'
resp=requests.get(url,headers=headers)
print(resp.request.headers) #
print(resp) #　<Response [903]>  自定义的一个响应状态码，非标准响应状态码

