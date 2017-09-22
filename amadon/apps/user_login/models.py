from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "First Name: {}, Last Name: {}, Email: {}, Age: {}>".format(self.first_name, self.last_name, self.email, self.age)

