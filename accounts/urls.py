from django.urls import path
from .views import *
urlpatterns = [
    path('', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('<uuid:token>/', ConfirmEmailView.as_view(), name='confirm_email'),

]