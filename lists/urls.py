from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^fav/$',views.addtofav,name='fav'),
        url(r'^playlist/$',views.addtoplaylist,name='playlist'),
    ]
