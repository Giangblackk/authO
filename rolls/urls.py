from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^rolypoly/$',views.rolypoly,name='rolypoly')
    #url(r'^$',views.rolypoly,name='rolypoly')
]
