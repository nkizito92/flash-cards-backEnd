from django.contrib import admin

# Register your models here.
# added the created model and import the class
from .models import Word
# register the class like so: 
admin.site.register(Word)