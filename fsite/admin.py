from django.contrib import admin
from .models import Advertisment, Category, Subscriber, Comment

# Register your models here.
admin.site.register(Advertisment)
admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(Comment)
