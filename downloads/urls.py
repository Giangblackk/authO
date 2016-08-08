from django.conf.urls import url
#from django.conf.urls.defaults import *

from . import views

urlpatterns = [
    url(r'^images/(.*)$','django.views.static.serve',{'document_root':'static/'})
    #url(r'^$',views.downloads, name='downloads')
]
