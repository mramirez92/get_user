from django.urls import path
from .views import (
    AnimalDeleteView,
    AnimalDetailView,
    AnimalListView,
    AnimalCreateView,
    AnimalUpdateView,
)

urlpatterns =[
    path('', AnimalListView.as_view(), name ='animal_list'),
    path('create/', AnimalCreateView.as_view(), name='animal_create'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
    path('<int:pk>/update/', AnimalUpdateView.as_view(), name='animal_update'),
    path('<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal_delete'),
]