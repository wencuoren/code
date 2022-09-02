import requests

headers = {
    'Host': 'capi.wewillpro.com',
    'Connection': 'keep-alive',
    # 'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi K30 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 WillGo/2.7.8',
    # 'Origin': 'https://h5.wewillpro.com',
    # 'X-Requested-With': 'com.ruidonghy.will',
    # 'Sec-Fetch-Site': 'same-site',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Dest': 'empty',
    # # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = {
    'activity_id': '119',
    'company_id': '45110',
    'token': 'UWZUZwIyB2FSM11gWmdSfVA4VWsIZQRiVWxTZVBhAWkGM1No',
}

r = requests.get('https://capi.wewillpro.com/map_activity/get_info', params=params, headers=headers)
rr =r.json()
rr = rr['data']
rr = rr['map_info']
rr = rr['grid_list']

print (rr)

for i in rr:
    for key,valut in i.items():
        if key == "extra" :
            print(valut['title'])

            da = valut['option']
            for item in da:
                for k,v in item.items():
                    if k == 'option':
                    
                    # if (k,v)!=('answer',2) and k=='option' :
                        # if (k,v)==('answer',1):
                        li = (k,v)
                        print(k,v)
                    elif (k,v)==('answer',1):
                        print(k,v)
            # print(da)
            print("-"*90)



        # if key == "playCount" and (key,valut) == ("title","昭运电台"):
        #     print(key,valut)