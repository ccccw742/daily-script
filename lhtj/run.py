import os
import json
import requests
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
import asyncio


lhtj_data= '[{\
    "cookie": "acw_tc=1a0c66d217447896005764345e011a5f760476d63d25749ac699b34b1f2158",\
    "token": "b9d78fcd984f45819974572161790fe6",\
    "x-lf-dxrisk-token":"68009c0ayCvL40AicSqWthKL2tGHUD8PZREfPcv1",\
    "x-lf-bu-code":"C20400",\
    "x-lf-channel":"C2",\
    "x-lf-dxrisk-source":"5",\
    "x-lf-usertoken":"b9d78fcd984f45819974572161790fe6"\
    }]'


# 配置日志
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class LHTJ:
    def __init__(self):
        self.ck_name = "lhtj_data"
        self.user_cookie = self.parse_cookies(lhtj_data)
        self.base_url = ""
        self.is_debug = os.getenv("IS_DEBUG", "false").lower() == "true"
        self.do_flag = {"true": "✅", "false": "⛔️"}
        self.notify_msg = []
        self.ck_status = True
        self.title = ""
        self.avatar = ""

    def parse_cookies(self,lhtj_data) -> List[Dict]:
        try:
            return json.loads(lhtj_data)
        except json.JSONDecodeError:
            logger.error("Cookie 数据解析失败")

    def debug_log(self, data: Any, label: str = "debug") -> None:
        """调试日志"""
        if self.is_debug:
            logger.info(f"\n-----------{label}-----------\n{json.dumps(data, indent=2, ensure_ascii=False)}\n")


    def double_log(self, message: str) -> None:
        """双重记录日志和通知消息"""
        logger.info(message)
        self.notify_msg.append(message)

    async def send_msg(self, message: str) -> None:
        """发送通知"""
        if message:
            # 此处可添加通知服务集成，如 Telegram、Server 酱等
            logger.info(f"通知内容：\n{message}")

    def get_datetime(self) -> str:
        """获取当前时间字符串"""
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    async def fetch(
        self, method: str, url: str, headers: Dict, data: Optional[Dict] = None
    ) -> Optional[Dict]:
        """发送 HTTP 请求"""
        try:
            full_url = self.base_url + url if url.startswith(("/", ":")) else url
            kwargs = {"headers": headers, "timeout": 10}
            if data:
                kwargs["json"] = data

            response = requests.request(method.upper(), full_url, **kwargs)
            response.raise_for_status()

            self.debug_log(response.json(), url.split("/")[-1])
            return response.json()
        except Exception as e:
            self.ck_status = False
            logger.error(f"⛔️ 请求失败: {str(e)}")
            return None

    async def signin(self, user: Dict) -> int:
        """执行签到"""
        try:
            url = "https://gw2c-hw-open.longfor.com/lmarketing-task-api-mvc-prod/openapi/task/v1/signature/clock"
            headers = {
                "cookie": user["cookie"],
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003029) NetType/4G Language/zh_CN miniProgram/wx50282644351869da",
                "token": user["token"],
                "x-lf-dxrisk-token": user["x-lf-dxrisk-token"],
                "x-gaia-api-key": "c06753f1-3e68-437d-b592-b94656ea5517",
                "x-lf-bu-code": user["x-lf-bu-code"],
                "x-lf-channel": user["x-lf-channel"],
                "origin": "https://longzhu.longfor.com",
                "referer": "https://longzhu.longfor.com/",
                "x-lf-dxrisk-source": user["x-lf-dxrisk-source"],
                "x-lf-usertoken": user["x-lf-usertoken"],
            }
            data = {"activity_no": "11111111111686241863606037740000"}
            res = await self.fetch("POST", url, headers, data)
            reward_num = (
                res.get("data", {}).get("reward_info", [{}])[0].get("reward_num", 0)
                if res and res.get("data", {}).get("is_popup") == 1
                else 0
            )
            status = (
                self.do_flag["true"]
                if res and res.get("data", {}).get("is_popup") == 1
                else self.do_flag["false"]
            )
            logger.info(
                f"{status} 每日签到: {'成功，获得' + str(reward_num) + '分' if reward_num else '今日已签到'}"
            )
            return reward_num
        except Exception as e:
            logger.error(f"⛔️ 签到失败: {str(e)}")
            return 0

    async def lottery_signin(self, user: Dict) -> None:
        """抽奖签到"""
        try:
            url = "https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/sign"
            headers = {
                "cookie": user["cookie"],
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003029) NetType/4G Language/zh_CN miniProgram/wx50282644351869da",
                "authtoken": user["token"],
                "x-lf-dxrisk-token": user["x-lf-dxrisk-token"],
                "x-gaia-api-key": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
                "bucode": user["x-lf-bu-code"],
                "channel": user["x-lf-channel"],
                "origin": "https://longzhu.longfor.com",
                "referer": "https://longzhu.longfor.com/",
                "x-lf-dxrisk-source": user["x-lf-dxrisk-source"],
                "x-lf-usertoken": user["x-lf-usertoken"],
            }
            data = {"component_no": "CX19517850Z09MCL", "activity_no": "AP25W033P1KJBXNR"}

            res = await self.fetch("POST", url, headers, data)
            status = (
                self.do_flag["true"]
                if res and res.get("code") == "0000"
                else self.do_flag["false"]
            )
            msg = (
                f"获得{res.get('data', {}).get('ticket_times', 0)}次机会"
                if res and res.get("code") == "0000"
                else res.get("message", "")
            )
            logger.info(f"{status} 抽奖签到: {msg}")
        except Exception as e:
            logger.error(f"⛔️ 抽奖签到失败: {str(e)}")

        """点击抽奖"""
        try:
            url = "https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/click"
            headers = {
                "cookie": user["cookie"],
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003029) NetType/4G Language/zh_CN miniProgram/wx50282644351869da",
                "authtoken": user["token"],
                "x-lf-dxrisk-token": user["x-lf-dxrisk-token"],
                "x-gaia-api-key": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
                "bucode": user["x-lf-bu-code"],
                "channel": user["x-lf-channel"],
                "origin": "https://longzhu.longfor.com",
                "referer": "https://longzhu.longfor.com/",
                "x-lf-dxrisk-source": user["x-lf-dxrisk-source"],
                "x-lf-usertoken": user["x-lf-usertoken"],
            }
            data = {"component_no": "CX19517850Z09MCL", "activity_no": "AP25W033P1KJBXNR", "batch_no":""}

            res = await self.fetch("POST", url, headers, data)
            status = (
                self.do_flag["true"]
                if res and res.get("code") == "0000"
                else self.do_flag["false"]
            )
            msg = (
                f"奖励类型:{res.get('data', {}).get('reward_type', 0)}"
                f"获得{res.get('data', {}).get('reward_num', 0)}个奖励"
                if res and res.get("code") == "0000"
                else res.get("message", "")
            )
            logger.info(f"{status} 点击抽奖: {msg}")
        except Exception as e:
            logger.error(f"⛔️ 点击抽奖失败: {str(e)}")

    

    async def run(self):
        """主运行逻辑"""
        if not self.user_cookie:
            logger.error("找不到可用账户")
            return

        logger.info(f"发现 {len(self.user_cookie)} 个账户\n")
        for idx, user in enumerate(self.user_cookie):
            self.notify_msg = []
            self.ck_status = True
            logger.info(f"🚀 开始处理第 {idx + 1} 个账户")

            try:
                reward_num = await self.signin(user)
                if self.ck_status:
                    await self.lottery_signin(user)
                    # 其他任务可以在此添加...

                # 示例通知消息
                self.title = f"本次运行获得 {reward_num} 积分"
            except Exception as e:
                logger.error(f"账户处理异常: {str(e)}")


if __name__ == "__main__":
    client = LHTJ()
    asyncio.run(client.run())
