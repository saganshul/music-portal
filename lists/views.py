from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.contrib.auth.models import User
from fileupload.models import Picture,song
from lists.models import Playlist, Fav
import json

def addtoplaylist(request):
    context = RequestContext(request)
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['playlist_song_id']
    if cat_id:
        song = Picture.objects.get(id=int(cat_id))
        if song:
            make = Playlist(song = song, user = request.user)
            make.save()
    return HttpResponse("Success")

def addtofav(request):
    context = RequestContext(request)
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['fav_song_id']
    if cat_id:
        song = Picture.objects.get(id=int(cat_id))
        if song:
            make = Fav(song = song, user = request.user)
            make.save()
    return HttpResponse("Success")

# Create your views here.
