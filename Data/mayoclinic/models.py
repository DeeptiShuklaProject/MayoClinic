from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
class Mayoclinic(models.Model):
    mayoclinic_title=models.CharField(max_length=100)
    mayoclinic_desc=HTMLField()
    mayoclinic_image=models.FileField(upload_to="mayoclinic/",max_length=250,null=True,default=None)
    mayoclinic_slug=AutoSlugField(populate_from='mayoclinic_title',unique=True,null=True,default=None)


# Create your models here.
