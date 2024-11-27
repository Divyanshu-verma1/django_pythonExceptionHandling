from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ftry(request):
    return HttpResponse('''<h1>try : (block) </h1>
    <h2>In this block we write the Risky code, which may cause error while execution</h2>''')
