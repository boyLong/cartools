from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def input_html(request):
    return render(request, 'input.html')


def out(request):
    return render(request, 'out.html')


def manage(request):
    return render(request, 'manage.html')

