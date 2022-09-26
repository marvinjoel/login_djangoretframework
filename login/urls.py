from django.urls import path
from login.views import UserCreateView

urlpatterns = [
    path('signup/', UserCreateView.as_view()),
]