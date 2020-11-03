"""TutorialSerializers module"""

from rest_framework import serializers
from tutorials.models import Tutorials


class TutorialSerializers(serializers.ModelSerializer):
    """TutorialSerializer class"""

    class Meta:
        """Inner class container with options"""
        model = Tutorials
        fields = ("id", "title", "description", "published")
