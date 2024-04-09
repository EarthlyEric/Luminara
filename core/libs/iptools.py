# -*- coding: UTF-8 -*-
import asyncio
import platform
from aiohttp import ClientSession

from core.config import config

class Response():
    def __init__(self, response) -> None:
        self.ip = response["ip"]
        self.city = response["city"]
        self.region = response["region"]
        self.country = response["country"]
        self.loc = response["loc"]
        self.org = response["org"]
        self.timezone = response["timezone"]

class iptools():
    def __init__(self) -> None:
        self.ipinfo_apikey = config.IPINFO_APIKEY
        self.base_url = "https://ipinfo.io"
        
    @classmethod
    async def get_ipinfo(cls, ip:str):
        async with ClientSession() as session:
            async with session.get(url=f"{cls().base_url}/{ip}?token={cls().ipinfo_apikey}") as response:
                result = await response.json()
                return Response(result)