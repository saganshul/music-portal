from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login/$',views.login,name='login'),
        url(r'^auth',views.auth_view,name='auth'),
        url(r'^loggedin/$',views.loggedin,name='logggedin'),
        url(r'^logout/$',views.logout,name='logout'),
        url(r'^invalid/$',views.invalid,name='invalid'),
        url(r'^usernameinvalid/$',views.usernameinvalid),
        url(r'^passwordinvalid/$',views.passwordinvalid),
        url(r'^register/$',views.register_user,name='register'),
        url(r'^search/$',views.search,name='search'),
        url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
        url(r'^register_view/$',views.register_view),
        url(r'^playlistmaker/$', views.playlistmaker),
        url(r'^playit/$', views.playit),
        url(r'^suggest_category/$', views.suggest_category),
        url(r'^searchbyartist/$',views.searchbyartist),
        url(r'^searchbyalbum/$',views.searchbyalbum),
        url(r'^searchbygenre/$',views.searchbygenre),
        url(r'^users/$',views.usersearch),
        url(r'^usersplaylist/$',views.userplaylistsearch),
        url(r'^playmyplaylist/$',views.playmyplaylist),
        url(r'^playmyfav/$',views.playmyfav),
        url(r'^playotherplaylist/$',views.playotherplaylist),
    ]
