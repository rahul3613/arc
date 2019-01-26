from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from authtools.models import User
from .models import *

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ['name', 'email', 'password']

class UserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.register(Course)
admin.site.register(School)
admin.site.register(Itr)
admin.site.register(Item)
admin.site.register(CommentReport)
admin.site.register(UserReport)
admin.site.register(ItemReport)

