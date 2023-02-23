import subprocess
import time
from threading import Thread


def lavalink():
    process = subprocess.Popen(['java', "-Xmx128M", '-Xms128M', '-jar', './core/lavalink/Lavalink.jar'], stdin=subprocess.PIPE, text=True)

def init_lavalink():
    thread=Thread(target=lavalink())
    thread.run()
