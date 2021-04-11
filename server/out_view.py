from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from server.models import *
from openpyxl.writer.excel import save_virtual_workbook
import datetime
import openpyxl
import json
import time

key_info = {}


def acceptance(request):
    pass


def tax_table(request):
    pass


def update_key(request):
    req = request.POST
    module_key = req.get("module")
    module_key  = int(module_key)
    base_id = req.get("id")
    item = BaseInfo.objects.filter(id=base_id).first()
    key_info["left"] = item.postcode
    key_info["F1"] = item.name
    if module_key == 0:
        # 税表模式

        key_info["F2"] = item.phone
        key_info["F3"] = item.cardNo.split("_")[0]
        key_info["F4"] = item.billCode
        key_info["F5"] = item.billNumber
        key_info["F6"] = item.tax
        key_info["F7"] = item.engineCode
        key_info["F8"] = item.WPMI
        key_info["F9"] = item.Number
        key_info["F10"] = item.brand
        key_info["F11"] = item.produce
        key_info["F12"] = "auto_0"

    elif module_key == 1:
        # 受理模式
        mortgage_id = req.get("mortgage_id")
        try:
            mortgage_info = Mortgage.objects.filter(id=mortgage_id).first()
        except:
            return JsonResponse({"code": 0, "msg": "没有抵押公司数据"})
        key_info["F2"] = item.cardNo.split("_")[0]
        key_info["F3"] = item.CardAddress
        key_info["F4"] = item.address
        key_info["F5"] = item.phone
        key_info["F6"] = mortgage_info.company
        key_info["F7"] = mortgage_info.code
        key_info["F8"] = mortgage_info.address
        key_info["F9"] = mortgage_info.phone
        key_info["F10"] = mortgage_info.postcode
        key_info["F11"] = "auto_1_0"
        key_info["F12"] = "auto_1_1"
    else:
        key_info["F2"] = item.license_number
        key_info["F3"] = item.carType
        key_info["F4"] = item.WPMI
        key_info["F5"] = item.engineCode
        key_info["F6"] = "粤"+item.license_number
        key_info["F7"] = "auto_3"
        key_info["F8"] = "auto_2"
        key_info["F9"] = ""
        key_info["F10"] = ""
        key_info["F11"] = ""
        key_info["F12"] = ""
    return JsonResponse({"code": 0, "msg": "成功","module_key":module_key})


def out_query(request):
    pagenum = request.GET.get("page")
    key = request.GET.get("key")
    limit = request.GET.get("limit")
    if key:
        base_info = BaseInfo.objects.filter(Q(name__icontains=key)).all()
    else:
        base_info = BaseInfo.objects.all()
    paginator = Paginator(base_info, int(limit))
    page = paginator.page(int(pagenum))
    total = paginator.count
    data = []
    for item in page:

        item_res = {
            "id":item.id,
            "name": item.name,
            "cardNo": item.cardNo.split("_")[0],
            "WPMI": item.WPMI,

        }
        data.append(item_res)
    return JsonResponse({ "code": 0, "msg": "成功", "count": total, "data": data})


def mortgage(request):
    mor = Mortgage.objects.all()
    data = []
    for item in mor:
        data.append({"id":item.id,"value":item.company,
                     "company":item.company, "code":item.code, "phone": item.phone,"address":item.address,
                     "postcode":item.postcode})

    return JsonResponse({"code": 0, "data": data})


def add_company(request):
    req = request.POST
    _id = req.get("id")
    company = req.get("company")
    code = req.get("code")
    phone = req.get("phone")
    address = req.get("address")
    postcode = req.get("postcode")
    if _id:
        Mortgage.objects.filter(id=_id).update(company=company,code=code,phone=phone,address=address,postcode=postcode,base_id=0)
        return JsonResponse({"code": 0, "msg": "修改成功"})

    m = Mortgage(company=company,code=code,phone=phone,address=address,postcode=postcode,base_id=0).save()

    return JsonResponse({"code": 0, "msg": "添加成功"})



def get_key(request):

    return JsonResponse({"code": 0, "data": key_info})