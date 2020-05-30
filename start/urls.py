from django.urls import path
import start.views

urlpatterns = [
    path('', start.views.initial, name="initial"),
    path('signup/', start.views.signup, name="signup"),
    path('login/', start.views.login, name="login"),
    path('home/', start.views.home, name="home"),
    path('read_login/', start.views.read_login, name="read_login"),
]
