from django.contrib import admin

from .models import Post, Sport

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sport')
    prepopulated_fields = {'slug': ('title',)}

    def sport(self, object):
        return "\n".join([a.title for a in obj.sport.all()])

@admin.register(Post)
class PostArticle(admin.ModelAdmin):
    list_display = ('title', 'body')
