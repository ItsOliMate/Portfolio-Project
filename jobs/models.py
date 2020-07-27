from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length = 100)
    summary = models.CharField(max_length =250)
    startdate = models.CharField(max_length = 10)
    enddate = models.CharField(max_length = 10)

    def __str__(self):
        return self.title

class Detail(models.Model):
    about = models.CharField(max_length =300)

class Skill(models.Model):
    logo = models.ImageField(upload_to="images/")
    name = models.CharField(max_length =20)
    experience = models.CharField(max_length =15)

    def __str__(self):
        return self.name

class Project (models.Model):
    title = models.CharField(max_length =300)
    info = models.CharField(max_length =450)
    codeused = models.CharField(max_length =100)

    def __str__(self):
        return self.title

class Education (models.Model):
    subject = models.CharField(max_length =30)
    type = models.CharField(max_length =30)
    info = models.CharField(max_length =30)

    def __str__(self):
        return self.title
