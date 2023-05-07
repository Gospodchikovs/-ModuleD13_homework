from django.contrib import admin
from .models import Advertisment, Category, Subscriber, Comment, Profile

# Register your models here.
admin.site.register(Advertisment)
admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(Profile)