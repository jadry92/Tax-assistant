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

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='signup/',
        view=views.SignUpView.as_view(),
        name='signup'
    ),

    path(
        route='profile/',
        view=views.UpdateProfile.as_view(),
        name='update'
    ),

]
