import pyperclip
from pynput.keyboard import Key, Controller
keyboard = Controller()
import requests
import time


def auto_1(timer):

    try:
        data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
        # 按F2
        keyboard.type("")
        keyboard.type(data["F2"])
        time.sleep(timer)
        #两次tab
        keyboard.press(Key.tab)
        time.sleep(timer)
        keyboard.press(Key.tab)
        time.sleep(timer)

        # 两次tab
        keyboard.press(Key.tab)
        time.sleep(timer)
        keyboard.press(Key.tab)
        time.sleep(timer)

        # 全选删除
        with keyboard.pressed(Key.ctrl_l):
            keyboard.press('a')
            keyboard.release('a')
        time.sleep(timer)
        keyboard.press(Key.delete)
        time.sleep(timer)
        # 按F3
        keyboard.type(data["F3"])
        time.sleep(timer)
        # 2次tab
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(timer)
        keyboard.press(Key.tab)
        time.sleep(timer)
        # 删除
        with keyboard.pressed(Key.ctrl_l):
            keyboard.press('a')
            keyboard.release('a')
        time.sleep(timer)
        keyboard.press(Key.delete)
        time.sleep(timer)
        # 按F4
        keyboard.type(data["F4"])
        time.sleep(timer)
        # 3次tab
        keyboard.press(Key.tab)
        time.sleep(timer)

        keyboard.type(data["left"])
        time.sleep(timer)
        keyboard.press(Key.tab)
        time.sleep(timer)
        keyboard.press(Key.tab)
        time.sleep(timer)
        keyboard.type("")
        keyboard.type(data["F5"])
        time.sleep(timer)
    except Exception as e:
        print(e,'error')
        pass
