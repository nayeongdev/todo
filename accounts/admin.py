from django.contrib import admin
from django.contrib.auth.models import Group
from accounts.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.unregister(Group)
