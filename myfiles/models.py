from django.db import models

# Create your models here.

class raxbar(models.Model):
  direktor = models.CharField(max_length=45)
  yoordamchisi = models.CharField(max_length=45)
  madanyatchi = models.CharField(max_length=45)
  sekretar = models.CharField(max_length=45)

class Xaqida(models.Model):
  xonalar = models.CharField(max_length=10)
  oshxona = models.CharField(max_length=10)
  sport = models.CharField(max_length=10)
  malumot = models.CharField(max_length=100)

class News(models.Model):
  rasim = models.ImageField(upload_to='media')
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=500)

class Talim(models.Model):
  rasimt = models.ImageField(upload_to='media')
  namet = models.CharField(max_length=100)
  titlet = models.CharField(max_length=500)

class Sharoyit(models.Model):
  rasims = models.ImageField(upload_to='media')
  names = models.CharField(max_length=100)
  titles = models.CharField(max_length=500)

class Murojat(models.Model):
  fish = models.CharField(max_length=100)
  otasi = models.CharField(max_length=100)
  onasi = models.CharField(max_length=100)
  rasim = models.ImageField(upload_to='media')
  malumot = models.TextField()
  raqam = models.CharField(max_length=12)
  vaqt = models.DateTimeField(auto_now=True)


