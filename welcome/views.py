""" Welcome's Views"""

# Django
from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = "welcome/landing_page.html"
