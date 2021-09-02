from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)

# Create your views here.

from django.urls import reverse_lazy
from .models import Games


class GameListView(ListView):
    template_name = "game/game-list.html"
    model = Games


class GameDetailView(DetailView):
    template_name = "game/game-detail.html"
    model = Games


class GameCreateView(CreateView):
    template_name = "game/game-create.html"
    model = Games
    fields = []


class GameUpdateView(UpdateView):
    template_name = "game/game-update.html"
    model = Games
    fields = []


class GameDeleteView(DeleteView):
    template_name = "game/game-delete.html"
    model = Games
    success_url = reverse_lazy("game-list")