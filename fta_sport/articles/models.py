from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from sports.models import Sport, Sport_Category

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    post_slug = models.SlugField(max_length=100, unique=True)
    short_description = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField()
    headline_image = models.FileField(blank=True, null=True)
    post_image = models.FileField(blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    post_category = models.ForeignKey('sports.Sport', related_name='post_category')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'slug':self.post_slug})
