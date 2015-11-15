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
from recommendation.models import Reclist
import json


def addtomyfriendreclist(request):
    context = RequestContext(request)
    to_user_id = None
    rec_song_id = None
    if request.method == 'GET':
        to_user_id = request.GET['to_user_id']
        rec_song_id = request.GET['rec_song_id']
    if rec_song_id:
        rec_song = Picture.objects.get(id=int(rec_song_id))
        to_user = User.objects.get(pk=int(to_user_id))
        if rec_song:
            make = Reclist(song = rec_song, sender = request.user, receiver = to_user)
            make.save()
    return HttpResponse("Success")

def clearmylist(request):
    rec_list = Reclist.objects.filter(receiver = request.user).filter(read_status = False)
    for entry in rec_list:
        entry.read_status = True
        entry.save()
    return HttpResponse('updated')
