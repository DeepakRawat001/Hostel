from django.db import models

class Student(models.Model):
    Image=models.ImageField()
    Registration_Number=models.IntegerField()
    Student_Name =models.CharField(max_length=255)
    Gender=models.CharField(max_length=10)
    Course=models.CharField(max_length=100)
    Blood_Group=models.CharField(max_length=4)
    Date_of_birth=models.DateField()
    Mobile_Number=models.IntegerField()
    Email_id=models.CharField(max_length=255 )
    Father_Name=models.CharField(max_length=255)
    Father_Mobile_Number=models.IntegerField()
    Address=models.TextField()
    #City=models.CharField(max_length=255)
    #State=models.CharField(max_length=255)
    #Hostel_Fees=models.CharField(max_length=255)
    #Mess_Fees=models.CharField(max_length=255)
   # Room_Number= models.ForeignKey(Room, on_delete=models.CASCADE)
    #a=(Student_Name,Room_Number)


'''  def __str__(self):
        a = self.id
        a = str(a)
        return (a)'''
class Room(models.Model):
    Block_Name = models.CharField(max_length=255)
   # student = models.CharField(max_length=255)
    Room_Number = models.IntegerField()
    Bed_Availabel=models.IntegerField()
    Student_Name = models.CharField(max_length=255)
    Floor=models.CharField(max_length=255)
    Registration_Number=models.CharField(max_length=255)
    '''def __str__(self):
        a = self.Room_Number
        a=str(a)
        return (a)'''

class Complain(models.Model):
    student_name=models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject=models.CharField(max_length=100)
    roll_no = models.IntegerField()
    body=models.TextField()
    date=models.DateField()




class Notice(models.Model):
    #Date=models.DateField()
    subject=models.CharField(max_length=100)
    notice=models.TextField()
    date = models.DateField()






class Hotel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    email=models.CharField(max_length=150,default="bknfdvnk")

class Detail(models.Model):
    username=models.CharField(max_length=250)
    #password=models.CharField(max_length=25)
    email=models.CharField(max_length=255)
    code=models.IntegerField(max_length=4,default=0)

class Feedback(models.Model):
    username=models.CharField(max_length=250)
    email = models.CharField(max_length=255)
    phone_no=models.IntegerField(max_length=14,default=0)
    message=models.TextField()

class Notification(models.Model):
    Subject=models.CharField(max_length=250)
    Body = models.TextField()

    def __str__(self):
        return (self.Subject)





