from ronglian_sms_sdk import SmsSDK
import random


accId = '8aaf0708806f236e0180786cc7310208'
accToken = '6f272100c8d44473ad1797467b426cf9'
appId = '8aaf0708806f236e0180786cc834020f'

num = random.randint(1000, 9999)

def send_message(mobile):
    sdk = SmsSDK(accId, accToken, appId)
    tid = 1
    datas = (num, 5)
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)


# send_message(mobile='13332246270')
