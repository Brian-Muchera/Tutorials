from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Tutorials(models.Model):
  tutorial_title = models.CharField(max_length=150)
  description = models.TextField()
  tutorial_image = models.CloudinaryField('image')
  tutorial_content = models.TextField()
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  published = models.BooleanField()
  created_on = models.DateField()
  postded_on = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return "{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.tutorial_title,self.description,self.tutorial_image,self.tutorial_content,self.author,self.published,self.postded_on,self.created_on,self.pk)