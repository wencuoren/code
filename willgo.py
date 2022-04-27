import requests
import random

ru =random.randrange(20000,25000)
print(ru)

headers = {
    'User-Agent': 'okhttp/3.12.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '432',
    'Host': 'capi.wewillpro.com',
}

data = {
  'mServerStep': '0',
  'app_type': '1',
  'app_version': '2.7.7',
  'mHuaWeiStep': '0',
  'os_version': 'Android11',
  'step_count': ru,
  'sign': '94958c19e958a5f1a65bf29a8844eeeb',
  'time_zone': 'GMT 08:00',
  'mPhoneStep': '0',
  'time_str': '1650878339',
  'mTotalStep': '0',
  'data_source': '1',
  'token': 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No',
  'app_imei': '91166cacdeee13ff72fb6dbb339ff428',
  'request_time': '1650878339',
  'model': 'Redmi K30 Pro',
  'brand': 'Redmi',
  'mWechatStep': ru,
  'sport_type': '0',
  'mPhoneServerStepIncreased': '0'
}

ok = requests.post('https://capi.wewillpro.com/sport/addSportRecord', headers=headers, data=data)

headers = {
    'User-Agent': 'okhttp/3.12.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '240',
    'Host': 'capi.wewillpro.com',
}

data = {
  'app_imei': '91166cacdeee13ff72fb6dbb339ff428',
  'app_type': '1',
  'app_version': '2.7.7',
  'os_version': 'Android11',
  'sign': 'c3f7034514cbc4b22feecc420f5b2d1c',
  'model': 'Redmi K30 Pro',
  'time_str': '1650878339',
  'brand': 'Redmi',
  'token': 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No'
}

siend = requests.post('https://capi.wewillpro.com/task/getTodayTaskRewardList', headers=headers, data=data)
# print(ok.text)
# print(siend.text)

if ok.status_code and siend.status_code == 200:
    token = '99ea9fc9d39d4296b7d68815183b5d05' #在pushplus网站中可以找到
    title= 'willgo打卡成功' #改成你要的标题内容
    content = ok.text #改成你要的正文内容
    user = 'lul'
    url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content+'&template=html&topic='+user
    requests.get(url)
else:
    token = '99ea9fc9d39d4296b7d68815183b5d05' #在pushplus网站中可以找到
    title= '运行willgo打卡失败' #改成你要的标题内容
    content = ok.text #改成你要的正文内容
    user = 'lul'
    url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content+'&template=html&topic='+user
    requests.get(url)
