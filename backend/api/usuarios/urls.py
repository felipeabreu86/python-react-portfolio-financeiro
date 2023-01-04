from django.urls import path
from api.usuarios import views


urlpatterns = [
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("create/", views.CreateUserView.as_view()),
    path("profile/", views.ProfileView.as_view()),
]
