from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customisation
admin.site.site_header = "Developer Aaryan's Login"
admin.site.site_title = "Welcome to Aaryan's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.index, name='index'),
    path('achievements', views.achievements, name='achievements'),
    path('contact', views.contact, name='contact'),
    path('message', views.message, name='message')
]