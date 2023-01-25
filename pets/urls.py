from django.urls import path  # import path from django
from .views import PetListView, PetDetailView  # import class from .views

urlpatterns = [
    path('', PetListView.as_view()),
    path('<int:pk>/', PetDetailView.as_view()),
]