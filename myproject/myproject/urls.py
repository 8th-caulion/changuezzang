from django.contrib import admin
from django.urls import path
import notice.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notice.views.home, name="home")
]
