from django.conf.urls import url
from django.urls import path
from weatherAppDemo import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    path('weather', views.weather),

]
