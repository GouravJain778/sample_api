from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','roll']






