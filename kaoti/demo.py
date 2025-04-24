import requests
import json
import gzip

# json转 word

def get_questions(question_bank_id, page=1, page_size=50):
    url = "https://api.next.bspapp.com/client"

    headers = {
        "Host": "api.next.bspapp.com",
        "x-serverless-sign": "469c648196cae496d0a0dcf4e6e5b1bc",
        "content-type": "application/json",
        "x-basement-token": "0d4842f6-50aa-4326-a7be-e56be143495b",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.57(0x18003932) NetType/4G Language/zh_CN",
    }

    params = {
        "method": "serverless.function.runtime.invoke",
        "spaceId": "mp-0959ef53-ddf9-449b-aac9-9f3b378a36e7",
        "timestamp": 1745300330184,
        "token": "87f5e580-ed9b-4510-ae0a-5fce283b5387",
        "params": json.dumps(
            {
                "functionTarget": "DCloud-clientDB",
                "functionArgs": {
                    "command": {
                        "$db": [
                            {"$method": "collection", "$param": ["a01-questions"]},
                            {
                                "$method": "where",
                                "$param": [{"questionBankId": question_bank_id}],
                            },
                            {"$method": "skip", "$param": [(page - 1) * page_size]},
                            {"$method": "limit", "$param": [page_size]},
                            {"$method": "get", "$param": []},
                        ]
                    },
                    "clientInfo": {
                        # ...保持原有clientInfo内容
                    },
                },
            },
            ensure_ascii=False,
        ),
    }

    try:
        response = requests.post(url, headers=headers, json=params)
        print(response.text)
        response.raise_for_status()

        data = response.json()

        if data.get("success"):
            return data["data"]["data"]
        else:
            print("请求失败:", data.get("message", "未知错误"))
            return []

    except Exception as e:
        print(f"请求发生错误: {str(e)}")
        return []


# 使用示例
if __name__ == "__main__":
    # 获取第一页50条数据
    questions = get_questions("6806f58b7c8de468d1def93e", page=1, page_size=1000)

    # 保存到文件
    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"成功获取 {len(questions)} 条题目数据")
