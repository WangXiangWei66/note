#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import requests
import sys,io
import json
import jmespath
url='https://mapi.vip.com/vips-mobile/rest/content/reputation/queryBySpuId_for_pc?app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101103101&client=pc&mobile_platform=1&province_id=101103&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=289567902&mars_cid=1614176790770_4d585139090f2070afe4ad1c5dcf7f78&wap_consumer=c&spuId=795243796572786688&brandId=1710615683&page=1&pageSize=10&timestamp=1624628502000&keyWordNlp=%E5%85%A8%E9%83%A8-%E6%8C%89%E9%BB%98%E8%AE%A4%E6%8E%92%E5%BA%8F&_=1624628490788'
headers={
'cookie': 'mars_pid=0; vip_first_visitor=1; vip_address=%257B%2522pid%2522%253A%2522101103%2522%252C%2522cid%2522%253A%2522101103101%2522%252C%2522pname%2522%253A%2522%255Cu6cb3%255Cu5317%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu77f3%255Cu5bb6%255Cu5e84%255Cu5e02%2522%257D; vip_province=101103; vip_province_name=%E6%B2%B3%E5%8C%97%E7%9C%81; vip_city_name=%E7%9F%B3%E5%AE%B6%E5%BA%84%E5%B8%82; vip_city_code=101103101; vip_wh=VIP_BJ; vip_ipver=31; VIP_QR_FIRST=1; vip_cps_cuid=CU162462831081341337e62567a50607; vip_cps_cid=1624628310816_7aa8d9fdda9bb4b88ef277b3d89378b0; cps_share=cps_share; cps=adp%3AC01V0000jr2uzug2%3A%40_%401624628310815%3Amig_code%3A%3Aac01tii67vx5cqlbmx17mz4g0m58co9u; PAPVisitorId=b0c7901efe42f675f02d93dadc539be9; vip_new_old_user=1; mars_sid=b8e21c206840b0651623db3ee2a1d704; PHPSESSID=hjlufojcnvsktc7letalg4c746; visit_id=3A8A926EF16219E850D69CCBD531F82D; vip_access_times=%7B%22list%22%3A4%2C%22detail%22%3A0%7D; vipshop_passport_src=https%3A%2F%2Fdetail.vip.com%2F; PASSPORT_ACCESS_TOKEN=FF32B90D3919B968F1790EAFA9817179A7A47920; VipRUID=289567902; VipUID=4f1cd0d06eb534c793bf8cf5b270432f; VipRNAME=186*****736; VipLID=0%7C1624628423%7C77e292; VipDegree=D1; user_class=c; VipUINFO=luc%3Ac%7Csuc%3Ac%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3102; VipCI_te=; vip_tracker_source_from=; pg_session_no=12; waitlist=%7B%22pollingId%22%3A%22C89FD91B-25A2-4F8D-8D9A-65B28B80BAAD%22%2C%22pollingStamp%22%3A1624628501531%7D; mars_cid=1614176790770_4d585139090f2070afe4ad1c5dcf7f78',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
'referer': 'https://detail.vip.com/'
}
# 发送请求
resp=requests.get(url,headers=headers)

# 响应结果乱码，解决方案
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
#print(resp.text)
#由字符串转成字典
d=json.loads(resp.text)
# 第三方模块
content=jmespath.search('data[0].reputation.content',d)
print(content)

# 如果不使用第三方模块
print(d['data'][0]['reputation']['content'])
print(d.get('data')[0].get('reputation').get('content'))