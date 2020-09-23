from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import demand_draft
 # Create your views here.


def login(request):
    return render(request,'catlog/login.html')
    user=request.POST['user']
    password=request.POST['password']
    if user == 46998 and password == 123:
        return render(request,'catlog/index.html')
    return render(request,'catlog/login.html')


def index(request):

    return render(request,'catlog/index.html')


def submit(request):
    dd_no = request.POST['dd_no']
    dd_name=request.POST['dd_name']
    dd_amount=request.POST['dd_amount']
    dd_bank=request.POST['dd_bank']
    dd_date=request.POST['dd_date']
    data=demand_draft(dd_no=dd_no,dd_name=dd_name,dd_amount=dd_amount,dd_bank=dd_bank,dd_date=dd_date)
    data.save()
    print(dd_no,dd_name,dd_amount,dd_bank)
    return redirect('index')


def search(request):

    dd_dict={
     'dd_data':demand_draft.objects.all()
     }
    return render(request,'catlog/search.html',dd_dict)
