
from django.urls import path,include
from . import views
from .views import *

app_name = 'landingpage'

urlpatterns = [
    path('',index,name="index")
]