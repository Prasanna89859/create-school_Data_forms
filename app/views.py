from django.shortcuts import render
from app.forms import *
from app.models import *
# Create your views here.
from django.http import HttpResponse

def create_school(request):
    SDFO=StudentForms()
    d={'SDFO':SDFO}
    if request.method=='POST':
        SDFD=StudentForms(request.POST)
        if SDFD.is_valid():
            SDFD.save()
            return HttpResponse('create school forms Done.... ')
        else:
            return HttpResponse('Data not insert....')
    return render(request,'create_school.html',d)

