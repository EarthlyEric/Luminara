import base64
import io
from aiohttp import ClientSession

class LuminaraAPI:
    def __init__(self) -> None:
        self.base_url = "https://api.luminara.destinysoul.xyz"
        self.header = {
            'Content-Type': 'application/json',
        }
        
    class StatusDetails:
        def __init__(self, response) -> None:
            self.version = response["version"]
            
    @classmethod
    async def getStatus(cls):
        url = f"{cls().base_url}/status"
        async with ClientSession() as session:
            async with session.get(url=url, headers=cls().header) as response:
                status = await response.json()
                return cls().StatusDetails(status)
    
    @classmethod
    async def getGenerateMapImages(cls, loaction: str):
        url = f"{cls().base_url}/generateMapImages/{loaction}"
        async with ClientSession() as session:
            async with session.get(url=url, headers=cls().header) as response:
                image_codes = await response.json()
                image = io.BytesIO(base64.b64decode(image_codes["image"]))
                return image