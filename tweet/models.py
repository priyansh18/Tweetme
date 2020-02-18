from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse

# Create your models here.
class TweetManager(models.Manager):
    def like_toggle(self,user,tweet_obj):
        if user in tweet_obj.liked.all():
            is_liked = False
            tweet_obj.liked.remove(user)
        else:
            is_liked = True
            tweet_obj.liked.add(user)
        return is_liked    



class Tweet(models.Model):
    user        =      models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=None )
    content      =     models.CharField(max_length=120)
    liked       =      models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='liked')
    updated    =       models.DateTimeField(auto_now=True)
    timestamp    =     models.DateTimeField(auto_now_add=True)

    objects = TweetManager()

    def __str__(self):
        return str(self.content)

    def clean(self,*args,**kwargs):
        content = self.content
        if content == 'any' :
            raise ValidationError('cannot be null')
        else:
            return super(Tweet,self).clean(*args,**kwargs)
    
    class Meta:
        ordering = ['timestamp']        


