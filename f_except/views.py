from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fexcept(request):
    return HttpResponse('''<h1>except :(block)</h1>
    <h2>If some error occurs while running the try block code then except block will be executed to continue other program.</h2>''')
