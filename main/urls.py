from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
  path("", views.homepage, name="homepage"),
  path("register", views.register, name="register"),
  path("logout", views.logout_request, name="logout"),
  path("login", views.login_request, name="login"),
  path("account", views.view_profile, name="view_profile"),
  path("edit", views.edit_profile, name="edit_profile"),
  path("change-password", views.change_password, name="change_password"),
  path("<single_slug>", views.single_slug, name="single_slug"),
]
