from django.http import HttpResponse
from django .template import loader
from django.shortcuts import render
from .models import Movie

def index(request):
    #movie=Movie.objects.get(pk=1)
    template=loader.get_template("movies/index.html")
    context={
        'ab':"movie",
    }
    return HttpResponse(template.render(context,request))

def detail(request,movie_id):
   # movie = Movie.objects.get(pk=1)
    template=loader.get_template("movies/index1.html")
    context = {
        'ab1': movie_id,

    }
    return HttpResponse(template.render(context, request))
def count(request):
    data = request.GET['user']
    pass1 = request.GET['password1']
    return render(request,'movies/form.html',{ 'user2': data  ,'name2': pass1})
