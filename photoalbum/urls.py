from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from . import models

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='photoalbum'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('upload', views.upload_file, name='upload'),
]
urlpatterns += staticfiles_urlpatterns()

