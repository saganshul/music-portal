from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^friend/$',views.addtomyfriendreclist,name='entry'),
        url(r'^remove/$',views.clearmylist,name='clear'),
]
