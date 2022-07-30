from django.contrib import admin
from .models import Website, Images, Url
# Register your models here.


admin.site.register(Website)
admin.site.register(Url)
admin.site.register(Images)