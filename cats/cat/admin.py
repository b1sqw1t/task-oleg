from django.contrib import admin
from cat.models import Cat

class CatAdmin(admin.ModelAdmin):
    list_display = ('User','Name','Age','Breed','Hairiness','Created','Changed')

admin.site.register(Cat,CatAdmin)