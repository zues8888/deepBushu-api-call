import requests
import random
import os

# Server酱配置
SERVER_CHAN_KEY = os.getenv('SERVER_CHAN_KEY', 'SCT276475TOx1Q2zTNuIWKEkcNNyRBiWOq')  # 从环境变量获取Server酱的key

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://yd.gaojiniu.cn',
    'priority': 'u=1, i',
    'referer': 'https://yd.gaojiniu.cn/',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.2.380',
}

step_value = random.randint(30000, 35000)
params = {
    'user': '15197266646',
    'password': 'shuge0517',
    'step': str(step_value),
}

print(f'生成的步数: {step_value}')
response = requests.get('https://api.leafone.cn/api/misport', params=params, headers=headers)
print(f'接口调用状态码: {response.status_code}')
print(f'接口返回内容: {response.text}')

# 发送微信通知
def send_wechat_notification(title, desp):
    if not SERVER_CHAN_KEY:
        print('未设置Server酱key，跳过微信通知')
        return
    
    server_chan_url = f'https://sctapi.ftqq.com/{SERVER_CHAN_KEY}.send'
    notification_data = {
        'title': title,
        'desp': desp
    }
    try:
        notify_response = requests.post(server_chan_url, data=notification_data)
        print(f'微信通知发送状态码: {notify_response.status_code}')
        print(f'微信通知返回内容: {notify_response.text}')
    except Exception as e:
        print(f'发送微信通知失败: {str(e)}')

# 发送步数更新结果通知
title = f'步数{step_value}\n 状态:{response.status_code}'
desp = f'步数更新: {step_value}\n状态码: {response.status_code}\n返回内容: {response.text}'
send_wechat_notification(title, desp)