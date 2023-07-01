import subprocess
import time
from threading import Thread


def lavalink():
    process = subprocess.Popen(['java', "-Xmx256M", '-Xms128M', '-jar', './core/lavalink/Lavalink.jar'])

def init_lavalink():
    thread=Thread(target=lavalink())
    thread.run()
