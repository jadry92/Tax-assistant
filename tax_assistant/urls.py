""" Tax Assistant's URLs """
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include(('welcome.urls', 'welcome'), namespace='welcome')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('expenses/', include(('users.urls', 'expenses'), namespace='expenses')),
    path('goals/', include(('users.urls', 'goals'), namespace='goals')),

]
