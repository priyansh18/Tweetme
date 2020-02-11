from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Tweet(models.Model):
    user        =      models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=None )
    content      =     models.CharField(max_length=350)
    updated    =       models.DateTimeField(auto_now=True)
    timestamp    =     models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def clean(self,*args,**kwargs):
        content = self.content
        if content == 'any' :
            raise ValidationError('cannot be null')
        else:
            return super(Tweet,self).clean(*args,**kwargs)


