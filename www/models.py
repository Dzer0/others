#coding=utf-8
from django.db import models
from django import forms

# Create your models here.
class Members(models.Model):
    Email = models.EmailField()
    password = models.CharField(max_length=200)
    headimg = models.FileField(upload_to='./upload/')

    def __unicode__(self):
        return self.Email