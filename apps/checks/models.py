from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheckType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self): return u'%s' % self.name

class CheckTypeAttribute(models.Model):
    check_type = models.ForeignKey(CheckType)
    name = models.CharField(max_length=255)
    required = models.BooleanField()
    attribute_type = models.CharField(max_length=255)

    def __unicode__(self): return u'%s' % self.name

class Check(models.Model):
    label = models.CharField(max_length=255)
    check_type = models.ForeignKey(CheckType)
    user = models.ForeignKey(User)
    check_interval = models.IntegerField(default=60)
    status = models.CharField(max_length=20, blank=True, null=True)
    last_checked = models.DateTimeField(blank=True, null=True)
    max_confirmations = models.IntegerField(default=3)
    confirmations = models.IntegerField(blank=True, null=True)
    lock = models.CharField(max_length=16, blank=True, null=True)
    last_locked = models.DateTimeField(blank=True, null=True)

    def __unicode__(self): return u'%s' % self.label

    def save(self, **kwargs):
        super(Check, self).save(**kwargs)
        for attr in CheckTypeAttribute.objects.filter(check_type = self.check_type):
            CheckAttribute.objects.get_or_create(check_id = self, check_type_attribute = attr)

class CheckAttribute(models.Model):
    check_id = models.ForeignKey(Check)
    check_type_attribute = models.ForeignKey(CheckTypeAttribute)
    value = models.CharField(max_length=255)

    def __unicode__(self): return u'%s' % self.check_type_attribute.name
