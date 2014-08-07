from django.shortcuts import render

# Create your views here.

def index(request):
    page_title='Dashboard'
    return render(request, "index.html", locals())