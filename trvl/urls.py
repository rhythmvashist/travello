
from django.urls import path
from .views import index
from trvl import views
from trvl.views import index

urlpatterns = [
    path("",views.index,name='index'),
]
