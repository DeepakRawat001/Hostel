from django.http import HttpResponse
from django .template import loader
from django.shortcuts import render,redirect
from .models import Student,Notice,Room,Complain
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):

    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['name'])
                return render(request,'sign/signup.html',{'error':'Username already exist'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['name'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'sign/signup.html',{'error':'Password dosen\'t matched'})
    else:
         return render(request, 'sign/signup.html')

def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'sign/login.html',{'error':"username or password is incorrect"})
    return render(request, 'sign/login.html')

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'sign/header.html')

def home(request):
    return render(request, 'sign/index.html')

def search(request):
    return render(request, 'sign/search.html')
# for searching the result from database
def result1(request):
    data=request.GET['query']
    data2=request.GET['query2']
    if(data=="Course"):
        result=Student.objects.filter(Course=data2)
    else:
        result = Student.objects.filter(City=data2)
    return render(request,'sign/foreign.html',{"key":result})

def notice(request):
    b = Student.objects.get(pk=1)
    a=Notice.objects.all()
    return  render(request,'sign/notice.html',{"key2":a,"key3":b})

def detail(request):
    a=request.user
    # request.user returns an object hence it is to be converted into the string
    b=str(a)
    if b=="director" or b=="dstar" or b=="warden":
        return render(request, 'sign/detail.html')

    else :
        return render(request, 'sign/header.html', {'error': "you don\'t have permission to access this page "})


def room(request):
    a=request.GET['Block_Name']
    b=request.GET['Room_Number']
    c=request.GET['Bed_Availabel']
    x=Room(Block_Name=a,Room_Number=b,Bed_Availabel=c)
    x.save()
    return render(request, 'sign/insert.html',{"key3":a})

def complain(request):
    return render(request,'sign/complaint.html')

def hello(request):
    if request.method=="POST":

        a=request.POST['subject']
        print(a)
        b=request.POST['body']
        #d=request.POST('date')
        c=Complain()
        c.subject=a
        c.body=b
        #c.date=d
        c.save()
        return render(request,'sign/header.html')
    else:
        return render(request, 'sign/result1.html')
#for room selection
def seat(request):
    '''for changing the color of chceckbox'''
    a = Room.objects.all()
    occupied = ""
    empty=""
    for i in a:
        name=i.Student_Name
        b=name.split(",")
        #print(b)
        c=len(b)
        #print(c)
        if(i.Bed_Availabel==c):
            x=str(i.Room_Number)+","
            occupied=occupied+x
        else:
            y=str(i.Room_Number)
            empty=y+","+empty
    return render(request, 'sign/seat.html',{"occupied":occupied,"empty":empty})
'''after clicking in a room'''
def check(request):
    x=request.POST['room']
    b = Room.objects.get(pk=x)
    name=b.Student_Name
    j= name.split(",")
    c=len(j)
    "taking the name from the user"
    print(b.Bed_Availabel)
    print(c)
    # if (b.Bed_Availabel >= c):
    if (b.Bed_Availabel != c):
        j=b.Block_Name
        k=b.Bed_Availabel
        l=b.Room_Number
        return render(request, 'sign/StudentName.html',{"BlockName":j,"BedAvailabel":k,"RoomNumber":l})
    return redirect('seat')

def add(request):
    if request.method == "POST":
        x=request.POST['RoomNumber']
        y=request.POST['name']
        b=Room.objects.get(pk=x)
        name=b.Student_Name
        j = name.split(",")
        c = len(j)
        if(name=="null"):
            name=""
            #for null
            #b.Student_Name=name+" , "+y
            b.Student_Name =""+y
            b.save()
        elif(c<b.Bed_Availabel):
            b.Student_Name = name + " , " + y
            b.save()
    return redirect('seat')

def contact(request):
    return render(request, 'sign/contact.html')




