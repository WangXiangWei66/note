import requests
import re

headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
'Cookie': 'BIDUPSID=CDDF8B16182289FE0BDBD698D033E5F0; PSTM=1637564947; BAIDUID=CDDF8B16182289FECA60BF876579869C:FG=1; __yjs_duid=1_94dd714c978093ae0f093ac0b7882a6a1637571067466; MCITY=-340%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=35104_35631_35456_34584_35490_35698_35246_34812_35644_35318_26350_35474_35562; delPer=0; PSINO=6; BAIDUID_BFESS=CDDF8B16182289FECA60BF876579869C:FG=1; log_guid=eeaf4a14cdd93ff09255b6199aaff670; ZX_UNIQ_UID=a73a549cb60e5a87d860b16e4d690898; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1641458626; _j47_ka8_=57; BA_HECTOR=alal80840l0g00ahlc1gtdcia0q; BCLID=7623202212547193484; BDSFRCVID=ft_OJeC62l07libHcZRyMH3dfg5rbsOTH6ao-nFQfPqrimqguPwkEG0PHf8g0Ku-S2EqogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI0aJDvDqTrP-trf5DCShUFsa6ciB2Q-XPoO3KtMDhOny-bWjM0IyabbKtbiW5cpoMbgylRM8P3y0bb2DUA1y4vpKhbBt2TxoUJ2abjne-53qtnWeMLebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD5thj6PVKgTa54cbb4o2WbCQHlRU8pcN2b5oQTO3h-bqBPJO3HRuaIOe5J3vOPQKDpOUWfAkXpJvQnJjt2JxaqRC5M38hp5jDh3MhP_1bhode4ROfgTy0hvctb3cShPm0MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT-tJJ3aQ5rtKRTffjrnhPF3yt0PXP6-hnjy3b4JWpOJWnOWsxJEy5bfb4-UypjpJh3RymJJ2-39LPO2hpRjyxv4bp-qDPoxJpOJaK6x0P57HR7Wbh5vbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK_XfC-KhCDrMRoqM4FHqxbXqMJUfgOZ0l8Ktt5-qb7s5x7j2-0ieaQqQtbLBaIH3xomWIQHDP55Kprj05FAhN_H0x59-ej4KKJxW-PWeIJo5t5Wjbt8hUJiB5JMBan7_UJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbCDRe5L5jjjM5pJfeJOK5InQ04Jq5nbSejrvK4t_-P6MblOdWMT-0bFHWIt5anTDObOL0RrYy5tObxttbtjeBan7_JjOHRrPVJQMKJ5EhJ_s5J3faMQxtNR70DnjtpvhKf84QJQobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DLlj55P; BCLID_BFESS=7623202212547193484; BDSFRCVID_BFESS=ft_OJeC62l07libHcZRyMH3dfg5rbsOTH6ao-nFQfPqrimqguPwkEG0PHf8g0Ku-S2EqogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oI0aJDvDqTrP-trf5DCShUFsa6ciB2Q-XPoO3KtMDhOny-bWjM0IyabbKtbiW5cpoMbgylRM8P3y0bb2DUA1y4vpKhbBt2TxoUJ2abjne-53qtnWeMLebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD5thj6PVKgTa54cbb4o2WbCQHlRU8pcN2b5oQTO3h-bqBPJO3HRuaIOe5J3vOPQKDpOUWfAkXpJvQnJjt2JxaqRC5M38hp5jDh3MhP_1bhode4ROfgTy0hvctb3cShPm0MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT-tJJ3aQ5rtKRTffjrnhPF3yt0PXP6-hnjy3b4JWpOJWnOWsxJEy5bfb4-UypjpJh3RymJJ2-39LPO2hpRjyxv4bp-qDPoxJpOJaK6x0P57HR7Wbh5vbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK_XfC-KhCDrMRoqM4FHqxbXqMJUfgOZ0l8Ktt5-qb7s5x7j2-0ieaQqQtbLBaIH3xomWIQHDP55Kprj05FAhN_H0x59-ej4KKJxW-PWeIJo5t5Wjbt8hUJiB5JMBan7_UJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbCDRe5L5jjjM5pJfeJOK5InQ04Jq5nbSejrvK4t_-P6MblOdWMT-0bFHWIt5anTDObOL0RrYy5tObxttbtjeBan7_JjOHRrPVJQMKJ5EhJ_s5J3faMQxtNR70DnjtpvhKf84QJQobUPUDUJ9LUkJLgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DLlj55P; _fb537_=xlTM-TogKuTwMEfNN9YBvpCezYTkkgBEIBSlx1Nc-SnBmd; ZX_HISTORY=%5B%7B%22visittime%22%3A%222022-01-06+17%3A14%3A09%22%2C%22pid%22%3A%22xlTM-TogKuTwb1CZ-CeOcTdNkKluIH0L%2AQmd%22%7D%5D; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1641460451; ab_sr=1.0.1_YWU5ZWY1Nzk0ODQxMmZiZGExMzBhZDRkYTA0NDFkZWVjMjZlMTgyYTQ4MzMyZmI3YTEzZjdiNGM2ODE4YTJkMTZlNGI1ZGUwZGYyNTIyMjU0ZjkxNDUzNjhmMjA3Y2YyNzJiNzIxYTAyM2ViNTg5NTI4OGJmNDBmZjEzYWM4NGRjYjZjZWIyZDZhYjVlNTY1OTJjYmU4ODQ0NDJiOGFmYw==; _s53_d91_=e27d644896d1800d6f2981fcb981e321adea0c9c207d962fd7fd1650b06e7c64d352812de00d5ecddceb68e28b0a04371ac1acc065c2edcd6a20c956c34515d0cab06f9df47a2c3506816d3e3abc37ff0e5d506e1d62a9ec37ae3a3d03f92030ad3b90e94ef1b137a8c499a796df5b6962e2de09c8f91855beeb0ff9334d710001e58b99c498f95bae1fa7c6136474c26faf21f973ec61c6abb3339b811160e2438f1066113f81bb2581a5a64339e9ce37682ccd3d9ed8659e7c326df9031938034362cf1a5dd3213f960086357db4db; _y18_s21_=e0907032; RT="z=1&dm=baidu.com&si=fzecqjr5tus&ss=ky2q3947&sl=j&tt=qtm&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=12zfv&ul=13mc5"',
'Host': 'aiqicha.baidu.com',
'Pragma': 'no-cache',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

#url = 'https://aiqicha.baidu.com/company_detail_31889532487718'
url='https://aiqicha.baidu.com/company_detail_99169412051313?t=0'
data = requests.get(url=url,headers=headers)
data.encoding = 'UTF-8'

##print(data.text)

re_data = 'window.pageData = {(.*?)};'
html_data = re.findall(re_data,data.text,re.S)
html_data = ''.join(html_data)
##print(html_data)

personTitle = re.findall('"legalPerson":"(.*?)",',html_data,re.S)[0]
legalPerson = re.findall('"personTitle":"(.*?)",',html_data,re.S)[0]
startDate = re.findall('"startDate":"(.*?)",',html_data,re.S)[0]
regCapital = re.findall('"regCapital":"(.*?)",',html_data,re.S)[0]
unifiedCode = re.findall('"unifiedCode":"(.*?)",',html_data,re.S)[0]
regAddrDetail = re.findall('"regAddrDetail":{(.*?)},',html_data,re.S)
phone = re.findall('"phone":"(.*?)",',html_data,re.S)[0]
email = re.findall('"email":"(.*?)",',html_data,re.S)[0]
website = re.findall('"website":"(.*?)",',html_data,re.S)[0]
describe = re.findall('"describe":"(.*?)",',html_data,re.S)[0]


print('------------------------------------------------------')

print(personTitle.encode('utf8').decode('unicode_escape'))
print(startDate.encode('utf8').decode('unicode_escape'))
print(regCapital.encode('utf8').decode('unicode_escape'))
print(unifiedCode.encode('utf8').decode('unicode_escape'))
print(phone.encode('utf8').decode('unicode_escape'))
print(email.encode('utf8').decode('unicode_escape'))
print(website.encode('utf8').decode('unicode_escape'))
print(regAddrDetail)  #### 这个给的是给经纬度的 ,没有给实际地址
print(describe.encode('utf8').decode('unicode_escape'))  # 实际地址可从详细信息里获取



