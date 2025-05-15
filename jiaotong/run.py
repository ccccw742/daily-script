# import requests

# url = "https://creditcardapp.bankcomm.com/pacpAccusTaskcenterWeb/task/awrd"

# headers = {
#     "Host": "creditcardapp.bankcomm.com",
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "X-Tingyun": "c=B|P54-bRBPcGU;x=67090cad75a54ee8;u=base64#MTA2NjkzODA4Mg==",
#     "X-Requested-With": "XMLHttpRequest",
#     "Sec-Fetch-Site": "same-origin",
#     "Accept-Language": "zh-CN,zh-Hans;q=0.9",
#     "Sec-Fetch-Mode": "cors",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Origin": "https://creditcardapp.bankcomm.com",
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148com.bankcomm.maidanba.V2;mapp_saoma;isApplePayUsable;paypinflag;newVCard;digitalcert;WKWebView;UnionPay/1.0 BoComMDB;buildVersion264;mdbTitleBar;",
#     "Referer": "https://creditcardapp.bankcomm.com/pacpAccusTaskcenterWeb/ddySgn/index?channel=00",
#     "Cookie": "JSESSIONID=0D8F3A7DCFBAC4B30B250C9F6124B2A2"
# }

# data = {
#     "token": "2576CBAC8FCE8C90FD5FB1B01E0876DA",
#     "taskId": "20250429092312000001",
#     "channel": "00"
# }

# try:
#     response = requests.post(url, headers=headers, data=data)
#     print(response.text)
#     response.raise_for_status()
    
#     if response.headers.get("Content-Encoding") == "gzip":
#         result = response.json()
#     else:
#         result = response.json()
    
#     if result.get("returnCode") == "000000":
#         print("请求成功！")
#         print(f"奖励名称: {result['prizeNm']}")
#         print(f"图片地址: {result['prizeImgUrl']}")
#         print(f"UUID: {result['uuid']}")
#         print(f"新Token: {result['token']}")
#     else:
#         print(f"请求失败，代码: {result.get('returnCode')}")
#         print(f"失败信息: {result.get('returnMsg')}")

# except Exception as e:
#     print(f"请求发生错误: {e}")





import requests

cookies = {
    '_tcs': '33d3c82b-206b-4ae2-87da-3425e7d1468d',
    'x-s3-sid': '>td61P1gd0/bmsjJ2B1643301',
    'loginType': 'mobile',
    'GeeTestUser': '103d0ae2ecbccf875164584d49aeefaf',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,az;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://creditcardapp.bankcomm.com',
    'Pragma': 'no-cache',
    'Referer': 'https://creditcardapp.bankcomm.com/idm/sso/login.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': '_tcs=33d3c82b-206b-4ae2-87da-3425e7d1468d; x-s3-sid=>td61P1gd0/bmsjJ2B1643301; loginType=mobile; GeeTestUser=103d0ae2ecbccf875164584d49aeefaf',
}

data = 'TLDFZTVbK6TTJJ9p8Qei379LWHtkgWx28QgMWvTHQpfzArxQgaI3sIsdwZD+n1/OnlzcBPEFjNPxyDobvoPYpSItukTnyDOx9yJcmGCBcIbDdndHuVPvfqy7+bMm9SDy/n5cw4BRDsIA0WFrNV28kQ==0ef749f8691dade4b837d01645c09c6e189362673795d1a495cd77cce99f73cd08ec0394a6e1ae752f8d536afdc32db29df974668b422b571ee75ac94f8f7893794dabd37743b0e380d9837c312181eb486bd01c5b0c4dd5c48108495df6e7a67dae38250497e44a9355fb8f6ca4ed0f046412e4a838b916542b3d2939218711'

response = requests.post('https://creditcardapp.bankcomm.com/ismsIbvmIbvpWeb/get.php', cookies=cookies, headers=headers, data=data)
print(response.text)