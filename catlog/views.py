from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import demand_draft,number_register,farmer_register,kit_numbersSerializer,kit_numbers,debitCard,debitCardSerializer
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from django.core.exceptions import ObjectDoesNotExist
import json
 # Create your views here.



def login(request):
    # if request.method =='GET':
    #     return render(request,'catlog/login.html')
    #
    # user=int(request.POST['user'])
    # password=int(request.POST['password'])
    # if user == int(46998) and password == int(123):
    return render(request,'catlog/home_page.html')
    # return render(request,'catlog/login.html')


def index(request):

    return render(request,'catlog/index.html')


def submit(request):
    if len(demand_draft.objects.filter(pk=int(request.POST['dd_no']))) >0:
        return render(request,'catlog/index.html',{'message':'यह डिमांड ड्राफ्ट पहले से मौजूद है।'})
    dd_no = request.POST['dd_no']
    dd_name=request.POST['dd_name'].upper()
    dd_amount=request.POST['dd_amount']
    dd_bank=request.POST['dd_bank']
    dd_date=request.POST['dd_date']
    dd_image=request.FILES['dd_photo']
    print(dd_image,'IMAGE-2')
    data=demand_draft(dd_no=dd_no,dd_name=dd_name,dd_amount=dd_amount,dd_bank=dd_bank,dd_date=dd_date,dd_image=dd_image)
    data.save()
    print(dd_no,dd_name,dd_amount,dd_bank)
    return redirect('index')

def change(request,id):
    if request.method =='POST':
        if len(str(id))>=9:
            mobile_number=request.POST['number']
            num_place=request.POST['num_place']
            num_status=request.POST['num_status']
            number_register.objects.filter(pk=id).update(mob_number=mobile_number,place=num_place,status=num_status)
            return redirect('view')

        dd_no=request.POST['dd_no']
        dd_name=request.POST['dd_name']
        dd_name=dd_name.upper()
        dd_amount=request.POST['dd_amount']
        dd_bank=request.POST['dd_bank']
        dd_date=request.POST['dd_date']
        # if request.FILES['dd_photo'] == '':
        #     dd_image=demand_draft.objects.filter(pk=id).dd_image
        # else:
        # default=request.FILES.get('hide',False)
        # print('HIDE',default)
        if 'dd_photo' in request.FILES:
            dd_image=request.FILES['dd_photo']
        # demand_draft(dd_name=dd_name,dd_bank=dd_bank,dd_no=dd_no,dd_amount=dd_amount,dd_date=dd_date,dd_image=dd_image).save()
            obj=demand_draft.objects.get(pk=id)
            obj.dd_image=dd_image
            obj.save()

        demand_draft.objects.filter(pk=id).update(dd_name=dd_name,dd_bank=dd_bank,dd_no=dd_no,dd_amount=dd_amount,dd_date=dd_date)


        # print(dd_image,'Image','Image')

        return redirect('search')


    if len(str(id))==10:
        data_no={
        'number_data':number_register.objects.get(pk=id)
        }
        return render(request,'catlog/change.html',data_no)

    data={
    'dd_data':demand_draft.objects.get(dd_no=id)
    }
    return render(request,'catlog/change.html',data)



def search(request):

    dd_dict={
     'dd_data':demand_draft.objects.all().order_by('dd_name')
     }
    return render(request,'catlog/search.html',dd_dict)



def number(request):
    if request.method =='POST':
        number = int(request.POST['numbers'])
        if len(str(number))!=10:
            return render(request,'catlog/number_register.html',{'message':'कृपया वेध्य मोबाइल नंबर दर्ज करें।कृपया पुनः नंबर जांचे।'})
        if len(number_register.objects.filter(pk=number))>0:
            return render(request,'catlog/number_register.html',{'message':'मोबाइल नंबर पहले से मौजूद है। कृपया नया मोबाइल नंबर डाले या view मे जाकर देखे।'})
        place=request.POST['num_place']
        state=request.POST['num_status']
        number_register(mob_number=number,place=place,status=state).save()
        print('Numbers:-',number)

    return render(request,'catlog/number_register.html')

def view(request):
    number={
    'numbers':number_register.objects.all()
    }


    return render(request,'catlog/view.html',number)

def edit_detail(request,id):
    if request.method =='POST':
        name=request.POST['farmer_name']
        yojna=request.POST['yojna']
        d=number_register.objects.get(pk=id)
        status=d.status
        place=number_register.objects.get(mob_number=id).place

        print(name,yojna,status,place,'Yesd',id)

        farmer_register(mobile_number=number_register.objects.get(pk=id),name=name,yojna=yojna,status=status,place=place).save()
        details={
        'detail':farmer_register.objects.filter(mobile_number=id),
        'mob_number':number_register.objects.get(pk=id),
        'number':id
        }
        print(details['detail'],'Detail')
        return render(request,'catlog/edit_detail.html',details)
    details={
    'detail':farmer_register.objects.filter(mobile_number=id),
    'mob_number':number_register.objects.get(pk=id),
    'number':id
            }
    return render(request,'catlog/edit_detail.html',details)

def delete_farmer(request,name):

    id=farmer_register.objects.filter(name=name)[0].mobile_number
    print(type(id),'ID',id)

    farmer_register.objects.filter(name=name).delete()
    return redirect('edit_detail',id,)
def enquire_number(request):
    engine = create_engine("postgres://kmxkyswiscvymi:7611aec6de2b7052be8059fa505542f0d51be950c8c873d92096db0e25d4834b@ec2-3-213-106-122.compute-1.amazonaws.com:5432/d239ji720r2qie")
    db = scoped_session(sessionmaker(bind=engine))

    results=db.execute('SELECT * FROM Farmer_detail').fetchall()


    result={
    'results':results
    }
    db.close()
    return render(request,'catlog/enquire_numbers.html',result)


def fino_customers(request):
    if request.method =='POST':
        name=request.POST['customer_name']
        customer_dob=request.POST['customer_dob']
        account_kit=request.POST['account_kit']
        atm_kit=request.POST['atm_kit']
        adhaar_no=request.POST['adhaar_no']
        mobile_no=request.POST['mobile_no']
        customer_father=request.POST['customer_father']
        customer_mother=request.POST['customer_mother']

        return render(request,'catlog/fino_customer.html')


    return render(request,'catlog/fino_customer.html')

def validate(request):
    kit_number=request.GET['value']
    if kit_number=='':
        return HttpResponse('{"data":"False"}')
    if len(kit_number) ==7:
        try:
            atm_info=debitCardSerializer(debitCard.objects.get(pk=kit_number))
            print(atm_info,'atm_info')
            return HttpResponse(json.dumps(atm_info.data))
        except ObjectDoesNotExist or ValueError:
            return HttpResponse('{"data":"False"}')
    else:
        try:
            kit_info=kit_numbersSerializer(kit_numbers.objects.get(pk=kit_number))
            return HttpResponse(json.dumps(kit_info.data))
        except ObjectDoesNotExist or ValueError:
            return HttpResponse('{"data":"False"}')


    # if len(kit_info.data)>0:
    #



def delete_number(request,id):
    number_register.objects.get(pk=id).delete()
    return redirect('view')
