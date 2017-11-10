from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostArticle(admin.ModelAdmin):
    list_display = ('title', 'post_category', 'headline_image', 'post_image', 'posted')
    prepopulated_fields = {'post_slug': ('title',)}
