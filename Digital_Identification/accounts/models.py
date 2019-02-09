from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.
# def userDir(instance,filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

class Beneficiary(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='beneficiary')
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    date_of_birth=models.DateTimeField()
    gender=models.CharField(max_length=50,choices=(('male','male'),('female','female')))
    displacement_reason=models.CharField(max_length=50,choices=(('r1','reason1'),('r2','reason2')))
    number_of_familymembers=models.PositiveIntegerField()
    disabilities=models.CharField(max_length=50,choices=(('blind','Visual Impairment'),('deaf','Hearing Impairment'),('mute','Speech Impairment'),('amputee','Amputee')))
    country_of_origin=models.CharField(max_length=50,choices=tuple(json.load(open("out.json"))))
    photo=models.CharField(max_length=255,default='Images/def.jpeg')
    def __str__(self):
        return self.user.username

class Image(models.Model):
    img=models.CharField(max_length=255,null=True)
    uploader=models.ForeignKey(Beneficiary,on_delete=models.CASCADE,null=True,related_name='img')
