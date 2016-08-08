from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str

from os.path import abspath, dirname

def downloads(request):
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('example.png')
    #response['X-Sendfile'] = smart_str('E:/MyWorkspace/Web-Beginner/Django/authO/downloads/example.png')
    print abspath(dirname(__file__))
    response['X-Sendfile'] = smart_str( abspath(dirname(__file__)) + '\sexample.png')
    return response
