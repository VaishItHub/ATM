from django.urls import path
from .views import home, verify, dashboard, withdraw, check_balance

urlpatterns = [
    path('', home, name='home'),
    path('verify/', verify, name='verify'),
    path('dashboard/', dashboard, name='dashboard'),
    path('withdraw/', withdraw, name='withdraw'),
    path('check_balance/', check_balance, name='check_balance'),
]
