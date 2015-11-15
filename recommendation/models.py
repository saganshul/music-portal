from django.db import models
from django.contrib.auth.models import User
from fileupload.models import Picture

class Reclist(models.Model):
    song = models.ForeignKey(Picture, related_name='rec_song')
    sender = models.ForeignKey(User,related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    time = models.DateTimeField(auto_now_add=True)
    read_status=models.BooleanField(default=False)
    def __unicode__(self):
        return unicode(self.id)
