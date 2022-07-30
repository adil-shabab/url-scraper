from django.db import models

# Create your models here.
class Website(models.Model):
    domain = models.CharField(max_length=240)
    word_count = models.IntegerField()
    urls = models.TextField(null=True)
    images = models.TextField(null=True)
    
    def __str__(self):
        return self.domain


class Favourite(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

