from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	exclude = ('body',)

admin.site.register(Story, StoryAdmin)