from django.shortcuts import render
from django.core.paginator import Paginator
from models import Devices, Server


# Create your views here.

def index(request):
    page_title='Dashboard'
    return render(request, "index.html", locals())

def list_server(request):
    page_title='服务器列表'
    list_items = Server.objects.all()
    count = list_items.count()
    paginator = Paginator(list_items ,15)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    return render(request, "assets/list_server.htmll", locals())