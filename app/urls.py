from django.urls import path


from .views import index, AkceList, AkceDetail, SportovecDetail, SportovecList

urlpatterns = [
    path('', index, name='index'),
    path('sportovec/',SportovecList.as_view(),name='sportovec_list'),
    path('sportovec/<int:pk>',SportovecDetail.as_view(),name='sportovec_detail'),
    path('akce/<int:pk>',AkceDetail.as_view(),name='akce_detail'),
    path('akce/',AkceList.as_view(),name='akce_list')
]