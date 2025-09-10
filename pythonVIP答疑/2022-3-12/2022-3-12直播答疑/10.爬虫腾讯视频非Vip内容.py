# coding:utf-8
# author:杨淑娟
import requests
url='https://apd-225fb905395fadf335417ac9d10f33c5.v.smtcdns.com/moviets.tc.qq.com/Axu3kIoV0tj1aErkSLYfErbun3jaKBaCupvi-2img9n4/uwMROfz2r5zCIaQXGdGnC2df644Q3LWUuLvyGY4RMhgE_3T2/hbfpNwXajEcDRlHXU-GOmth0pP2kWt7TR4Gfxp42rTZ8l7whsoE3GU_3XIgfl2HVGnE3aggJiRPjhesD44GNCyRZ_e5O75UHaBkqpoJod4t3wb1zZ_ky0flfTfdfj-4m4Q6v5zwsbJYD98CWbVEae_Kziuuq_gYv0mhlszRhaqMm7zCVb0aJIQ/09_a0020wq0taz.321002.1.ts?index=9&start=94760&end=102640&brs=8134948&bre=8731471&ver=4&token=2130708def4b6ec3c618bb355d8496e6'

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
resp=requests.get(url,headers=headers)

with open('a.mp4','wb') as file:
    file.write(resp.content)
