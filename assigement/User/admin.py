from django.contrib import admin
from .models import Post,user

# Register your models here.
admin.site.register(user)
admin.site.register(Post)

