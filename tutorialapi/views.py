from django.shortcuts import render

def home(request):
  title ="Welcome"
  return render(request,'tutorialapi/home.html',{"title":title})