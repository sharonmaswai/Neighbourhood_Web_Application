from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns=[
    
    url('^$',views.index,name='index'),
    url(r'^newprofile/', views.create_profile, name='profile-form'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^postconcern/', views.post_concern, name='post-concern'),
    url(r'^concerns/', views.view_concern, name='concerns'),
    url(r'^search/', views.search_results, name='search_results')
    url(r'^onehood/(\d+)/', views.one_hood, name='one_hood'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
