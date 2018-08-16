from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
      path('about/', views.about, name='about'),
      path('conatct/', views.contact, name='contact_list')





]
