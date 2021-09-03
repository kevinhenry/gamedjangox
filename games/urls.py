from django.urls import path
from .views import GamesListView, GamesDetailView, GamesCreateView, GamesUpdateView, GamesDeleteView

urlpatterns = [
    path('', GamesListView.as_view(), name='games_list'),
    path('<int:pk>/', GamesDetailView.as_view(), name='games_detail'),
    path('create/', GamesCreateView.as_view(), name='games_create'),
    path('<int:pk>/update/', GamesUpdateView.as_view(), name='games_update'),
    path('<int:pk>/delete/', GamesDeleteView.as_view(), name='games_delete'),
]