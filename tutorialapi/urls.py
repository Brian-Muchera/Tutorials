from django.conf.urls import url,include
from . import views
from .views import ListTutorialView,TutorialViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tutorial',TutorialViewset,basename='tutorial')

urlpatterns=[
  url(r'^viewset/',include(router.urls)),
  url(r'^$',views.home,name='home'),
  url(r'^tutorials/(?P<pk>\d+)/',ListTutorialView.as_view(),name='all-tutorials'),
  url(r'^tutorials/',ListTutorialView.as_view())

 
]