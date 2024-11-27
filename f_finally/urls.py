from django.urls import path
from f_finally.views import *

urlpatterns = [
    path('finally/',ffinally,name='f_finally'),

]