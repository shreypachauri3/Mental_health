from django.db import models
from django.forms import CharField



class basicinfo(models.Model):
    name=models.CharField(max_length=50,default=' ')
    timepass=models.CharField(max_length=80,default=' ')



class final(models.Model):
    qid=models.IntegerField(default=0)
    option=models.CharField(max_length=200,default=' ')
    img=models.URLField(max_length=1000,default=' ')
    def __str__(self):
        return self.option

class questions(models.Model):
    qid=models.IntegerField()
    ques=models.CharField(max_length=800,default=' ')
    op1=models.CharField(max_length=800,default=' ')
    op2=models.CharField(max_length=800,default=' ')
    op3=models.CharField(max_length=800,default=' ')
    op4=models.CharField(max_length=800,default=' ')
    ans=models.CharField(max_length=800,default=' ')
    def __str__(self):
        return self.ques


class res(models.Model):
    responce=models.CharField(max_length=80)
    def __str__(self):
        return self.responce