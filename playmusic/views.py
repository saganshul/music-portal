from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from form import MyRegistrationForm
from .models import Profile
from fileupload.models import Picture,song
import json
from django.db.models import Q
from recommendation.models import Reclist
from lists.models import Fav, Playlist
from mutagenwrapper import read_tags
from django.conf import settings
playlist=[]
def index(request):
	return render(request, 'playmusic/index.html')
def register_user(request):
    c={}
    c.update(csrf(request))
    return render_to_response('playmusic/register.html',c)
def register_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	cpassword=request.POST.get('cpassword','')
	email=request.POST.get('email','')
	first_name=request.POST.get('first_name','')
	last_name=request.POST.get('last_name','')
	if password==cpassword:
		try:
			user = User.objects.create_user(username,email, password)
			user.save()
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			user=auth.authenticate(username=username,password=password)
			auth.login(request,user)
			return HttpResponseRedirect('/playmusic/loggedin')
		except:
			return HttpResponseRedirect('/playmusic/usernameinvalid')
	else:
		return HttpResponseRedirect('/playmusic/passwordinvalid')
def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('playmusic/login.html',c)
def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/playmusic/loggedin/')
	else:
		return HttpResponseRedirect('/playmusic/invalid/')

def loggedin(request):
	if request.user.is_authenticated():
		rec_list = Reclist.objects.filter(receiver = request.user).filter(read_status = False).order_by('-time')[:20]
		len_rec_list = len(rec_list)
		dict1= { 'user':request.user, 'playlist':playlist,'rec_list':rec_list,'len_rec_list':len_rec_list }

		return render_to_response('playmusic/loggedin.html',dict1)
	else:
		return redirect('playmusic.views.login')
def logout(request):
	auth.logout(request)
	return redirect('playmusic.views.index')
def invalid(request):
	c={}
	c.update(csrf(request))
	return render_to_response('playmusic/invalid.html',c)
def usernameinvalid(request):
	c={}
	c.update(csrf(request))
	return render_to_response('playmusic/usernameinvalid.html',c)
def passwordinvalid(request):
	c={}
	c.update(csrf(request))
	return render_to_response('playmusic/passwordinvalid.html',c)
def profile(request,user_id):
	try:
		myuser = Profile.objects.get(user=user_id)
	except Profile.DoesNotExist:
		raise Http404("User does not exist")
	return render(request, 'playmusic/profile.html', {'myuser': myuser })

def search(request):
	context = RequestContext(request)
	results=[]
	if request.method == 'GET':
		name=request.GET['name']
	rsong=name.replace(' ','_')
	results = Picture.objects.filter(file__icontains = rsong )
	no_of_results = len(results)
	dict2={'results': results,'playlist':playlist,'no_of_results' : no_of_results}
	return render_to_response('playmusic/searchresults.html',dict2,context)
def playlistmaker(request):
	context = RequestContext(request)
	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['song_id']
	if cat_id:
		song = Picture.objects.get(id=int(cat_id))
		if song:
			playlist.append(song)
	return render_to_response('playmusic/playlist.html', {'playlist':playlist}, context)


def playit(request):
	context = RequestContext(request)
	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['song_id']
	if cat_id:
		song = Picture.objects.get(id=int(cat_id))
		if song:
			del playlist[:]
			playlist.append(song)
	return render_to_response('playmusic/playlist.html', {'playlist':playlist}, context)

def suggest_category(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        song=q.replace(' ','_')

        drugs = Picture.objects.filter(file__icontains = song )[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = drug.file.name.replace('_',' ')[6:]
            drug_json['value'] = drug.file.name.replace('_',' ')[6:]
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
def searchbyartist(request):
	context = RequestContext(request)
	results=[]
	if request.method == 'GET':
		name=request.GET['name']
	r = Picture.objects.all()
	for item in r:
		mp3 = read_tags(settings.MEDIA_ROOT + item.file.name)
		if name in str(mp3['artist'][0]).lower():
			results.append(item)
	no_of_results = len(results)
	dict2={'results': results,'playlist':playlist,'no_of_results' : no_of_results}
	return render_to_response('playmusic/searchresults.html',dict2,context)

def searchbyalbum(request):
	context = RequestContext(request)
	results=[]
	if request.method == 'GET':
		name=request.GET['name']
	r = Picture.objects.all()
	for item in r:
		mp3 = read_tags(settings.MEDIA_ROOT + item.file.name)
		if name in str(mp3['album'][0]).lower():
			results.append(item)
	no_of_results = len(results)
	dict2={'results': results,'playlist':playlist,'no_of_results' : no_of_results}
	return render_to_response('playmusic/searchresults.html',dict2,context)
def searchbygenre(request):
	context = RequestContext(request)
	results=[]
	if request.method == 'GET':
		name=request.GET['name']
	r = Picture.objects.all()
	for item in r:
		mp3 = read_tags(settings.MEDIA_ROOT + item.file.name)
		print str(mp3['genre'][0])
		if name in str(mp3['genre'][0]).lower():
			results.append(item)
	no_of_results = len(results)
	dict2={'results': results,'playlist':playlist,'no_of_results' : no_of_results}
	return render_to_response('playmusic/searchresults.html',dict2,context)

def usersearch(request):
	context = RequestContext(request)
	results=[]
	if request.method == 'GET':
		name=request.GET['username']

	results = User.objects.filter( Q(username__icontains = name) | Q(email__icontains= name) | Q(first_name__icontains= name) | Q(last_name__icontains= name))
	no_of_results = len(results)
	dict2={'results': results, 'no_of_results' : no_of_results }
	return render_to_response('playmusic/usersearchresults.html',dict2,context)
def playmyplaylist(request):
	p = Playlist.objects.filter(user = request.user)
	del playlist[:]
	for item in p:
		playlist.append(item.song)
	return render_to_response('playmusic/playlist.html', {'playlist':playlist})
def playmyfav(request):
	p = Fav.objects.filter(user = request.user)
	del playlist[:]
	for item in p:
		playlist.append(item.song)
	return render_to_response('playmusic/playlist.html', {'playlist':playlist})
def userplaylistsearch(request):
	context = RequestContext(request)
	results=[]
	if request.method == 'GET':
		name=request.GET['username']

	results = User.objects.filter( Q(username__icontains = name) | Q(email__icontains= name) | Q(first_name__icontains= name) | Q(last_name__icontains= name))
	no_of_results = len(results)
	dict2={'results': results, 'no_of_results' : no_of_results }
	return render_to_response('playmusic/userlistforplaylist.html',dict2,context)

def playotherplaylist(request):
    context = RequestContext(request)
    user_id = None

    if request.method == 'GET':
        user_id = request.GET['user_id']

    if user_id:
        user = User.objects.get(pk=int(user_id))
	p = Playlist.objects.filter(user = user)
	del playlist[:]

	for item in p:
		playlist.append(item.song)
	return HttpResponse("Success")
