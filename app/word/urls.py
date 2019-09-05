from django.urls import path
from .views import WordFilterView, WordDetailView, WordCreateView, WordUpdateView, WordDeleteView
urlpatterns = [
    path('', WordFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', WordDetailView.as_view(), name='detail'),
    path('create/', WordCreateView.as_view(), name='create'),
    path('update/<int:pk>/', WordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', WordDeleteView.as_view(), name='delete'),
]
