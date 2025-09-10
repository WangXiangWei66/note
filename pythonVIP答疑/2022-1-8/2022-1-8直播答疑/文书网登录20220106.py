# coding=UTF-8
import requests
#from fake_useragent import UserAgent
from lxml import etree
from urllib import parse
import encodings

session=requests.session()
#UserAgent().chrome
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Referer': 'https: // account.court.gov.cn / app?back_url = https % 3A % 2F % 2Faccount.court.gov.cn % 2Foauth % 2Fauthorize % 3Fresponse_type % 3Dcode % 26client_id % 3Dzgcpwsw % 26redirect_uri % 3Dhttps % 253A % 252F % 252Fwenshu.court.gov.cn % 252FCallBackController % 252FauthorizeCallBack % 26state % 3Dd54d7dd0 - b388 - 4dc8 - 8120 - 50674ffbfc4f % 26timestamp % 3D1640144274970 % 26signature % 3D7AFA224238B4C8C5FDF984ACA875DFB64877A99E6808B2846C023BFDC046F356 % 26scope % 3Duserinfo',
        'Host': 'wenshu.court.gov.cn',
        'Referer': 'https://www.baidu.com/link?url=1VLPz3Aih5revMdUxeimYfICvUlLo5eSsPSW8s9WA7BpVpzPimeah8-YqsjhkGK4&wd=&eqid=93887e2e00212c540000000261d6f6e3',
        'Upgrade-Insecure-Requests': '1'
    }
# 对首页发起请求，希望用session持续会话
def first_page():

    url='https://wenshu.court.gov.cn/'


    resp=session.get(url,headers=headers)
    # 这里能够正常返回首页的信息，带着汉字
    #print(resp.text)

# 对登录页发起post请求，
def log_page():
    log_url='https://account.court.gov.cn/api/login'
    data={
        #账号就是手机号，我就不打出来了
        'username': '156********',
        # 这里的密码使用了js加密，我还没学会怎么处理，就先把浏览器加完密的拉了过来
        'password':'hMUyq6UYv2f3aHm6MYjfV62DHyIJfKZzrLibTxGsrpI3U1pAI12r3Wdjd7I81lVek9qKji0s7Sl3r%2Ba%2B%2F2Sks1O4NQ%2B8I6MZlOOAm2YDnbaGHnsJin422IyOs0f6X159GNVdGEa3B%2BMpY%2FxF1EcMPa26r2COhnPz74O98UBEkCaTVKiKkDxP5BYY2U2sT7%2FgFxcLodsBgzsPiyO%2FM6047REUOFbdv4bVvSMRf0yDKdIHsaPbIiJ%2BekxFx193vuMdbWzbHTCl7Os%2FPEcbHFulGsnSNCxD1bxpNtC3gBn7%2FzaPwB55rjrvipqZOnFXq166ivewV4UyZupMu0AqqF1uAQ%3D%3D'
    }
    resp=session.post(log_url,headers=headers,data=data)
    # 这里虽然密码肯定不对，但是返回的resp.text完全看不懂，按道理来说应该有提示密码错误，结果一个汉字没有，我也不知道现在到哪一步了。
    print(resp.text)



if __name__ == '__main__':
    first_page()
    log_page()
