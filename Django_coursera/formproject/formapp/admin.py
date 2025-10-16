from django.contrib import admin

# Register your models here.
from .models import Person 
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith", ) 