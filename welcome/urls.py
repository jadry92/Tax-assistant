""" Users' URLS """

# Django
from django.urls import path
# Local
from welcome import views


urlpatterns = [
    path(
        route='',
        view=views.LandingPage.as_view(),
        name='landing'
    ),
    path(
        route='base/',
        view=views.LandingPage.as_view(),
        name='home'
    ),
]
