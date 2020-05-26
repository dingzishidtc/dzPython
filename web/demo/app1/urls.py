from django.urls import path,re_path
from app1 import views as app1_views

urlpatterns = [
    # path('articles/2020', app1_views.articles),
    # path('articles/<int:year>', app1_views.articles),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', app1_views.articles),
    path('get_name', app1_views.get_name),
]
