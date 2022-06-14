from django.contrib import admin

# Register your models here.
#user:admin
#pass:1234

from .models import Question,Articulo

admin.site.register(Question),
admin.site.register(Articulo)