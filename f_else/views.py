from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def felse(request):
    return HttpResponse('''<h1>else : (block)</h1> 
    <h2>If <b>no error</b> found in the try block then this block will be executed. </h2>''')
