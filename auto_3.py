from pynput.keyboard import Key, Controller
keyboard = Controller()
import requests
import time


def auto_3(timer):
    data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
    keyboard.type("")
    keyboard.type(data["F2"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.type(data["F4"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.type(data["F5"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)
    keyboard.type(data["F1"])
    time.sleep(timer)
   