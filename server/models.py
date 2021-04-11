from django.db import models


class BaseInfo(models.Model):

    date = models.DateTimeField()
    carType = models.TextField(verbose_name='号码种类', default="小型汽车")
    Type = models.TextField(verbose_name='牌证类型')
    country = models.TextField(verbose_name="户籍所在地")
    city = models.TextField(verbose_name="户籍所在城市")
    cardType = models.TextField(verbose_name="证件类型")
    name = models.CharField(max_length=30)
    cardNo = models.TextField(verbose_name="证件号", unique=True)
    CardAddress = models.TextField(verbose_name="证件地址")
    company = models.TextField(verbose_name="公司")
    agent = models.CharField(max_length=30, verbose_name="代理人")
    phone = models.CharField(max_length=30, verbose_name="手机")
    address =models.TextField(verbose_name="收铁牌地址")
    postcode = models.CharField(max_length=30,verbose_name="邮编")
    saleName = models.CharField(max_length=30, verbose_name="销售人员")
    create_time = models.DateField(auto_now=True)
    Number = models.CharField(max_length=50, verbose_name="合格证编号")
    brand = models.CharField(max_length=50, verbose_name="品牌")
    WPMI = models.CharField(max_length=50, verbose_name="车辆识别号")
    engineCode = models.CharField(max_length=50, verbose_name="发动机号")
    CertText = models.TextField(verbose_name="合格证文本")
    printDate = models.DateField(verbose_name="打证日期",blank=True,null=True)
    owner = models.CharField(max_length=50, verbose_name="所有人")
    license_number = models.CharField(max_length=50, verbose_name="号牌号码")
    mortgage = models.CharField(max_length=50, verbose_name="抵押",null=True)
    inputDate = models.DateField(verbose_name="打证日期",blank=True,null=True)
    tax = models.CharField(max_length=50, verbose_name="税价合计")
    produce = models.CharField(max_length=50, verbose_name="制造商",default="")

    billCode = models.CharField(max_length=50, verbose_name="发票代码")
    billNumber = models.CharField(max_length=50, verbose_name="发票号码")
    billDate = models.CharField(max_length=50, verbose_name="发票日期")
    billText = models.TextField(verbose_name="发票文本")
    remark = models.TextField(verbose_name='号码种类', default="聚成报销")
    class Meta:
        ordering = ['-id']


class Mortgage(models.Model):
    base_id = models.IntegerField()
    company = models.CharField(max_length=50, verbose_name="公司名称")
    code = models.CharField(max_length=50, verbose_name="统一社会代码")
    phone = models.CharField(max_length=50, verbose_name="固话")
    address = models.TextField( verbose_name="地址")
    postcode = models.CharField(max_length=50, verbose_name="邮编")


class Remarks(models.Model):
    remark = models.CharField(max_length=50, verbose_name="备注")

class NumberTypeS(models.Model):
    NumberType = models.CharField(max_length=50, verbose_name="号码种类")