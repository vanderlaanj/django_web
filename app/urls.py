from django.urls import path

from django_web.urls import urlpatterns
from .views import index, AkceList, AkceDetail, SportovecDetail, SportovecList

urlpatterns = [
    path('',index,name='index'),
    path('tempelates/',SportovecList.as_view,name='sportovec_list'),
    path('tempelates/<int:pk>',SportovecDetail.as_view,name='sportovec_detail'),
    path('tempelates/<int:pk>',AkceDetail.as_view,name='akce_detail'),
    path('tempelates/',AkceList.as_view,name='akce_list')
]