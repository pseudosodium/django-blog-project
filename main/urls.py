from django.urls import path
from . import views
#from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
  path("", views.default, name="default"),
  path("home", views.homepage, name="homepage"),
  path("register", views.register, name="register"),
  path("logout", views.logout_request, name="logout"),
  path("login", views.login_request, name="login"),
  path("account", views.view_profile, name="view_profile"),
  path("edit", views.edit_profile, name="edit_profile"),
  path("change-password", views.change_password, name="change_password"),
  #path("reset-password", PasswordResetView.as_view(), name="reset_password"),
  #path("reset-password/done", PasswordResetDoneView.as_view(), name="reset_password_done"),
  #path("reset-password/confirm", PasswordResetConfirmView.as_view(), name="reset_password_confirm"),
  path("<single_slug>", views.single_slug, name="single_slug"),
]
