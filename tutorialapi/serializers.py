from rest_framework import serializers
from .models import Tutorials

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorials
        fields = ("tutorial_title", "description","tutorial_image","tutorial_content","author","published","postded_on","created_on","pk")
        
