from flask import Flask, render_template
from threading import Thread


app = Flask('')

@app.route('/')
def main():
  return render_template('uptime.html')

def run():
  app.run(host="0.0.0.0", port=3064)

def keep_alive():
  server = Thread(target=run)
  server.start()