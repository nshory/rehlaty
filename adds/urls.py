

from django.urls import path , include
from . import views

app_name = 'list'

urlpatterns = [

    path('',views.list, name='list'),
    path('Sections',views.SectionsModel, name='sections'),
    path('create_add',views.create_ad,name='create_ad'),
    path('update_add/<int:id>',views.update_add,name='update_add'),
    path('<int:id>',views.detail,name='details'),
    path('sub/<title>',views.sub_1,name='sub_1'),
    path('land',views.sub_land,name='land'),




]
