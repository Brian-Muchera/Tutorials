from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  
from .models import Tutorials
from .serializers import TutorialSerializer

def home(request):
  title ="Welcome"
  return render(request,'tutorialapi/home.html',{"title":title})

class ListTutorialView(generics.GenericAPIView, 
                       mixins.ListModelMixin, 
                       mixins.CreateModelMixin, 
                       mixins.UpdateModelMixin, 
                       mixins.RetrieveModelMixin, 
                       mixins.DestroyModelMixin):
  """
  Provides a get post put delete method handler.
  """
  queryset = Tutorials.objects.all() 
  serializer_class = TutorialSerializer
  lookup_field ='pk'
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get(self,request,pk=None):
    if pk:
      return self.retrieve(request)
    else:
      return self.list(request)
  
  def post(self,request):
    return self.create(request)
  
  def put(self,request,pk=None):
    return self.update(request,pk)
  
  def delete(self,request,pk):
    return self.destroy(request,pk)