from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# from enroll.models import inputIndex
from inputdata.models import data

def index(request):
    return render(request,"index.html")
def help(request):
    return  render(request,"help.html")


def delte(request):
    getdata=data.objects.all()
    viewdata={
        "getdata":getdata
        }
    # print(getdata)
    return render(request,"delte.html",viewdata)



# ============================================================
def insert(request):
    try:
        if request.method=="POST":
# ==========================HTML FILE NAME TAG SET (INSIDE GET)=========================
            name=request.POST.get("name") 
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
# ==========================HTML FILE NAME TAG SET (INSIDE GET)=========================
            saveddata=data(name=name,mobno=mobno,city=city)
            saveddata.save()
# ===============check Data recived or not -START=================
            # print(name)
            # print(mobno)
            # print(city)
# ===============check Data recived or not -END=================
    except:
        pass
    return render(request,"insert.html")


def delte(request):
    getdata=data.objects.all()
    viewdata={
        "getdata":getdata
        }
    print(getdata)
    return render(request,"delte.html",viewdata)
#===== DELTE CONNECTIED TO DELETEDATA (INPAGE DELTE)=====
def deletedata(request,uid):
    get_id=data.objects.get(id=uid)
    get_id.delete()
    url="/delte/"
    return HttpResponseRedirect(url)


def update(request,uid):
    get_id=data.objects.get(id=uid)
    internaldata={
        "citylist":["Delhi","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"],
        "modifydata":get_id
    }
    try:
        if request.method=="POST":
            name=request.POST.get("name")
            mobno=request.POST.get("mobno")
            city=request.POST.get("city")
            newdatachange=data(id=uid,name=name,mobno=mobno,city=city)
            newdatachange.save()
            url="/delte/"
            return HttpResponseRedirect(url)
    except:
        pass

    return render(request,"update.html",internaldata)


def viewall(request):
    getdata=data.objects.all()
    viewdata={
        "getdata":getdata
    }
    # print(viewdata)
    return render(request,"viewall.html",viewdata)



import datetime
def viewdazine(request):
    hour=['1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12AM','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM','12PM',]
    a={
        'aa':hour
    }
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            
            mobno=request.POST.get('contact')
            
            city=request.POST.get('city')
            
            address=request.POST.get('address')
            
            photo=request.FILES['photo']
            
            
            # aa=datetime.datetime.now()
            # partydate=str(f'{aa.day}-{aa.month}-{aa.year}')
            
            datehtml=request.POST.get('date')
            
            
            timehtml=request.POST.get('time')
            # print(timehtml,'timehtml')
            
            datetime =str(datehtml)+" Time"+str(timehtml)
            

            # print(name,mobno,city,address,photo,datetime)
            savefile=data(name=name,mobno=mobno,city=city,address=address,Photo=photo,partydate=datetime)
            savefile.save()
        
    except:
        pass
    
    
    return render(request,'viewdazine.html',a)

def viewdata(request):
    
    allinvitaation=data.objects.all()
    
    da={
        'awa':allinvitaation
    }
    
    return render(request,'viewdata.html',da)

def bydate(request):
    alldata=data.objects.all()
    timec=[]
    for i in alldata:
        print(i.partydate)
        timec.append(i.partydate)

    print(timec,'timec')
    AA={
        'aa':timec
    }
    
    # print(one,'ononononono')
    try:
        if request.method=="POST":
            # date=request.POST.get('ddate')
            time=request.POST.get("time")
            print(time)
            datetimec=time
            url='/showbydate/'+datetimec
            return HttpResponseRedirect(url)


    except:
        pass

        
    return render(request,'bydate.html',AA)

def showbydate(request,getadate):
    print(getadate)
    
    aqwa=[getadate]
    
    sameview=data.objects.filter(partydate=getadate)
    
    aa={
        'aa':sameview,
        'bb':aqwa
        
    }
    return render(request,'showbydate.html',aa,)