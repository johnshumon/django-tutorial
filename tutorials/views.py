"""Endpoints API view module"""

from rest_framework import generics

from tutorials.models import Tutorials
from tutorials.serializers import TutorialSerializers


class TutorialsList(generics.ListCreateAPIView):
    """TutorialsList class"""

    queryset = Tutorials.objects.all()
    serializer_class = TutorialSerializers


class TutorialsDetails(generics.RetrieveUpdateDestroyAPIView):
    """TutorialsDetails class"""

    queryset = Tutorials.objects.all()
    serializer_class = TutorialSerializers


class TutorialsListPublished(generics.ListAPIView):
    """TutorialsListPublished class"""

    queryset = Tutorials.objects.filter(published=True)
    serializer_class = TutorialSerializers
