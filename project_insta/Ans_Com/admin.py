from django.contrib import admin

from .models import Answer

# Register your models here.


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'content', 'create_date', 'owner']
    list_display_links = ['content', 'create_date']












