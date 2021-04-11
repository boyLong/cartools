import PyHook3
import pythoncom
import threading
import requests
from auto_1 import auto_1
from auto_2 import auto_2
from auto_3 import auto_3
from auto_4 import auto_4
from pynput.keyboard import Key, Listener, Controller
keyboard = Controller()

try:
    with open("WaitTimer.txt","r") as w:
        timer = float(w.read().strip())

except Exception as e:
    print("出错使用0.5"+str(e))
    timer = 0.5
import os
def onKeyboardEvent(event):

    try:
        if event.Key == "F1":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F1",'')
            keyboard.type(value)
            return False
        elif event.Key == "F2":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F2",'')
            keyboard.type(value)
            return False
        elif event.Key == "F3":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F3",'')
            keyboard.type(value)
            return False
        elif event.Key == "F4":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F4",'')
            keyboard.type(value)
            return False
        elif event.Key == "F5":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F5",'')
            keyboard.type(value)
            return False
        elif event.Key == "F6":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F6",'')
            keyboard.type(value)
            return False
        elif event.Key == "F7":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F7",'')
            if value == "auto_3":
                threading.Timer(1, auto_4, (timer,)).start()
            else:
                keyboard.type(value)
            return False
        elif event.Key == "F8":
            data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
            value = data.get("F8",'')
            if value == "auto_2":
                threading.Timer(1, auto_3, (timer,)).start()
            else:
                keyboard.type(value)
            return False
        elif event.Key == "F9":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F9",'')
            keyboard.type(value)
            return False

        elif event.Key == "F10":
            value = requests.get("http://127.0.0.1:8000/get_key").json()["data"].get("F10",'')
            keyboard.type(value)
            return False
        elif event.Key == "F11":
            data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
            value = data.get("F11")
            if value == 'auto_1_0':
                threading.Timer(1, auto_1, (timer,)).start()
            else:
                keyboard.type(value)

            return False
        elif event.Key == "Oem_3":
            data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
            value = data.get("left")
            keyboard.type(value)
            return False
        elif event.Key == "F12":
            data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
            value = data.get("F12",'')
            if value=="auto_0":
                os.popen(r".\all_input\all_input.exe")
                return False
            elif value == "auto_1_1":
                threading.Timer(1, auto_2, (timer,)).start()
            else:
                keyboard.type(value )
            return False
        else:
            return True
    except Exception as e:
        return False

def run_key():
    hm = PyHook3.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
if __name__ == '__main__':
    run_key()