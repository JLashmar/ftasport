from django.db import models
from django_countries.fields import CountryField

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
        return self.name
       #return 'Category: ' + self.name

    #def list_of_sports_in_category(self):
        #sport_cat = self.category.name
        #return sport_cat

    def get_absolute_url(self):
        return reverse('sports:sport-home', kwargs={'slug':self.sport_slug})

class Gender(models.Model):
    gender = models.CharField(max_length=50) #male/female

    def __str__(self):
       return self.gender

class Tier(models.Model):
    tier_level = models.CharField(max_length=50)

    def __str__(self):
       return self.tier_level

class MatchType(models.Model):
    name = models.CharField(max_length=250)
    tier = models.ForeignKey('Tier', on_delete=models.CASCADE)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)

    def __str__(self):
       return '%s %s' % (self.sport, self.name)

class Team(models.Model):
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    country = CountryField()
    team_name = models.CharField(max_length=250)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE)
    tier = models.ForeignKey('Tier', on_delete=models.CASCADE)

    def __str__(self):
       return self.team_name
