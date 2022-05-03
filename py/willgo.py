import requests
import random
from time import sleep

ru =random.randrange(20000,25000)

su =1

headers = {
    'User-Agent': 'okhttp/3.12.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '432',
    'Host': 'capi.wewillpro.com',
}

data = {
  'step_count': ru,
  'sign': '94958c19e958a5f1a65bf29a8844eeeb',
  'mPhoneStep': '0',
  'mTotalStep': '0',
  'data_source': '1',
  'token': 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No',
  'app_imei': '91166cacdeee13ff72fb6dbb339ff428',
  'request_time': '1650878339',
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
  'sign': 'c3f7034514cbc4b22feecc420f5b2d1c',
  'token': 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No'
}

siend = requests.post('https://capi.wewillpro.com/task/getTodayTaskRewardList', headers=headers, data=data)
res = ok.json()
xy = res['data']
xx = xy['step']

# print(xx)
headers = {
    'User-Agent': 'okhttp/3.12.1',
    'deviceId': '91166cacdeee13ff72fb6dbb339ff428',
    'Host': 'capi.wewillpro.com',
    'Connection': 'Keep-Alive',
}

params = (
    ('app_imei', '91166cacdeee13ff72fb6dbb339ff428'),
    ('sign', 'cf4e427fe95bf864a42eaaa5f8170bd9'),
    ('token', 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No'),
)

gtm = requests.get('https://capi.wewillpro.com/gold/get_gold_info', headers=headers, params=params)

gg = gtm.json()
ggg = gg['data']
gggg = ggg['next_receive_days']


print("还有",gggg,"日大红包")

if gggg == 0:
  i = [3,7,14]
  for ii in i:  
    headers = {
        'deviceId': '91166cacdeee13ff72fb6dbb339ff428',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '264',
        'Host': 'capi.wewillpro.com',
    }

    data = {
      'app_imei': '91166cacdeee13ff72fb6dbb339ff428',
      'sign': 'e44927d0880461337ca60e4ea7e40da3',
      'days': ii,
      'token': 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No'
    }

    day = requests.post('https://capi.wewillpro.com/gold/task_receive', headers=headers, data=data)

    print(day.text)
    sleep(1)
    # 日期打卡

while su < 11:
  print (su)
  headers = {
  'User-Agent': 'okhttp/3.12.1',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Content-Length': '254',
  'Host': 'capi.wewillpro.com',
  }

  data = {
  'sign': '4906dd20ab9a1193ed203e69713d6c49',
  'id': su,
  'token': 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No'
  }

  jb = requests.post('https://capi.wewillpro.com/gold/user_gold_sign', headers=headers, data=data)

  print(jb.text)
  sleep(1)
  su += 1

res1 = jb.json()
pd = res1['code']

if pd == 200:
  yy = res1['data']
  yyy = yy['gold_num']
else:
  yyy = "请进app查看" 


if ok.status_code and siend.status_code == 200:
    token = '99ea9fc9d39d4296b7d68815183b5d05' #在pushplus网站中可以找到
    title= 'willgo打卡成功' #改成你要的标题内容
    content = '今天打卡步数：'+ str(xx) +'; 现在账号共有金额：'+ str(yyy) #改成你要的正文内容
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
