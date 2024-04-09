import base64
import json
import io

from typing import Optional
from aiohttp import ClientSession

from core.config import config

class WizModel:
    def __init__(self) -> None:
        self.api_key = config.WIZMODEL_APIKEY
        self.url = "https://api.wizmodel.com/sdapi/v1/txt2img"
        self.header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.api_key
        }

    @classmethod
    async def text2image(cls, prompt: str, steps: Optional[int]) -> dict:
        if steps is None:
            steps = 100
        payload = json.dumps({
            "prompt": prompt,
            "steps": steps
        })

        async with ClientSession(headers=cls().header) as session:
            async with session.post(url=cls().url, data=payload) as response:
                image_codes = await response.json()
                image = io.BytesIO(base64.b64decode(image_codes['images'][0]))

                return image



