from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rolypoly(request,match,aphabel):
    print match + aphabel
    print request.path
    print request.method
    print request.GET.dict()
    requestParams = request.GET.dict()
    print requestParams['name']
    print request.environ
    return render(request,'rolypoly.html')
