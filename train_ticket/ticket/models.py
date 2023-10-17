from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=60)
    mobile=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=60)


class Ticket(models.Model):
    from_city=models.CharField(max_length=50)
    to_city=models.CharField(max_length=50)
    name=models.CharField(max_length=60)
    moblie=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=50)
    birth=models.CharField(max_length=50)


