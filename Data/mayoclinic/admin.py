from django.contrib import admin
from mayoclinic.models import Mayoclinic

class MayoclinicAdmin(admin.ModelAdmin):
    list_display=('mayoclinic_title','mayoclinic_desc','mayoclinic_image')

admin.site.register(Mayoclinic,MayoclinicAdmin)

# Register your models here.
