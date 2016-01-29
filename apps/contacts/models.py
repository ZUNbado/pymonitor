from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NotificationMethod(models.Model):
    name = models.CharField(max_length=255)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    notification = models.ForeignKey(NotificationMethod)
    user = models.ForeignKey(User)

class ContactGroup(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)

class ContactGroupRelations(models.Model):
    contact = models.ForeignKey(Contact)
    group = models.ForeignKey(ContactGroup)
