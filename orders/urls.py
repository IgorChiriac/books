from django.urls import path
from .views import charge, OrdersPageView

urlpatterns = [
  path('charge/', charge, name='charge'),
  path('', OrdersPageView.as_view(), name='orders'),
]
