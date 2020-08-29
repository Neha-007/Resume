from django.urls import path
from . import views
urlpatterns = [
	path('',views.about, name='index'),
	path('about/', views.about, name='about'),
	path('career/', views.career, name='career'),
	path('projects/', views.projects, name='projects'),
	path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]