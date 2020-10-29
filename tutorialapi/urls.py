from django.conf.urls import url
from . import views
from .views import ListTutorialView

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^tutorials/(?P<pk>\d+)/',ListTutorialView.as_view(),name='all-tutorials'),
  url(r'^tutorials/',ListTutorialView.as_view())

 
]