from django.contrib import admin
from .models import BoardMember

class BoardMemberAdmin(admin.ModelAdmin):
	list_display = ('position', 'name')

admin.site.register(BoardMember, BoardMemberAdmin)
