"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .input_view import *
from .out_view import *
from .manage_view import *
from .view import *
from django.conf.urls import static
from server import settings
urlpatterns = [
    path('input.html', input_html),
    path('index', index),
    path('out.html', out),
    path('manage.html', manage),
    path('query', query),
    path('import_wjx', import_wjx),
    path('import_pz', import_pz),
    path('update_cert', update_cert),
    path('update_car_type', update_car_type),
    path('up_postcode', up_postcode),
    path('out_query', out_query),
    path('update_key', update_key),
    path('manage', manage),
    path('mortgage', mortgage),
    path('add_company', add_company),
    path('get_key', get_key),
    path('del_cert', del_cert),
    path('manage_query', manage_query),
    path('to_data', to_data),
    path('to_excel', to_excel),
    path('del_data', del_data),
    path('update_tax', update_tax),
    path('update_bill', update_bill),
    path('remarks', remarks),
    path('up_remark', up_remark),
    path('add_remark', add_remark),
    path('del_remark', del_remark),
    path('to_excel_wei', to_excel_wei),
    path("update_manage",update_manage),
    path("del_bill", del_bill),
    path("add_info", add_info),
    path("del_number", del_number),
    path("add_number", add_number),
    path("numberType", numberType),
]

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)