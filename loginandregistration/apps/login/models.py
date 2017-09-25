from __future__ import unicode_literals
import re
from django.db import models


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UsersManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        password = ""
        if post_data['formtype'] == 'register':
            # check all fields for emptyness
            for field, value in post_data.iteritems():
                if len(value) < 1:
                    errors[field] = "{} field is required".format(field.replace('_', ''))

                # check name fields for min length
                if field == "first_name" or field == "last_name":
                    if not field in errors and len(value) < 2:
                        errors[field] = "{} field must be at least 2 characters".format(field.replace('_', ''))

                if field == "password":
                    password = value
                    if len(value) < 8:
                        errors[field] = "{} field must be at least 8 characters".format(field.replace('_', ''))

                # check password & confirmation fields for match
                if field == "passwordconf":
                    password = post_data['password']

                    if not field in errors and value != password:
                        errors[field] = "{} and confirmation do not match".format(field.replace('_', ''))



            # check email field for valid email
            if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
                errors['email'] = "invalid email"
            
            # if email is valid check db for existing email
            else:
                    if len(self.filter(email=post_data['email'])) > 1:
                        errors['email'] = "email already in use"


        if post_data['formtype'] == 'login':
            if len(self.filter(email=post_data['email'])) < 1:
                errors['email'] = "No User found with that email"


        

        return errors

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)    
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    isnew = models.CharField(max_length=3)
    objects = UsersManager()

    def __str__(self):
        printout = str(self.id) + " " + str(self.first_name) + " " + str(self.last_name) + " " + str(self.email + " " + str(self.password))
        return printout
