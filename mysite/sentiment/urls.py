from django.conf.urls import url
from sentiment import views




urlpatterns = [
        url(r'^$', views.HomePageView.as_view()),
        url(r'^about/$', views.AboutPageView.as_view()), 
        url(r'^search$',views.search),
         
        ]
