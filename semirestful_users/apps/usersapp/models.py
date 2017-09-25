from __future__ import unicode_literals
import re
from django.db import models


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UsersManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # check all fields for emptyness
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is required".format(field.replace('_', ''))

            # check name fields for min length
            if field == "first_name" or field == "last_name":
                if not field in errors and len(value) < 3:
                    errors[field] = "{} field must be at least 3 characters".format(field.replace('_', ''))

        # check email field for valid email
        if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "invalid email"
        
        # if email is valid check db for existing email
        else:
                if len(self.filter(email=post_data['email'])) > 1:
                    errors['email'] = "email already in use"

        return errors


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()
    def __str__(self):
        printout = str(self.id) + " " + str(self.first_name) + " " + str(self.last_name) + " " + str(self.email)
        return printout

