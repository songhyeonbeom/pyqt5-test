from django.contrib import admin

from .models import Answer

# Register your models here.
admin.site.register(Answer,)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('content', 'create_date', 'owner',)
    search_fields = ['content']















