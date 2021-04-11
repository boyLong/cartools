from pynput.keyboard import Key, Controller
keyboard = Controller()
import requests
import time


def auto_2(timer):
    data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
    keyboard.type("")
    keyboard.type(data["F7"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(timer)
    keyboard.type(data["F9"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(timer)

    keyboard.type(data["F6"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(timer)

    keyboard.type(data["F10"])
    time.sleep(timer)

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(timer)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(timer)
    keyboard.type(data["F8"])
    time.sleep(timer)