

# Create your models here.
from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.urls import reverse

from django.conf import settings


dpt_choices=(('CSE','CSE'),('ETE','ETE'),('EEE','EEE'),('DBA','DBA'),('EBA','EBA'),('FME','FME'),)
batch_choices=(('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),
              ('06','06'),('07','07'),('08','08'),('09','09'),('10','10'),
              ('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),
              ('16','16'),('17','17'),('18','18'),('9','9'),('20','20'),
              ('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),
              ('26','26'), ('27','27'), ('28','28'), ('29','29'), ('30','30'),
              ('31','31'), ('32','32'), ('33','33'), ('34','34'), ('35','35'), 
              ('36','36'), ('37','37'), ('38','38'), ('39','39'),('40','40'),
              ('41','41'), ('42','42'), ('43','43'), ('44','44'), ('45','45'), 
              ('46','46'), ('47','47'), ('48','48'), ('49','49'),('50','50'),)
MALE='male'
FEMALE='female'
gender_choices=((MALE,"Male"),(FEMALE,'Female'),)
# Create your models here.
# This is for personal data
class StudentRegistration(AbstractUser):
    username=models.CharField(unique=True,max_length=7,default='C143027',help_text='Please Enter Your Student ID')	
    full_name = models.CharField(max_length=100,help_text='Please Use Block Letter')
    address1=models.CharField(max_length=150,help_text='Please Use Block Letter')
    address2=models.CharField(max_length=150,help_text='Please Use Block Letter')
    email=models.EmailField()
    mobile_number=models.CharField(max_length=14,default='+8801836917507')
    gender=models.CharField(max_length=7,choices=gender_choices,default=MALE)
    dpt=models.CharField(max_length=5,choices=dpt_choices,default='CSE')
    batch_number=models.CharField(max_length=5,choices=batch_choices,default='39')

    def __str__(self):
        return self.username

class GroupCreation(models.Model):
    group_name= models.CharField(unique=True,max_length=71)
    member_1 = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = 'member_1')
    member_2 = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = 'member_2')
    member_3 = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = 'member_3')
    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse("create", kwargs={"id": self.id})
