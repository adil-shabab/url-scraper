from django.db import models

# Create your models here.
class Website(models.Model):
    domain = models.CharField(max_length=240)
    word_count = models.IntegerField()
    urls = models.ManyToManyField('Url')
    images = models.ManyToManyField('Images')
    
    def __str__(self):
        return self.domain


class Url(models.Model):
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url

class Images(models.Model):
    image = models.ImageField(upload_to='media')
