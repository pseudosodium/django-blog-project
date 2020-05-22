from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
  path("", views.homepage, name="homepage"),
  path("register", views.register, name="register"),
  path("logout", views.logout_request, name="logout"),
  path("login", views.login_request, name="login"),
  path("<single_slug>", views.single_slug, name="single_slug")
]
