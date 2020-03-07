from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Session)
admin.site.register(UserMetaData)
admin.site.register(Game)