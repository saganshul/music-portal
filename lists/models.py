from django.db import models
from django.contrib.auth.models import User
from fileupload.models import Picture

class Playlist(models.Model):
    song = models.ForeignKey(Picture)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.user)

class Fav(models.Model):
    song = models.ForeignKey(Picture)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return unicode(self.user)
