""" Users' URLS """

# Django
from django.urls import path
# Local
from welcome import views
urlpatterns = [
    # TODO: Create the view and template for "/"
    path(
        route='/',
        view=views.,
        name='login'
    ),
]
