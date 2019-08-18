from django.urls import path
from .views import WordFilterView, WordDetailView, WordCreateView, WordUpdateView, WordDeleteView
urlpatterns = [
    path('', WordFilterView.as_view(), name='index'),
    path('', WordFDetailView.as_view(), name='detail'),
    path('', WordCreateView.as_view(), name='create'),
    path('', WordUpdateView.as_view(), name='update'),
    path('', WordDeleteView.as_view(), name='delete'),
]
