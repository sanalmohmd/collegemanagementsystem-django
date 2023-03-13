from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Hodregister(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=255,blank=False,null=False)
    hod_img=models.ImageField(null=True,blank=True,upload_to="images/")
    email=models.CharField(max_length=255,blank=False,null=False)
    department=models.CharField(max_length=255,blank=False,null=False)
    phoneno=models.CharField(max_length=255,blank=False,null=False)
    gender=models.CharField(max_length=255,blank=False,null=False)   
    qualification=models.CharField(max_length=255,blank=False,null=False)
    address=models.CharField(max_length=255,blank=False,null=False)
    pin=models.CharField(max_length=255,blank=False,null=False)
    status=models.CharField(max_length=255,blank=False,null=False)
    role=models.CharField(max_length=255,blank=False,null=False)


    def __str__(self):
        return self.fullname
    

class teacherregister(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    fullname=models.CharField(max_length=255,blank=False,null=False)
    teacher_img=models.ImageField(null=True,blank=True,upload_to="images/")
    email=models.CharField(max_length=255,blank=False,null=False)
    department=models.CharField(max_length=255,blank=False,null=False)
    phoneno=models.CharField(max_length=255,blank=False,null=False)
    gender=models.CharField(max_length=255,blank=False,null=False)   
    dob=models.DateField()
    qualification=models.CharField(max_length=255,blank=False,null=False)
    address=models.CharField(max_length=255,blank=False,null=False)
    pin=models.CharField(max_length=255,blank=False,null=False)
    state=models.CharField(max_length=255,blank=False,null=False)
    country=models.CharField(max_length=255,blank=False,null=False)
    status=models.CharField(max_length=255,blank=False,null=False)
    role=models.CharField(max_length=255,blank=False,null=False)


    def __str__(self):
        return self.fullname


class studentregister(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     fullname=models.CharField(max_length=255,blank=False,null=False)
     student_img=models.ImageField(null=True,blank=True,upload_to="images/")
     email=models.CharField(max_length=255,blank=False,null=False)
     year=models.CharField(max_length=255,blank=False,null=False)
     course=models.CharField(max_length=255,blank=False,null=False)
     department=models.CharField(max_length=255,blank=False,null=False)
     phoneno=models.CharField(max_length=255,blank=False,null=False)
     gender=models.CharField(max_length=255,blank=False,null=False) 
     address=models.CharField(max_length=255,blank=False,null=False)
     pin=models.CharField(max_length=255,blank=False,null=False)
     state=models.CharField(max_length=255,blank=False,null=False)
     country=models.CharField(max_length=255,blank=False,null=False)
     status=models.CharField(max_length=255,blank=False,null=False)
     role=models.CharField(max_length=255,blank=False,null=False)
    


     def __str__(self):
        return self.fullname   


class leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    purpose=models.CharField(max_length=255,blank=False,null=False)
    date=models.DateField()
    department=models.CharField(max_length=255,blank=False,null=False)
    status=models.CharField(max_length=255,blank=False,null=False)
    role=models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.purpose



# class exam(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     department=models.CharField(max_length=255,blank=False,null=False)   
#     subject=models.CharField(max_length=255,blank=False,null=False)
#     time=models.TimeField()
#     date=models.DateField()
#     status=models.CharField(max_length=255,blank=False,null=False)
#     role=models.CharField(max_length=225,blank=False,null=False)

#     def __str__(self):
#         return self.subject
            
class exam(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(max_length=10)
    subject=models.CharField(max_length=100)
    role=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    department=models.CharField(max_length=40)
    def __str__(self):
        return self.subject



class mark(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=40)
    subject=models.CharField(max_length=40)
    total=models.CharField(max_length=40)
    mymark=models.CharField(max_length=40)
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.subject

