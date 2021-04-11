from pynput.keyboard import Key, Controller
keyboard = Controller()
import requests
import time


def auto_4(timer):
    data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]

    # 全选删除
    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(timer)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(timer)

    keyboard.type(data["F6"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)

    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(timer)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(timer)

    keyboard.type(data["F1"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)

    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(timer)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(timer)

    keyboard.type(data["F3"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)

    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(timer)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(timer)

    keyboard.type(data["F4"])
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)

    keyboard.press(Key.enter)
    time.sleep(timer)
    keyboard.press(Key.tab)
    time.sleep(timer)


    with keyboard.pressed(Key.ctrl_l):
        keyboard.press('a')
        keyboard.release('a')
    time.sleep(timer)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    time.sleep(timer)
    keyboard.type(data["F5"])