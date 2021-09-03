from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)

# Create your views here.

from django.urls import reverse_lazy
from .models import Games


class GamesListView(ListView):
    template_name = "games/games-list.html"
    model = Games


class GamesDetailView(DetailView):
    template_name = "games/games-detail.html"
    model = Games


class GamesCreateView(CreateView):
    template_name = "games/games-create.html"
    model = Games
    fields = ['name', 'description', 'owner']


class GamesUpdateView(UpdateView):
    template_name = "games/games-update.html"
    model = Games
    fields = ['name', 'description', 'owner']


class GamesDeleteView(DeleteView):
    template_name = "games/games-delete.html"
    model = Games
    success_url = reverse_lazy("games_list")