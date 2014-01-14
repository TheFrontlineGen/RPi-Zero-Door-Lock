#!/usr/bin/env python
import os, sys
from RPi import GPIO
from datetime import timedelta
import tornado.ioloop
import tornado.web
from tornado.ioloop import IOLoop

os.chdir(os.path.dirname(__file__))

DOOR_PIN = 11
DEFAULT_DURATION = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)

def open_door():
    GPIO.output(DOOR_PIN, 1)

def close_door():
    GPIO.output(DOOR_PIN, 0)

def open_door_for_seconds(seconds=3):
    open_door()
    ioloop = IOLoop.current()
    ioloop.add_callback(ioloop.add_timeout, timedelta(seconds=seconds), close_door)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', default_duration=DEFAULT_DURATION)

class OpenDoorHandler(tornado.web.RequestHandler):
    def post(self):
        seconds = int(self.get_body_argument('seconds', DEFAULT_DURATION))
        open_door_for_seconds(seconds)
        

application = tornado.web.Application(
    [
        (r"/", MainHandler),
        (r"/open", OpenDoorHandler),
    ],
    debug=True,
    static_path='statics',
    template_path='html',
)

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
    GPIO.cleanup()
