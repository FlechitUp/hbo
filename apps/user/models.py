from django.db import models
from django.contrib.auth.models import User #AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver

"""class User(models.Model):  # AbstractBaseUser):
    usuario = models.OneToOneField(User)
    nick_name = models.CharField(max_length=50, blank='False', null='False')
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, blank='False')   
    age = models.IntegerField()
    e_mail = models.CharField(max_length=50, blank='False')
    number_phone = models.IntegerField(blank='False', null='True')
    github = models.CharField(max_length=50)
    Student_Mentor = models.BooleanField(default=True)  # True = Student, False = Mentor   
    
    def __str__(self):
        return (self.name)
"""

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)   
    age = models.IntegerField(null='True')
    number_phone = models.IntegerField(blank='False', null='True')
    github = models.CharField(max_length=50, null='True')
    #Student_Mentor = models.BooleanField(default=True)  # True = Student, False = Mentor

    def __str__(self):
        return self.user.username # (self.name)


@receiver(post_save, sender=User)
def create_user_userprofileinfo(sender, instance, created, **kwargs):
    if created:
        UserProfileInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_userprofileinfo(sender, instance, **kwargs):
    instance.userprofileinfo.save()

"""
class Student2(UserProfileInfo):
    is_working = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Mentor(UserProfileInfo):
    is_mentorizing = models.BooleanField(default=False)
    
    def __str__(self):
        return (self.user.username)

class Program(models.Model):
    year = models.SmallIntegerField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return (self.title)

class Students_Mentor(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)  # One to many = foreign
    studentA = models.ForeignKey(Student2, null=True, related_name='studentA', on_delete=models.CASCADE)
    studentB = models.ForeignKey(Student2, null=True, related_name='studentB', on_delete=models.CASCADE)    
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)

class Courses_Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student2 = models.ForeignKey(Student2, on_delete=models.CASCADE)
    percentage = models.IntegerField()

    #def __str__(self):
    #    return (self._check_single_primary_key)
   
"""
