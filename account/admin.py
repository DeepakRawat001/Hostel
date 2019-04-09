from django.contrib import admin
from .models import Student,Notice,Complain,Room
from django.contrib.auth.models import Group
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Student_Name','Room_Number',"Course")

   # list_display=("Student_Name","Course")

class RoomAdmin(admin.ModelAdmin):
    #a=("Room_Number","Bed_Number")
    list_filter = ("Room_Number","Bed_Availabel")

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject','Date')

admin.site.register(Student,StudentAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Complain)

