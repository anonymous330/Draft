from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import demand_draft
 # Create your views here.


def login(request):
    if request.method =='GET':
        return render(request,'catlog/login.html')

    user=int(request.POST['user'])
    password=int(request.POST['password'])
    if user == int(46998) and password == int(123):
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
