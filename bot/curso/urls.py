from django.urls import path
from . import views
from . import apis


urlpatterns = [
    path(r'', views.home, name='portal'),
    path(r'api/chatterbot/', views.ChatterBotApiView.as_view(), name='chatterbot'),

]
