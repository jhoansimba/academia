
from Login.views import Login, changePassword, resetPassword, updatePassword
from django.urls import path

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('login/reset', resetPassword.as_view(), name='reset'),
    path('login/changepassword', changePassword.as_view(), name='changepassword'),
    path('login/update/<token>', updatePassword.as_view(), name='update'),

]