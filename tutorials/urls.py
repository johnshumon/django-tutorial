"""URLs module"""

from django.urls import path

from tutorials.views import TutorialsDetails, TutorialsList, TutorialsListPublished

urlpatterns = [
    path("tutorials", TutorialsList.as_view(), name="tutorials_list"),
    path("tutorials/published", TutorialsListPublished.as_view(), name="tutorials_list_published"),
    path("tutorials/<int:pk>", TutorialsDetails.as_view(), name="tutorials_details")
]
