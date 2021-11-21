from django.contrib import admin
from .models import TutorialCategory, TutorialDetails

# Register your models here.
admin.site.register(TutorialCategory)
admin.site.register(TutorialDetails)