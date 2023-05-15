from django.urls import path
from .views import FactorView

urlpatterns = [
	path('',FactorView.as_view())
]