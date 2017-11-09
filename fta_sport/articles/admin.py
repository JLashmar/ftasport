from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostArticle(admin.ModelAdmin):
    list_display = ('title', 'body', 'headline_image', 'post_image')
    prepopulated_fields = {'post_slug': ('title',)}
