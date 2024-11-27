from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ffinally(request):
    return HttpResponse('''<h1>Finally: (block) </h1>
    <h2>This block will be executed irrespective of error occurs or not.</h2>''')
