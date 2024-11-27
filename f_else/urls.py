from django.urls import path
from f_else.views import *

urlpatterns = [
    path('else/',felse, name='f_else'),
]