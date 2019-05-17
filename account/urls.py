from django.conf.urls import  url
from . import  views
urlpatterns = [
    url(r'logout', views.logout, name='logout'),
    url(r'search', views.search, name='search'),
    url(r'result1', views.result1, name='result1'),
    url(r'notice', views.notice,name='notice'),
    url(r'detail', views.detail, name='detail'),
    url(r'room',views.room,name='room'),
    url(r'complain',views.complain,name='complain'),
    url(r'hello',views.hello,name='hello'),
    url(r'seat',views.seat,name='seat'),
    url(r'check',views.check,name='check'),
    url('add',views.add,name="add"),
    url('contact',views.contact,name='contact'),
    url('register',views.register,name="register"),
    url('about', views.about, name="about"),
    url(r'login', views.login, name='login'),
    url(r'signup', views.signup, name='signup'),
    url(r'create',views.create,name='create'),
    url('studentRegister',views.studentRegister,name="studentRegister"),
    url('image',views.hotel,name="hotel"),
    url('success',views.success,name="success"),
    url('media',views.media,name="media"),
    url(r'change_password/$', views.change_password, name='change_password'),
    url(r'password_changed',views. password_changed,name= "password_changed"),
    url(r'forget_password',views.forget_password,name='forget_password'),
    url(r'otp',views.otp,name="otp"),
    url(r'confirm_password',views.confirm_password,name="confirm_password"),
    url(r'entry',views.entry,name="entry"),
    url(r'submit',views.submit,name="submit"),
    url("xyz",views.xyz,name="xyz"),
    #url(r'login', views.login, name='login'),
    url(r'', views.home, name='home'),

   #
    #url(r'deepak', views.deepak, name='deepak'),






]