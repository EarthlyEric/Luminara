# -*- coding: UTF-8 -*-
import random

from discord.enums import UserFlags

def showinfo(tip, info):
    print("{}:{}".format(tip,info))


def randomimgall():
    num=random.randint(1, 73)

    baseurl="https://raw.githubusercontent.com/EarthlyEric/Alice-RES/master/image/Alice-icon-"

    url=f"{baseurl}{num}.png"

    return url

def randomimgnsfw():
    num=random.randint(0,0)