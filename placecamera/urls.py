from django.contrib import admin
from django.urls import path, re_path
from placecamera import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home),
    re_path(r'\w+', views.placecameraview)
]
