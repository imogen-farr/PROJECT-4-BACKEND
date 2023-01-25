from django.urls import path
from .views import EnvironmentListView

urlpatterns = [
    path('', EnvironmentListView.as_view())
]
