import sys

import warnings
warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from KeyListener import run_key
from PyQt5.QtCore import *
import os,sys

import time
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from django.core.management import execute_from_command_line
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
DEBUG_PORT = '5588'
DEBUG_URL = 'http://127.0.0.1:%s' % DEBUG_PORT
os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = DEBUG_PORT
class MainWindow(QMainWindow):


    def on_downloadRequested(self, download: "QWebEngineDownloadItem"):

        download.finished.connect(self._finished)
        old_path = download.path()
        suffix = QFileInfo(old_path).suffix()
        # 下载文件类型
        filttype = download.mimeType()
        # 后缀切割
        unkonw_suffix = filttype.split(r'/')[-1]
        path, _ = QFileDialog.getSaveFileName(self, "Save File", old_path, "*." + unkonw_suffix + ";;" + "*." + suffix)
        if path != "":
            download.setPath(path)
            download.accept()

    def _finished(self):

        QMessageBox.question(self, '导出完成', '导出完成',
                                     QMessageBox.Yes)

    def __init__(self):
        super(MainWindow, self).__init__()
        time.sleep(1)
        self.setWindowTitle('服务站数据')
        self.setGeometry(5, 30, 1760, 850)
        self.browser = QWebEngineView()
        default_profile = QWebEngineProfile.defaultProfile()
        default_profile.setCachePath('cache')
        default_profile.setPersistentStoragePath('cache')


        self.browser.page().profile().downloadRequested.connect(self.on_downloadRequested)
        self.browser.load(QUrl('http://127.0.0.1:8000/index'))
        self.setCentralWidget(self.browser)

    # def closeEvent(self, *args, **kwargs):
    #
    #     try:
    #         os._exit(5)
    #     except Exception as e:
    #         print(e)

if __name__ == '__main__':
    class mythread(QThread):  # 步骤1.创建一个线程实例
        def __init__(self):
            super(mythread, self).__init__()

        def run(self):
            execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000',"--noreload"])

    class mythread2(QThread):  # 步骤1.创建一个线程实例
        def __init__(self):
            super(mythread2, self).__init__()

        def run(self):
            run_key()

    a = mythread()
    a.start()
    t1 =mythread2()
    t1.start()

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())

