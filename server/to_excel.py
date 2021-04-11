import os
import time
import os.path
import datetime
import win32com.client
import pythoncom

def dealPath(pathname=''):
    '''deal with windows file path'''

    pathname = os.path.join(os.getcwd(), pathname)
    return pathname


class EasyExcel(object):
    '''class of easy to deal with excel'''

    def __init__(self):
        '''initial excel application'''
        self.m_filename = ''
        self.m_exists = False
        pythoncom.CoInitialize()
        try:
            self.m_excel = win32com.client.DispatchEx("Excel.Application")  # 也可以用Dispatch，前者开启新进程，后者会复用进程中的excel进程
        except:
            self.m_excel = win32com.client.DispatchEx("wps.Application")  # 也可以用Dispatch，前者开启新进程，后者会复用进程中的excel进程

        self.m_excel.DisplayAlerts = False  # 覆盖同名文件时不弹出确认框

    def open(self, filename=''):
        '''open excel file'''
        if getattr(self, 'm_book', False):
            self.m_book.Close()
        self.m_filename = dealPath(filename) or ''
        self.m_exists = os.path.isfile(self.m_filename)
        print(self.m_filename)
        if not self.m_filename or not self.m_exists:
            self.m_book = self.m_excel.Workbooks.Add()
        else:

            self.m_book = self.m_excel.Workbooks.Open(self.m_filename)
            # self.m_book

    def save(self, newfile=''):
        '''save the excel content'''
        assert type(newfile) is str, 'filename must be type string'
        newfile = dealPath(newfile) or self.m_filename
        if not newfile or (self.m_exists and newfile == self.m_filename):
            self.m_book.Save()
            return
        pathname = os.path.dirname(newfile)
        if not os.path.isdir(pathname):
            os.makedirs(pathname)
        self.m_filename = newfile
        self.m_book.SaveAs(newfile)

    def close(self):
        '''close the application'''
        self.m_book.Close(SaveChanges=1)
        self.m_excel.Quit()

    def getSheet(self, sheet=1):
        '''get the sheet object by the sheet index'''
        assert sheet > 0, 'the sheet index must bigger then 0'
        return self.m_book.Worksheets(sheet)


def oneself_excel(name, postcode, address,phone,brand,wpmi,car_type):
    ee = EasyExcel()
    ee.open(r"excel\base_info.xls")
    today = datetime.datetime.today().strftime("%Y年%m月%d日")
    status = True
    try:
        sht = ee.getSheet(1)
        sht.Range('e5').value = name
        sht.Range('x5').value = postcode
        sht.Range('e6').value = address
        sht.Range('e7').value = phone
        sht.Cells(8,5).Value = ''
        sht.Cells(8,18).Value = ''
        sht.Range('d12').value = car_type
        sht.Range('d13').value = brand
        sht.Range('r13').value = wpmi
        sht.Range('i19').value = today
        ee.save("../申请表/{}.xls".format(name))
    except Exception as e:
        print(e)
        status =False
    ee.close()
    return status


def company_excel(name, postcode, address,phone,brand,wpmi,car_type,agent):
    ee = EasyExcel()
    ee.open(r"excel\base_info.xls")
    today = datetime.datetime.today().strftime("%Y年%m月%d日")
    status = True

    try:
        sht = ee.getSheet(1)
        sht.Range('e5').value = name
        sht.Range('x5').value = postcode
        sht.Range('e6').value = address
        sht.Range('e7').value = phone
        sht.Cells(8,5).Value = agent
        sht.Cells(8,18).Value = phone
        sht.Range('d12').value = car_type
        sht.Range('d13').value = brand
        sht.Range('r13').value = wpmi
        sht.Range('i19').value = today
        ee.save("../申请表/{}.xls".format(name))
    except Exception as e:
        print(e)
        status =False
    ee.close()
    return status


def entrust_excel(name, agent,car_type,wpmi,phone,address):
    ee = EasyExcel()
    ee.open(r"excel\wei.xlsx")
    status = True
    try:
        sht = ee.getSheet(1)
        sht.Range('e4').value = " "*15+agent+" "*20
        sht.Range('g7').value = car_type
        sht.Range('g8').value = wpmi
        sht.Range('d10').value = agent
        sht.Range('j10').value = phone[0]
        sht.Range('k10').value = phone[1]
        sht.Range('l10').value = phone[2]
        sht.Range('m10').value = phone[3]
        sht.Range('n10').value = phone[4]
        sht.Range('o10').value = phone[5]
        sht.Range('p10').value = phone[6]
        sht.Range('q10').value = phone[7]
        sht.Range('r10').value = phone[8]
        sht.Range('s10').value = phone[9]
        sht.Range('t10').value = phone[10]
        sht.Range('d11').value = address+"（*详细地址*）"
        ee.save("../委托书/{}.xls".format(name))

    except Exception as e:
        print(e)
        status = False
    ee.close()
    return status

if __name__ == '__main__':
    entrust_excel("撒旦","阿斯顿", "型汽",'asdsadasd', "15116930701","asdasdasdasdasdasdas")
#     import sys
#     args = sys.argv
#     if len(args) == 8:
#         print(123123)
#         oneself_excel(args[1], args[2], args[3], args[4], args[5], args[6], args[7])
#     if len(args) == 9:
#         print(2222)
#         company_excel(args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])