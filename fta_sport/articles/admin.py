from django.contrib import admin

from .models import Post, Sport

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostArticle(admin.ModelAdmin):
    list_display = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
