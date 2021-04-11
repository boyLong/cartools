from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from server.models import *
from openpyxl.writer.excel import save_virtual_workbook
import datetime
import openpyxl
import json
import time


def manage_query(request):
    pagenum = request.GET.get("page")
    startInput = request.GET.get("startInput")
    endInput = request.GET.get("endInput")
    startPrint = request.GET.get("startPrint")
    endPrint = request.GET.get("endPrint")
    startWJX = request.GET.get("startWJX")
    endPrWJX = request.GET.get("endPrWJX")
    name = request.GET.get("name")
    limit = request.GET.get("limit")
    item=BaseInfo.objects.all()
    if name:
        item =item.filter(Q(name__icontains=name))
    if startInput:
        item =item.filter(Q(inputDate__gte=datetime.datetime.strptime(startInput,"%Y-%m-%d")))
    if endInput:
        item =item.filter(Q(inputDate__lte=datetime.datetime.strptime(endInput,"%Y-%m-%d")))
    if startPrint:
        item =item.filter(Q(printDate__gte=datetime.datetime.strptime(startPrint,"%Y-%m-%d")))
    if endPrint:
        item =item.filter(Q(printDate__lte=datetime.datetime.strptime(endPrint,"%Y-%m-%d")))
    if startWJX:
        item =item.filter(Q(create_time__gte=datetime.datetime.strptime(startWJX, "%Y-%m-%d")))
    if endPrWJX:
        item =item.filter(Q(create_time__lte=datetime.datetime.strptime(endPrWJX, "%Y-%m-%d")))

    paginator = Paginator(item, int(limit))
    page = paginator.page(int(pagenum))
    total = paginator.count
    data = []
    for item in page:
        data.append({
            "id": item.id,
            "wqx_time": item.create_time,
            "create_time":item.inputDate,
            "printDate": item.printDate,
            "name": item.name,
            "WPMI": item.WPMI,
            "brand":item.brand,
            "number": item.license_number,
            "mortgage": item.mortgage,
            "saleName": item.saleName,
            "remark":item.remark

        })
    return JsonResponse({ "code": 0, "msg": "成功", "count": total, "data": data})


def to_data(request):
    startInput = request.GET.get("startInput")
    endInput = request.GET.get("endInput")
    startPrint = request.GET.get("startPrint")
    endPrint = request.GET.get("endPrint")
    name = request.GET.get("name")
    startWJX = request.GET.get("startWJX")
    endPrWJX = request.GET.get("endPrWJX")

    info = BaseInfo.objects.all()
    if name:
        info =info.filter(Q(name__icontains=name))
    if startInput:
        info =info.filter(Q(inputDate__gte=datetime.datetime.strptime(startInput,"%Y-%m-%d")))
    if endInput:
        info =info.filter(Q(inputDate__lte=datetime.datetime.strptime(endInput,"%Y-%m-%d")))
    if startPrint:
        info =info.filter(Q(printDate__gte=datetime.datetime.strptime(startPrint,"%Y-%m-%d")))
    if endPrint:
        info =info.filter(Q(printDate__lte=datetime.datetime.strptime(endPrint,"%Y-%m-%d")))
    if startWJX:
        info =info.filter(Q(create_time__gte=datetime.datetime.strptime(startWJX, "%Y-%m-%d")))
    if endPrWJX:
        info =info.filter(Q(create_time__lte=datetime.datetime.strptime(endPrWJX, "%Y-%m-%d")))
    data = []
    for item in info:
        data.append({
            "wqx_time":item.create_time,
            "create_time":item.inputDate ,
            "printDate": item.printDate,
            "name": item.name,
            "WPMI": item.WPMI,
            "brand": item.brand,
            "number": item.license_number,
            "mortgage": item.mortgage,
            "saleName": item.saleName,
            "remark": item.remark

        })
    return JsonResponse({ "code": 0, "msg": "成功",   "data": data})


def del_data(request):
    if request.method == 'POST':

        startInput = request.POST.get("startInput")
        endInput = request.POST.get("endInput")
        startPrint = request.POST.get("startPrint")
        endPrint = request.POST.get("endPrint")
        name = request.POST.get("name")
        startWJX = request.POST.get("startWJX")
        endPrWJX = request.POST.get("endPrWJX")
        id_list = request.POST.get("id")
        info = BaseInfo.objects.all()

        if json.loads(id_list):

            for i in json.loads(id_list):
                info.filter(id=i).delete()
            return JsonResponse({"code": 0, "msg": "成功", })

        if name:
            info = info.filter(Q(name__icontains=name))
        if startInput:
            info =info.filter(Q(create_time__gte=datetime.datetime.strptime(startInput,"%Y-%m-%d")))
        if endInput:
            info =info.filter(Q(create_time__lte=datetime.datetime.strptime(endInput,"%Y-%m-%d")))
        if startPrint:
            info =info.filter(Q(printDate__gte=datetime.datetime.strptime(startPrint,"%Y-%m-%d")))
        if endPrint:
            info =info.filter(Q(printDate__lte=datetime.datetime.strptime(endPrint,"%Y-%m-%d")))
        if startWJX:
            info = info.filter(Q(create_time__gte=datetime.datetime.strptime(startWJX, "%Y-%m-%d")))
        if endPrWJX:
            info = info.filter(Q(create_time__lte=datetime.datetime.strptime(endPrWJX, "%Y-%m-%d")))
        info.delete()
    return JsonResponse({ "code": 0, "msg": "成功",  })


def update_manage(request):
    req = request.POST
    number = req.get("number")
    mortgage = req.get("mortgage")
    base_id = req.get("id")
    if number:
        BaseInfo.objects.filter(id=base_id).update(license_number=number)
    elif mortgage:
        BaseInfo.objects.filter(id=base_id).update(mortgage=mortgage)
    else:
        return JsonResponse({"code": 1, "msg": "不可修改", })

    return JsonResponse({ "code": 0, "msg": "成功", })
