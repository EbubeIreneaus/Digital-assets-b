from . import  views
from django.urls import path

urlpatterns = [
    path('details/<slug:profileId>', views.accountDetails),
    path('user_data/', views.change_user_data),
    path('profile_data/', views.change_profile_data),
    path('security/', views.change_security_data),
    # path('verify/', views.verify_account),
]