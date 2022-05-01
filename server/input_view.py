
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from server.models import *
from server.to_excel import *
import datetime
from xlrd import xldate_as_tuple
import openpyxl
import time
def add_info(request):
    if request.method == 'POST':
        req = request.POST
        name = req["name"]
        company = req["company"]
        cardNo = req["cardNo"] + '_' + str(time.time())
        CardAddress = req["CardAddress"]
        agent = req["agent"]
        phone = req["phone"]
        address = req["address"]
        saleName = req["saleName"]
        remark = Remarks.objects.filter(default=1).first()

        if name:
            base_info = BaseInfo( date=datetime.datetime.now(), Type="个人牌",
                                 name=name, phone=phone, address=address, saleName=saleName,
                                 cardNo=cardNo, CardAddress=CardAddress,remark=remark.remark)
            base_info.save()
        else:
            base_info = BaseInfo(date=datetime.datetime.now(), Type="公司牌",
                                 name=company, phone=phone, address=address, saleName=saleName,
                                 cardNo=cardNo, CardAddress=CardAddress, agent=agent,remark=remark.remark)
            base_info.save()
        return JsonResponse({"code": 0, "msg": "成功"})


def import_wjx(request):
    wb = openpyxl.load_workbook(request.FILES.get("file"))
    try:
        for sheet in wb:
            for item in sheet.values:
                if item[0] == "序号":
                    continue
                date = datetime.datetime.strptime(item[1], "%Y/%m/%d %H:%M:%S")
                Type = item[6]

                phone = item[23]
                address = item[24].replace("-", '') + item[25]
                postcode = item[26].split()[-1]
                saleName = item[27]
                if Type == "个人牌子":
                    country = item[7]
                    name = item[9]
                    if country == '中国内地':
                        cardType = '身份证'
                        cardNo = item[10]
                        CardAddress = item[11]
                    elif '港澳台' in country:
                        cardType = item[8]
                        if '居住证' in cardType:
                            cardNo = item[12]
                            CardAddress = item[15]
                        else:
                            cardNo = item[13]
                            CardAddress = item[16]
                    else:
                        cardType = '护照'
                        cardNo = item[14]
                        CardAddress = item[16]
                    try:
                        base_info =BaseInfo(date=date,Type=Type,country=country, cardType=cardType,
                                 name=name,phone=phone,address=address,postcode=postcode,saleName=saleName,
                                 cardNo=cardNo,CardAddress=CardAddress)
                        base_info.save()
                    except Exception as e:
                        print(e)
                elif Type == "公司牌":
                    name = item[17]
                    cardType = item[18]
                    if "信用代码" in cardType:
                        cardNo =item[19]
                    else: cardNo = item[20]
                    CardAddress = item[21]
                    agent = item[22]
                    try:
                        base_info =BaseInfo(date=date,Type=Type,country="country", cardType=cardType,
                                 name=name,phone=phone,address=address,postcode=postcode,saleName=saleName,
                                 cardNo=cardNo,CardAddress=CardAddress,agent=agent)
                        base_info.save()
                    except Exception as e:
                        print(e)
    except:
        wb.close()
        return JsonResponse({"code": 1, "msg": "表格数据格式不对"})
    wb.close()
    return JsonResponse({"code": 0, "msg": "问卷星数据上传成功"})


def import_pz(request):
    wb = openpyxl.load_workbook(request.FILES.get("file"))
    try:
        for sheet in wb:
            for item in sheet.values:
                if len(item)<5:
                    continue
                if "所有人" in item:
                    continue
                if type(item[0])==int or type(item[0])==float:
                    date = datetime.datetime(*xldate_as_tuple(item[0], 0))
                else:
                    date = item[0]


                printDate = date
                owner = item[1]
                WPMI = item[2]
                number = item[3]
                mortgage = item[4] or ""
                BaseInfo.objects.filter(WPMI=WPMI).update(printDate=printDate,owner=owner, license_number=number,mortgage=mortgage)
    except Exception as e:
        wb.close()
        return JsonResponse({"code": 1, "msg": "表格数据格式不对 "+str(e)})
    wb.close()
    return JsonResponse({"code": 0, "msg": "牌证数据上传成功"})


def del_cert(request):
    if request.method == 'POST':
        req = request.POST
        base_id = req.get("id")
        BaseInfo.objects.filter(id=base_id).update(Number="", brand="", WPMI="",
                                                   engineCode="", CertText="")
        return JsonResponse({"code": 0, "msg": "成功",})

def query(request):
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
            "date": item.date.strftime("%Y-%m-%d %H:%M:%S"),
            "name": item.name,
            "cardNo": item.cardNo.split("_")[0],
            "certText": item.CertText,
            "carType": item.carType,
            "saleName": item.saleName,
            "tax": item.tax,
            "postcode":item.postcode,
            "billText": item.billText,
            "remark":item.remark,
            "type":item.Type
        }
        data.append(item_res)
    return JsonResponse({ "code": 0, "msg": "成功", "count": total, "data": data})

def up_postcode(request):
    if request.method == 'POST':
        req = request.POST
        postcode = req.get("postcode")
        base_id = req.get("id")
        BaseInfo.objects.filter(id=base_id).update(postcode=postcode)
        return JsonResponse({"code": 0, "msg": "成功"})

def to_excel(request):
    # try:
    base_id = request.GET.get("id")
    base_info = BaseInfo.objects.filter(id=base_id).first()

    if base_info.Type == "个人牌":
        res = oneself_excel(base_info.name, base_info.postcode,base_info.address,base_info.phone, base_info.brand,
                      base_info.WPMI,base_info.carType)
    else:
        res=company_excel(base_info.name, base_info.postcode, base_info.address, base_info.phone, base_info.brand,
                      base_info.WPMI, base_info.carType,base_info.agent)
    if res:
        ee = EasyExcel()
        ee.m_excel.Visible = True
        ee.open("../申请表/{}.xls".format(base_info.name))
        return JsonResponse({"code": 0, "msg": "成功", })

    return JsonResponse({"code": 0, "msg": "失败", })


def to_excel_wei(request):
    # try:
    base_id = request.GET.get("id")
    base_info = BaseInfo.objects.filter(id=base_id).first()

    if base_info.Type == "个人牌":
        return JsonResponse({"code": 1, "msg": "个人牌不支持", })
    res = entrust_excel(base_info.name, base_info.agent, base_info.carType, base_info.WPMI,base_info.phone, base_info.address)
    if res:
        ee = EasyExcel()
        ee.m_excel.Visible = True
        ee.open("../委托书/{}.xls".format(base_info.name))
        return JsonResponse({"code": 0, "msg": "成功", })

    return JsonResponse({"code": 0, "msg": "失败", })

def numberType(request):
    rs = NumberTypeS.objects.all()
    item = []
    for nt in rs:
        item.append({
            "id":nt.id,
            "NumberType":nt.NumberType
        })

    return JsonResponse({"code": 0, "msg": "成功","data": item})

def update_cert(request):

    if request.method == 'POST':
        req = request.POST

        cert_text = req.get("CertText")
        base_id = req.get("id")
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        if cert_text:
            cert_items = cert_text.split("|")
            if len(cert_items) != 22:
                return JsonResponse({"code": 1, "msg": "合格证长度不对"})
            number = cert_items[2]
            brand = cert_items[5] + cert_items[6]
            wpmi = cert_items[7]
            produce =cert_items[3]
            engineCode = cert_items[9]
        else:
            number = req.get("number")
            brand = req.get("brand")
            wpmi = req.get("wpmi")
            engineCode = req.get("engineCode")
            produce= req.get("produce")
            cert_text = "|".join([number,brand,wpmi,engineCode])
        BaseInfo.objects.filter(id=base_id).update(Number=number, brand=brand, WPMI=wpmi,
                                                   engineCode=engineCode, CertText=cert_text,inputDate=today,produce=produce)
        return JsonResponse({"code": 0, "msg": "成功","certText": cert_text})


def update_car_type(request):

    if request.method == 'POST':
        req = request.POST
        car_type = req.get("carType")
        base_id = req.get("id")
        BaseInfo.objects.filter(id=base_id).update(carType=car_type)
        return JsonResponse({"code": 0, "msg": "成功"})


def update_tax(request):
    if request.method == 'POST':
        req = request.POST
        tax = req.get("tax")
        base_id = req.get("id")
        BaseInfo.objects.filter(id=base_id).update(tax=tax)
        return JsonResponse({"code": 0, "msg": "成功"})

def update_bill(request):
    if request.method == 'POST':
        req = request.POST
        bill_text = req.get("BillText")
        base_id = req.get("id")

        if bill_text:
            bill_items = bill_text.split(",")
            try:
                billCode = bill_items[2]
                billNumber = bill_items[3]
                billDate = bill_items[5]
            except:
                return JsonResponse({"code": 1, "msg": "发票长度不对"})
        else:
            billCode = req.get("billCode")
            billNumber = req.get("billNumber")
            billDate = req.get("billDate")
            bill_text = ",".join([billCode,billNumber,billDate])

        BaseInfo.objects.filter(id=base_id).update(billCode=billCode, billNumber=billNumber, billDate=billDate,
                                                   billText=bill_text)
        return JsonResponse({"code": 0, "msg": "成功","billText": bill_text})


def del_bill(request):
    if request.method == 'POST':
        req = request.POST
        base_id = req.get("id")
        BaseInfo.objects.filter(id=base_id).update(billCode="", billNumber="", billDate="",
                                                   billText="")
        return JsonResponse({"code": 0, "msg": "成功", })


def remarks(request):
    rs = Remarks.objects.all()
    item = []
    for remark in rs:
        item.append({
            "id":remark.id,
            "remark":remark.remark,
            "default": remark.default
        })

    return JsonResponse({"code": 0, "msg": "成功","data": item})


def up_remark(request):
    req = request.POST
    remark = req.get("remark")
    base_id = req.get("id")
    BaseInfo.objects.filter(id=base_id).update(remark=remark)
    return JsonResponse({"code": 0, "msg": "成功"})


def set_default_remark(request):

    remark = request.POST.get("id")
    Remarks.objects.filter(default=1).update(default=0)
    Remarks.objects.filter(id=remark).update(default=1)
    return JsonResponse({"code": 0, "msg": "成功"})


def add_remark(request):
    remark= request.POST.get("remark")
    rs = Remarks(remark=remark)
    rs.save()
    return JsonResponse({"code": 0, "msg": "成功"})


def del_remark(request):
    remark_id= request.POST.get("id")

    Remarks.objects.filter(id=remark_id).delete()
    return JsonResponse({"code": 0, "msg": "成功"})

def add_number(request):
    nt= request.POST.get("numberType")
    rs = NumberTypeS(NumberType=nt)
    rs.save()
    return JsonResponse({"code": 0, "msg": "成功"})


def del_number(request):
    remark_id= request.POST.get("id")

    NumberTypeS.objects.filter(id=remark_id).delete()
    return JsonResponse({"code": 0, "msg": "成功"})