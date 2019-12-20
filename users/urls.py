""" Users' URLS """

# Django
from django.urls import path

# Local
from users import views

urlpatterns = [

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
]
