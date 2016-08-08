from django.shortcuts import render
from django.http import HttpResponse

def downloads(request):
    response = HttpResponse(mimetype='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('example.png')
    response['X-Sendfile'] = smart_str(path_to_file)
    return response
