from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/home', views.notice_home, name="notice_home"), #home.html
    path('blog/<int:blog_id>', views.detail, name = "detail"), #detail.html
    path('blog/new/', views.new, name = "new"),
    path('blog/create', views.create, name = "create"),
    path('blog/edit<int:blog_id>', views.edit, name = "edit"),
    path('blog/update/<int:blog_id>', views.update, name = "update"),
    path('blog/delete/<int:blog_id>', views.delete, name = "delete"),
]