"""Users' views"""

# Django
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
# Models
from django.contrib.auth.models import User
from users.models import Profile
# Forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'


class UpdateProfile(LoginRequiredMixin, UpdateView):
    """Update profile View"""
    # TODO: create the update_profile.html
    #
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    # TODO : edit the logout.html
    # to take out the image
    """Login View."""
    template_name = 'users/login.html'


class SignUpView(FormView):
    """Class Sign up view"""
    # TODO : edit the signup.html
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save the form. """
        form.save()
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    # TODO : create the logout.html if is necessary
    template_name = 'users/logout.html'
