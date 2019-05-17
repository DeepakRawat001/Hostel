from django.contrib import admin
from .models import Student,Notice,Complain,Room,Hotel,Detail,Feedback,Notification
from django.contrib.auth.models import Group
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Student_Name',"Course")
    list_filter =("Course","Gender")
    # list_display=("Student_Name","Course")

class RoomAdmin(admin.ModelAdmin):
    #a=("Room_Number","Bed_Number")
    list_filter = ("Room_Number","Bed_Availabel")
    list_display =("Room_Number","Bed_Availabel")
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject','notice')

class ComplainAdmin(admin.ModelAdmin):
    list_display = ('subject','date')

admin.site.register(Student,StudentAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Complain,ComplainAdmin)
admin.site.register(Hotel)
admin.site.register(Detail)
admin.site.register(Feedback)
admin.site.register(Notification)
