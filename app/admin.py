from django.contrib import admin
from app.models import NewsModel

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
admin.site.register(NewsModel, NewsAdmin)

