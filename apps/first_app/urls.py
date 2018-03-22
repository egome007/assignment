from django.conf.urls import url
from . import views           # This line is new!
  
urlpatterns = [
    url(r'^$', views.time), 
    url(r'^blogs$', views.blogs),
    url(r'^news$', views.new), 
    url(r'^create$', views.create),
    url(r'^15$', views.number),       # This line has changed!
  ]
