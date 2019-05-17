from django.http import HttpResponse
from django .template import loader
from django.shortcuts import render,redirect
from .models import Student,Notice,Room,Complain,Hotel,Detail,Feedback,Notification
from django.contrib.auth.models import User
from .forms import HotelForm
from django.contrib import auth
'''to change the password'''
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
import smtplib
import random,time




def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        global username
        username=user
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'sign/login.html',{'error':"username or password is incorrect"})
    return render(request, 'sign/login.html')

#def pass1(request,user):

def logout(request):
    print("hello honey")
    if request.method=="GET":

        auth.logout(request)
        return redirect('home')
    return render(request,'sign/index.html')

def home(request):
    a = request.user
    # request.user returns an object hence it is to be converted into the string
    b = str(a)
    if b == "director" or b == "dstar" or b == "warden":
        return render(request, 'sign/index.html',{"key":'sign/register/',"key2":"Registeration","key3":'sign/search',"key4":"Search"})
    return render(request,'sign/index.html')
    #return render(request,admin.site.urls)
def signup(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST["password1"] != "":
            if request.POST['password1']==request.POST['password2']:
                try:
                    user=User.objects.get(username=request.POST['name'])
                    return render(request,'sign/signup.html',{'error':'Username already exist'})
                except User.DoesNotExist:
                    user=User.objects.create_user(request.POST['name'],password=request.POST['password1'])
                    auth.login(request,user)
                    b=Detail()
                    b.username=request.POST['name']
                    #b.password=request.POST["password1"]
                    b.email=request.POST["email"]
                    b.save()
                    x=Notification()
                    x.Subject="Student is Added"
                    x.Body="a new user has signed up with name "+user+" "
                    return redirect('home')
            else:
                return render(request,'sign/signup.html',{'error':'Password dosen\'t matched'})
        else:
             return render(request, 'sign/signup.html')
    else:
        return render(request, 'sign/signup.html')


def search(request):
    return render(request, 'sign/search.html')
# for searching the result from database

def idd(a):
    cd=[]
    master=[]
    detail=[]
    value=1
    x = a.find("(")
    for i in a:
        if (i == "("):
            z = a.find(")", x + 1)
            id = (a[x + 1:z])
            cd.append(id)
            y = a.find("(", x + 1)
            x = y
    for i in cd:
        b = Student.objects.get(pk=i)
        detail.append(value)
        detail.append(b.Registration_Number)
        detail.append(b.Student_Name)
        detail.append(b.Course)
        detail.append(b.Mobile_Number)
        detail.append(b.Email_id)
        master.append(detail)
        value = value + 1
        detail = []
    return(master)
def result1(request):
    data=request.GET['query']
    data2=request.GET['query2']
    data3=Student.objects.all()

    if(data=="Course"):
        def equal(x):
            for i in x:
                '''this method will find the correct course'''
                for j in i:
                    y=str(j)
                    if y.casefold() == data2.casefold():
                        return [i[0]]

        BBA=["BBA","Bachelor in Business Administration"]
        BTECH=["BTECH","Bachelor of Technology","Bachelor in Technology"]
        BCA=["BCA","Bachelor in Computer Application"]
        HM=["HM","Hotel Management System"]
        Poly=["poly","polytechnic"]
        course1=[BBA,BTECH,BCA,HM]
        xyz=equal(course1)
        if(xyz!=None):

            print(xyz)

            print(xyz[0])
            """to fetch the record of a particular course"""
            result = Student.objects.filter(Course=xyz[0])
            a = str(result)
            master=idd(a)
            return render(request, 'sign/SearchResult.html', {"master":master})
        else:
            return render(request, 'sign/search.html', {"error": "! please enter the valid course"})
    elif(data=="Gender"):
            """to fetch the record of a particular gender"""
            result = Student.objects.filter(Gender=data2)
            a=str(result)
            master=idd(a)
            return render(request, 'sign/SearchResult.html',{"master":master})
    elif(data=="Blood Group"):
        result = Student.objects.filter(Blood_Group=data2)
        a = str(result)
        master = idd(a)
        return render(request, 'sign/SearchResult.html', {"master": master})
    elif(data=="Room Number"):
        result=Room.objects.get(pk=data2)
        """b.room_number=2"""
        print(result)
        x=result.Registration_Number
        print(x)
        x=x.split(",")
        a=""
        for i in x:
            a=a+str(Student.objects.filter(Registration_Number=i))

        master=idd(a)
        return render(request, 'sign/SearchResult.html', {"master": master})
    elif(data=="Registration Number"):
        result = Student.objects.filter(Registration_Number=data2)
        print("hello")
        a = str(result)
        master = idd(a)
        return render(request, 'sign/SearchResult.html', {"master": master})

    '''elif (data == "Floor"):
        result = Room.objects.filter(Floor=data2)
        a = str(result)
        print(a)
        x = a.find("(")
        cd=[]
        for i in a:
            if (i == "("):
                z = a.find(")", x + 1)
                id = (a[x + 1:z])
                cd.append(id)
                y = a.find("(", x + 1)
                x = y
        print(cd)
        for i in cd:
            b=Room.objects.get(pk=i)
            print(b.Student_Name)
        return render(request, 'sign/SearchResult.html')'''


    #else:
        #result = Room.objects.filter(State=data2)
    return render(request,'sign/SearchResult.html',)

def notice(request):
    a = request.user
    # request.user returns an object hence it is to be converted into the string
    b = str(a)
    if b == "director" or b == "dstar" or b == "warden":
        print("helllo")
        return render(request, 'sign/notice.html',{"key2":""})

    else:
        print("honey")
        b = Notice.objects.all()
        b=str(b)
        length = len(b)
        print(b)
        print(length)
        '''<QuerySet [<Complain: Complain object (3)>, <Complain: Complain object (4)>, 
        <Complain: Complain object (5)>, <Complain: Complain object (6)>, <Complain: Complain object (7)>]>
        '''
        for i in range(length - 1, 0, -1):
            if (b[i] == ")"):
                j = b[i - 1]
                break
        b = Notice.objects.get(pk=j)
        #print(b)
        return render(request, 'sign/notice.html', {"key": b,"key2":"readonly"})



   #b = Student.objects.get(pk=1)
    #a=Notice.objects.all()


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
    a = request.user
    # request.user returns an object hence it is to be converted into the string
    b = str(a)
    if b == "director" or b == "dstar" or b == "warden":
        b = str(Complain.objects.all())
        length= len(b)
        print(b)
        print(length)
        '''<QuerySet [<Complain: Complain object (3)>, <Complain: Complain object (4)>, 
        <Complain: Complain object (5)>, <Complain: Complain object (6)>, <Complain: Complain object (7)>]>
        '''
        for i in range(length-1,0,-1):
            if(b[i]==")"):
                j=b[i-1]
                break
        print(j)
        b = Complain.objects.get(pk=j)
        return render(request, 'sign/complain.html', {"key": b, "key2": "readonly","key3":"Home"})
    else:
        return render(request,'sign/complain.html',{"key2":"","key3":"send complain"})

def hello(request):
    '''method for the firing the complain'''
    if request.method=="POST":
        a = request.user
        # request.user returns an object hence it is to be converted into the string
        b = str(a)
        if b == "director" or b == "dstar" or b == "warden":
            return redirect("home")

        else:
            a = request.POST['subject']
            print(a)
            b = request.POST['body']
            # d=request.POST('date')
            c = Complain()
            c.subject = a
            c.body = b
            c.email = request.POST['email']
            c.roll_no = request.POST['rollno']
            c.student_name = request.POST['name']
            v=time.strftime("%Y-%m-%d")
            c.date=v
            # c.date=d
            c.save()
            return redirect("home")

    else:
        return render(request, 'sign/complain.html')
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
    name= name.split(",")
    c=len(name)
    "taking the name from the user"
    print(b.Bed_Availabel)
    print(c)
    # if (b.Bed_Availabel >= c):
    if (b.Bed_Availabel != c):
        j=b.Block_Name
        k=b.Bed_Availabel
        l=b.Room_Number
        return render(request, 'sign/StudentName.html',{"BlockName":j,"BedAvailabel":k,"RoomNumber":l,"name":name})
    return redirect('seat')


def contact(request):
    return render(request, 'sign/contact.html')

def register(request):
    return render(request, 'sign/register.html')

def about(request):
    return render(request, 'sign/about.html')






# for searching the result from database

def RegisterNumberCheck(x):
    '''this method will check that either the room for the student is already
    allocated or not by mathing the registration number'''
    b=Room.objects.all()
    RegisterNumber=""
    for i in b:
        RegisterNumber=RegisterNumber+" "+i.Registration_Number
    if(x in RegisterNumber):
        print("hello")
        return False
    else:
        return True
def add(request):
    if request.method == "POST":
        n=request.POST['RoomNumber']
        b = Room.objects.get(pk=n)
        Existing_Student =b.Student_Name
        Existing_Student = Existing_Student.split(",")

        print(Existing_Student)

        register=request.POST['register']
        z=RegisterNumberCheck(register)

        if(z):
            #room number
            result=Student.objects.filter(Registration_Number=register)
            #print(result)
            '''to find the name of the student'''
            a = str(result)
            x = a.find("(")
            if(x!=-1):
                cd = []
                for i in a:
                    if  (i == "("):
                        z = a.find(")", x + 1)
                        id = (a[x + 1:z])
                        cd.append(id)
                        y = a.find("(", x + 1)
                        x = y
                StudentId=cd[0]
                ab=Student.objects.get(pk=StudentId)
                y=ab.Student_Name
                b=Room.objects.get(pk=n)
                name=b.Student_Name
                print(name)
                j = name.split(",")
                Registation_Number=b.Registration_Number
                c = len(j)
                if(name=="null" or Registation_Number==0):
                    name=""
                    #for null
                    #b.Student_Name=name+" , "+y
                    b.Student_Name =""+y
                    b.Registration_Number=register
                    b.save()
                    object1=Notification()
                    object1.Subject="Room Booked"
                    object1.Body="Room no."+ n + " is booked for the Student "+y
                    object1.save()
                elif(c<b.Bed_Availabel):
                    b.Student_Name = name + " , " + y
                    b.Registration_Number=Registation_Number+ " , "+register
                    b.save()
                    object1 = Notification()
                    object1.Subject = "Room Booked"
                    object1.Body = "Room no." + n + " is booked for the Student " + y
                    object1.save()
            else :
                b = Room.objects.get(pk=n)
                j = b.Block_Name
                k = b.Bed_Availabel
                l = b.Room_Number
                return render(request, 'sign/StudentName.html',{"BlockName":j,"BedAvailabel":k,"RoomNumber":l,'error':"!Registration number is wrong","name" : Existing_Student})
        else:
            b = Room.objects.get(pk=n)
            j = b.Block_Name
            k = b.Bed_Availabel
            l = b.Room_Number
            return render(request, 'sign/StudentName.html',
                          {"BlockName": j, "BedAvailabel": k, "RoomNumber": l, 'error': "!Room for this student is already allocated",'name' : Existing_Student})

    return redirect('seat')

def create(request):
    return render(request,"sign/create.html")

def studentRegister(request):
    if request.method == "POST":
        first_name=request.POST["first name"]
        last_name=request.POST["last name"]
        father_name=request.POST["father name"]
        email=request.POST["email"]
        phone_number=request.POST["phone number"]
        #image
        course=request.POST["course"]
        gender=request.POST["gender"]
        #if(gender=="male"):
        registration_number=request.POST["registration"]
        #registration_number=int(registration_number)
        father_number=request.POST["father number"]
        address=request.POST["address"]
        image=request.POST['image1']
        dob=request.POST["dob"]
        b=Student()
        b.Registration_Number=registration_number
        b.Student_Name=first_name+" "+ last_name
        b.Gender=gender
        b.Course=course
        b.Blood_Group=request.POST['blood']
        b.Date_of_birth=dob
        b.Mobile_Number=phone_number
        b.Email_id=email
        b.Father_Name=father_name
        b.Father_Mobile_Number=father_number
        b.Address=address
        b.Image=image
        b.save()
        object1 = Notification()
        object1.Subject = "Student Registered"
        object1.Body = first_name +" " + last_name  + " of course " + course +" is registered" " registeration number="+registration_number
        object1.save()
        return redirect('home')
    return render(request,'sign/register.html')

def hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

       #x=request.FILES['']
        if form.is_valid():

            form.save()
            #b = Hotel()
            #a = request.POST['text']
            #b.email = a
            #b.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'sign/image.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')


def media(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        return render(request, 'sign/displayImage.html',
                       {'hotel_images': Hotels})
    else:
        redirect("home")
def password_changed(request):
    return HttpResponse('password changed successfully')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_changed')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'sign/change_password.html', {
        'form': form
    })

def forget_password(request):
    if request.method == 'POST':
        email=request.POST["email"]
       # mail=str(mail)
        #print(mail)
        result = str(Detail.objects.filter(email=email))
        x=result.find('(')
        if(x!=-1):
            y=result.find(')')
            z=result[x+1:y]
            print(z)
            l = [1, 2, 3, 4]
            j = []
            k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in l:
                a = (random.choice(k))
                j.append(str(a))
                # print(a)
            print("hello")
            j="".join(j)
            x=4563
            content = "your one time password is "+str(j)
            try:
                mail = smtplib.SMTP("smtp.gmail.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login("rawatdeepak.dr34@gmail.com", "zatchbell")
                mail.sendmail("rawatdeepak.dr34@gmail.com",email, content)
                mail.close()
                b=Detail.objects.get(pk=z)
                b.code=j
                b.save()
                print(z)
                return render(request, 'sign/otp.html',{"id":z})
            except:
                return render(request, 'sign/forget_password.html',{"error":"!check your internet connection"})

        return render(request,'sign/forget_password.html',{"error":"we didn't recognize your email id"})

    return render(request, 'sign/forget_password.html')
def otp(request):
    if request.method == 'POST':
        otp= request.POST["otp"]
        user=request.POST["id"]
        print(user)
        print("fnndndnn")
        b = Detail.objects.get(pk=user)
        x=str(b.code)
        if(otp==x):

            return render(request, 'sign/confirm_password.html',{"id":user})
        else:
            return render(request, 'sign/otp.html',{"error":"!OTP is incorrect","id":user})
    return render(request,'sign/otp.html')
def confirm_password(request):
    if request.method == 'POST':
        pass1=request.POST["password"]
        pass2=request.POST["confirm_password"]
        user=request.POST["id"]
            #print("hellloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        print(user)

        if(pass1==pass2):
            if (len(pass1) >= 8):
                b = Detail.objects.get(pk=user)
                x = b.username
                u=User.objects.get(username__exact=x)
                u.set_password(pass1)
                u.save()
                b.code = 0
                b.save()
                return redirect('home')
            else:
                return render(request, 'sign/confirm_password.html',
                              {"error": "password should be minimum 8 characters long","id":user})

        else:
            return render(request, 'sign/confirm_password.html',{"error":"password not matched","id":user})

    return render(request, 'sign/confirm_password.html')

def entry(request):
    '''for entering the data if anyone wants to contact'''
    if request.method == 'POST':
        b=Feedback()
        x=request.POST["first-name"]
        y=x+" "+request.POST["last-name"]
        b.username=y
        b.email=request.POST["email"]
        phone_no=request.POST["phone"]
        phone_no=int(phone_no)
        b.phone_no=phone_no
        b.message=request.POST["message"]
        print(request.POST["message"])
        b.save()
    return redirect('home')
    #return render(request, 'sign/index.html')

def submit(request):
    '''method for submitting the notice updated '''
    if request.method == 'POST':
        a = request.user
        # request.user returns an object hence it is to be converted into the string
        b = str(a)
        if b == "director" or b == "dstar" or b == "warden":
            print("notice")
            b=Notice()
            b.subject=request.POST['subject']
            b.notice=request.POST['body']
            b.date=time.strftime("%Y-%m-%d")
            b.save()
            return redirect('home')
    return redirect('home')
def xyz(request):
    b=Complain.objects.all()
    print("hello")
    print(b)
    x=0
    for i in b:
        x=x+1
    print(x)
    return render(request, 'sign/complainResult.html',{"key":b})
