from Login.views import Login
from django.urls import path

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    
]