from django.db import models
class Room(models.Model):
    Block_Name = models.CharField(max_length=255)
   # student = models.CharField(max_length=255)
    Room_Number = models.IntegerField()
    Bed_Availabel=models.IntegerField()
    Student_Name = models.CharField(max_length=255)


    def __str__(self):
        a = self.Room_Number
        a=str(a)
        return (a)
class Student(models.Model):
    Image=models.ImageField(upload_to='images/')
    Registration_Number=models.IntegerField()
    Student_Name =models.CharField(max_length=255)
    Gender=models.CharField(max_length=10)
    Course=models.CharField(max_length=100)
    Blood_Group=models.CharField(max_length=4)
    Date_of_birth=models.DateField()
    Mobile_Number=models.IntegerField()
    Mobile_Number2=models.IntegerField()
    Email_id=models.EmailField()
    Father_Name=models.CharField(max_length=255)
    Father_Mobile_Number=models.IntegerField()
    Father_Mobile_Number2 = models.IntegerField()
    Address=models.TextField()
    City=models.CharField(max_length=255)
    State=models.CharField(max_length=255)
    Hostel_Fees=models.CharField(max_length=255)
    Mess_Fees=models.CharField(max_length=255)
    Room_Number= models.ForeignKey(Room, on_delete=models.CASCADE)
    #a=(Student_Name,Room_Number)

    def __str__(self):
        return (self.Student_Name)
    #student report

class Complain(models.Model):
    subject=models.CharField(max_length=100)
    body=models.TextField()
   # date=models.DateField()
    def __str__(self):
        return (self.subject)


class Notice(models.Model):
    Date=models.DateField()
    subject=models.CharField(max_length=100)
    notice=models.TextField()


    def __str__(self):
        return (self.subject)









