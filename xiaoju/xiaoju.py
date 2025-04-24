import requests
import threading
from hashlib import md5 as md5Encode

# 任务数和线程数
tasks_num = 1 # 运行 100 次
threads_num = 1 # 最大线程数 30 个

ticket ='LCcmEeOn4UtfgA5xMuA5Sdj_bWwl21BLj3C9Ddfl4IAkzDtuw0AMANG7TE0IpJYMd3mbfJTEzRqw4UrQ3Q1b1Uz1dqZStEUXRZhGmTBXKlTjtY1qYd3bGN01cxWmUyrMoED4PPNFRdfw8eHDMjNC-HlzG7Vzvz5u3xvlmtoO4Zey9PDIYSb8UVjP6Gv20RvC_8leKD2eAQAA__8='

headers = {
    "ticket": ticket,
    'Host': 'energy.xiaojukeji.com',
    'User-Agent': 'iPhone16,1(iOS/17.5.1) DiDiApp(XJCD4iOS/1.6.1) Weex/0.30.0 ExternalUA 1179x2556',
    'Content-type': 'application/json;charset=UTF-8',
    'wsgsig': 'dd04-FzthIVre11tDcCnB5e/ltPe3eS6pqUyPxj8TUF4RpLOo/GwmTlaHjI20fMW7KFnPHnMfY1TSeyVMkDUbruTb1wfjlrn6QHkergC4FvmqirCu9Pv8jgFMXZfOHNC9OFH7kneKXvltey76NYtmigMHD2fjHBgJ8s9'
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
