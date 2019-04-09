from django.shortcuts import render

def insert(request):
    a=request.GET['query']
    #data = request.GET['query']
    '''b=request.GET['Room_Availabel']
    c=request.GET['Bed_Number']
    x=Room(Block_Name=a,Room_Availabel=b,Bed_Number=c)
    x.save()'''
    return render(request,'sign/insert.html')
