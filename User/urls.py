from django.urls import path
from User.views import *

urlpatterns = [
    path('adduser/', addUser.as_view(), name='add_user'),

]