import requests

url = "https://creditcardapp.bankcomm.com/pacpAccusTaskcenterWeb/task/awrd"

headers = {
    "Host": "creditcardapp.bankcomm.com",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Tingyun": "c=B|P54-bRBPcGU;x=67090cad75a54ee8;u=base64#MTA2NjkzODA4Mg==",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Fetch-Site": "same-origin",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Sec-Fetch-Mode": "cors",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://creditcardapp.bankcomm.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148com.bankcomm.maidanba.V2;mapp_saoma;isApplePayUsable;paypinflag;newVCard;digitalcert;WKWebView;UnionPay/1.0 BoComMDB;buildVersion264;mdbTitleBar;",
    "Referer": "https://creditcardapp.bankcomm.com/pacpAccusTaskcenterWeb/ddySgn/index?channel=00",
    "Cookie": "JSESSIONID=8D7E02FCDC334C553E01096E729BE3FF"
}

data = {
    "token": "7BD0D554C30A0C803CFCE605F0D32D99",
    "taskId": "20250408095705000001",
    "channel": "00"
}

try:
    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    response.raise_for_status()
    
    if response.headers.get("Content-Encoding") == "gzip":
        result = response.json()
    else:
        result = response.json()
    
    if result.get("returnCode") == "000000":
        print("请求成功！")
        print(f"奖励名称: {result['prizeNm']}")
        print(f"图片地址: {result['prizeImgUrl']}")
        print(f"UUID: {result['uuid']}")
        print(f"新Token: {result['token']}")
    else:
        print(f"请求失败，代码: {result.get('returnCode')}")
        print(f"失败信息: {result.get('returnMsg')}")

except Exception as e:
    print(f"请求发生错误: {e}")