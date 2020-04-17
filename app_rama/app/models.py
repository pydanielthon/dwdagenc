from django.db import models
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=200)

    #ponizsze linie zwroca nazwwe kategori zamiast nazwy obiektu
    #sprobouj sobie je usunac i przejsc do admina
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()#Duze pole tekstwe
    img = ResizedImageField(size=[698, 339], crop=['middle', 'center'])
    #powyzsza linia kodu ResizeImage automatycznie obrobi twoje zdjecie przed zapisem w bazie danych
    #do rozmiarow podanych w size, oraz wykarduje na srodek poczytaj sobie
    # - dokumentacja "https://pypi.org/project/django-resized/"

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    typee = models.CharField(max_length=100)
    img = ResizedImageField(size=[698, 339], crop=['middle', 'center'])
    description = models.TextField()#Duze pole tekstwe
    url = models.URLField(max_length=200, default=False)

    def __str__(self):
        return self.name