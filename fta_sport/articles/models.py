from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from sports.models import Sport, Sport_Category

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('Sport', related_name='category')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'slug':self.slug})

class Sport(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
       return 'Sport: ' + self.title

    @permalink
    def get_absolute_url(self):
        return ('view_sport', None, { 'slug': self.slug })
