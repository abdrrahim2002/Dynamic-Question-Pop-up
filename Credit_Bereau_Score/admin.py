from django.contrib import admin
from .models import Question, UserProfile, UserResponse
# Register your models here.

admin.site.register(Question)
admin.site.register(UserProfile)
admin.site.register(UserResponse)
