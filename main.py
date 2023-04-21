import os, sys
from RPi import GPIO
from datetime import timedelta
from flask import Flask, render_template, request
import colorama
from colorama import Fore, Back, Style

print(sys.executable)

DOOR_PIN = 11
DEFAULT_DURATION = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)

def open_door():
    GPIO.output(DOOR_PIN, 1)
    print(Fore.GREEN + "Unlocking Door...")
  
def close_door():
    GPIO.output(DOOR_PIN, 0)
    print(Fore.RED + "Locking Door...")

def open_door_for_seconds(seconds=3):
    open_door()
    time.sleep(seconds)
    close_door()

app = Flask(__name__)
app.debug = True
app.static_folder = 'statics'
app.template_folder = 'html'

@app.route('/')
def index():
    return render_template('index.html', default_duration=DEFAULT_DURATION)

@app.route('/open', methods=['POST'])
def open_door_handler():
    seconds = int(request.form.get('seconds', DEFAULT_DURATION))
    open_door_for_seconds(seconds)
    return 'Door opened for {} seconds'.format(seconds)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    GPIO.cleanup()
