from django.db import models

# Create your models here.


class Contact(models.Model):

    NAME = models.CharField(max_length=250)
    DOB = models.DateField()
    AGE = models.IntegerField()
    EMAIL_ID = models.EmailField()
    PHONENUMBER = models.IntegerField()
    GENDER = models.CharField(max_length=250)
    ADDRESS = models.TextField()
    DISTRICT = models.CharField(max_length=250)
    BRANCHES = models.CharField(max_length=250)
    ACCOUNT_TYPE = models.CharField(max_length=250)
    MATERIALS_PROVIDE = models.CharField(max_length=250)

    def __str__(self):
        return self.NAME
