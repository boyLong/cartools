from pywinauto.application import Application
import requests


def run_text():
    try:
        data = requests.get("http://127.0.0.1:8000/get_key").json()["data"]
        app = Application().connect(class_name='ThunderRT6MDIForm')
        thunderrtmdiform = app.ThunderRT6MDIForm

        thunderrtmdiform["Edit27"].type_keys(data["F1"])
        thunderrtmdiform["Edit30"].type_keys(data["F2"])

        thunderrtmdiform["Edit28"].type_keys(data["F3"])
        thunderrtmdiform["Edit34"].type_keys(data["F4"])
        thunderrtmdiform["Edit35"].type_keys(data["F5"])
        thunderrtmdiform["Edit33"].type_keys(data["F6"])
        thunderrtmdiform["Edit0"].type_keys(data["F7"])
        thunderrtmdiform["Edit2"].type_keys(data["F8"])
        thunderrtmdiform["Edit9"].type_keys(data["F9"])
        thunderrtmdiform["Edit15"].type_keys(data["F10"])
        thunderrtmdiform["Edit5"].type_keys(data["F11"])
        return True
    except Exception as e:
        print(e)
        return False

run_text()



