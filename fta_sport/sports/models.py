from django.db import models

# Create your models here.

class Sport_Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category_slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.name

    def __str__(self):
       return  self.name

   #def get_absolute_url(self):
       #return reverse('sports:sport-category', kwargs={'slug':self.category_slug})

class Sport(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    sport_slug = models.SlugField(max_length=100, db_index=True)
    category = models.ForeignKey('Sport_Category', on_delete=models.CASCADE,)

    def __unicode__(self):
        return '%s' % self.name

    def __str__(self):
       return 'Category: ' + self.name

    #def list_of_sports_in_category(self):
        #sport_cat = self.category.name
        #return sport_cat

    def get_absolute_url(self):
        return reverse('sports:sport-home', kwargs={'slug':self.sport_slug})
