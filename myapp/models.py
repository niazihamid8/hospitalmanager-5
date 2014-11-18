from django.db import models

# Create your models here.

class user(models.Model):
    un = models.CharField(max_length=30)
    pw = models.CharField(max_length=50)


class RSS(models.Model):
    Link = models.CharField(max_length=150)
    Agency = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
class Member(models.Model):
    email=models.EmailField(max_length=50)
    fn=models.CharField(max_length=50)
    ln=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
