import requests
import threading
from hashlib import md5 as md5Encode

# 任务数和线程数
tasks_num = 1 # 运行 100 次
threads_num = 1 # 最大线程数 30 个

ticket ='0uQBaOVAyaOdG3CUyZ3wLYE9OQdlm7oULFZB7z2kaAA0zTluAzEMQNG7_JoYiJIoUmzT5w5ZJkujAAlSDebuhm34Au8drELStrIVhKWkCquSWrVZCKuRzTRsjNAYHkNYnVTv3WuZtQrLSJ6eEV5IEF5Jm6FtqFt4uLrwTk5hJw_-fv5_3_bHcQofV6-N2fvN-yRRmxG9qLkhfN3db7KclwAAAP__'

headers = {
    "ticket": ticket,
    'Host': 'energy.xiaojukeji.com',
    'User-Agent': 'iPhone16,1(iOS/17.5.1) DiDiApp(XJCD4iOS/1.6.1) Weex/0.30.0 ExternalUA 1179x2556',
    'Content-type': 'application/json;charset=UTF-8',
    'wsgsig': 'dd04-/qN3Iwj5VDdpex4Bnf87threzw53PBf2N+60Pd5tm8QVARdSaMfvi8ZbATXuMzvPtO4zY8MXA7X2myHb5vKv1tGo9BkZTD1e5gSUFsfv6BAmcd+8ynzxWsWGBBgwQj0h3Jw1Z+QoBTqT+/Ld3O1qZAGtAN20bSWS'
}

body = {
  "source": "1323124385",
  "ticket": ticket,
  "token": ticket,
  "tokenId": ticket,
  "cityId": "5",
  "excitationId": "144115195993789098"
}

def exchange():
    try:
        url = 'https://energy.xiaojukeji.com/am/marketing/api/member/charge/activity/sign/doSign'
        res = requests.post(url, headers=headers, json=body)
        print(f'任务开始: {res.text}')
    except Exception as e:
        print(f'任务失败: {e}')
def threading_run(tasks,threads):
    for i in range(tasks):
        if threading.active_count() < threads + 1 and tasks != 0:
            t = threading.Thread(target=exchange)
            t.start()
            tasks -= 1
            if threading.active_count() == threads + 1:
                while threading.active_count() == threads + 1:
                    pass
                while threading.active_count() != 1:
                    pass
def start_task():
    threading_run(tasks_num, threads_num)
if __name__ == '__main__':
    # 手动执行任务
    start_task()