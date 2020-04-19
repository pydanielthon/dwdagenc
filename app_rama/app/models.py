from django.db import models
from django_resized import ResizedImageField




class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    typee = models.CharField(max_length=10000)
    img = ResizedImageField(size=[698, 339], crop=['middle', 'center'])
    description = models.TextField()#Duze pole tekstwe
    url = models.URLField(max_length=200, default=False)

    def __str__(self):
        return self.name

class Mails(models.Model):
    email =     models.EmailField() 
    subject =   models.CharField(max_length=1000)
    message = models.CharField(max_length=20000)
    document = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.email  