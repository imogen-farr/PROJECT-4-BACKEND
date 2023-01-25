from django.urls import path
from .views import LifespanListView

urlpatterns = [
    path('', LifespanListView.as_view())
]
