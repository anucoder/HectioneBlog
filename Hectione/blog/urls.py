from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^about/',views.AboutView.as_view(),name='about'),
    url(r'^contact/',views.contactFormView,name='contact'),
    url(r'^blog/',views.PostListView.as_view(),name='post_list'),
    url(r'^thanks/',views.ThanksView.as_view(),name='thanks'),
    #url(r'^blog/')
]
