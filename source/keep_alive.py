'''
This script is outdated, because the bot isn't hosted on replit anymore
Keeping this in case of need for future script
If you plan on using python replit, consider this script to keep it alive
'''

from flask import Flask #, render_template
from threading import Thread

# Keep the script running
# From old video
# Using free account on https://uptimerobot.com/dashboard


app = Flask('')

@app.route('/')
def home():
  return "Up"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()