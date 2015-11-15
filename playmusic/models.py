from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
        user = models.ForeignKey(User)
        Location= models.CharField(max_length=200, blank=True)
        Institute = models.CharField(max_length=200, blank=True)
        Home_Place= models.CharField(max_length=200, blank=True)
        Profile_Pic = models.ImageField(upload_to='PPic', blank=True)
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        phone_number = models.CharField(max_length=15,validators=[phone_regex], blank=True) # validators should be a list
	def __unicode__(self):
		return unicode(self.user)
