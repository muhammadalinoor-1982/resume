from django.db import models

# Create your models here.
class Personal(models.Model):

    name        =models.CharField    (max_length=30, null=True, blank=True)
    email       =models.EmailField   (max_length=30, null=True, blank=True)
    phone       =models.CharField    (max_length=13, null=True, blank=True)
    address     =models.TextField    (max_length=80, null=True, blank=True)
    github      =models.CharField    (max_length=40, null=True, blank=True)
    linkedin    =models.CharField    (max_length=40, null=True, blank=True)
    instagram   =models.CharField    (max_length=40, null=True, blank=True)
    facebook    =models.CharField    (max_length=40, null=True, blank=True)
    tag_line    =models.TextField    (max_length=50, null=True, blank=True)
    heading     =models.CharField    (max_length=30, null=True, blank=True)
    description =models.TextField    (max_length=350, null=True, blank=True)
    image       =models.ImageField   (upload_to='me/', default='noImg/no_img.jpg', null=True, blank=True)

class Work_Experience(models.Model):

    name            =models.CharField   (max_length=30, null=True, blank=True)
    position        =models.CharField   (max_length=20, null=True, blank=True)
    job_description =models.TextField   (max_length=350, null=True, blank=True)
    joining_date    =models.CharField   (max_length=15, null=True, blank=True)
    resigning_date  =models.CharField   (max_length=15, null=True, blank=True)
    image           =models.ImageField  (upload_to='experience/', default='noImg/no_img.jpg', null=True, blank=True)

class Education(models.Model):
    name        =models.CharField   (max_length=40, null=True, blank=True)
    degree      =models.CharField   (max_length=40, null=True, blank=True)
    major       =models.CharField   (max_length=25, null=True, blank=True)
    logo        =models.ImageField  (upload_to='logo/', default='noImg/no_img.jpg', null=True, blank=True)
    image       =models.ImageField  (upload_to='certificate/', default='noImg/no_img.jpg', null=True, blank=True)
    location    =models.CharField   (max_length=20, null=True, blank=True)

class Training(models.Model):
    name        =models.CharField   (max_length=30, null=True, blank=True)
    institute   =models.CharField   (max_length=25, null=True, blank=True)
    description =models.CharField   (max_length=60, null=True, blank=True)
    image       =models.ImageField  (upload_to='certificate/', default='noImg/no_img.jpg', null=True, blank=True)

class Skills(models.Model):
    name        =models.CharField   (max_length=25, null=True, blank=True)
    potentials  =models.CharField   (max_length=15, null=True, blank=True)
    image       =models.ImageField  (upload_to='logo/', default='noImg/no_img.jpg', null=True, blank=True)

class Portfolio(models.Model):
    name        =models.CharField   (max_length=30, null=True, blank=True)
    description =models.TextField   (max_length=40, null=True, blank=True)
    gitlink     =models.CharField   (max_length=30, null=True, blank=True)
    projectURL  =models.CharField   (max_length=30, null=True, blank=True)
    image      =models.ImageField  (upload_to='project/', default='noImg/no_img.jpg', null=True, blank=True)

class Platform(models.Model):
    name        =models.CharField   (max_length=20, null=True, blank=True)
    image       =models.ImageField  (upload_to='logo/', default='noImg/no_img.jpg', null=True, blank=True)

class Language(models.Model):
    name        =models.CharField   (max_length=15, null=True, blank=True)
    potentials  =models.CharField   (max_length=15, null=True, blank=True)

class Reference(models.Model):
    name        =models.CharField   (max_length=25, null=True, blank=True)
    designation =models.CharField   (max_length=60, null=True, blank=True)
    relation    =models.CharField   (max_length=15, null=True, blank=True)
    email       =models.EmailField  (max_length=35, null=True, blank=True)
    phone       =models.CharField   (max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.name)