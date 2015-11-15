from django.db import models

# Create your models here.
class Picture(models.Model):
	file = models.FileField(upload_to="songs")
	slug = models.SlugField(max_length=50, blank=True)
	
	def __unicode__(self):
		return unicode(self.file.name)

class song(models.Model):
	GENRES_CHOICES = (
        ('Alternative Music', 'Alternative Music'),
        ('Blues', ' Blues'),
        ('Classical Music', 'Classical Music'),
        ('Country Music', 'Country Music'),
    )
	picture = models.OneToOneField(Picture,primary_key=True)
	artist= models.CharField(max_length=200, blank=True,default="artist")
	album = models.CharField(max_length=200, blank=True,default="album")
	genre = models.CharField(max_length=200, blank=True,default="genre",choices=GENRES_CHOICES)
	tag = models.CharField(max_length=200, blank=True,default="tag")
	def __unicode__(self):
		
		return unicode(self.picture)
