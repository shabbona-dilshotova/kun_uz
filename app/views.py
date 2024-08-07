from django.shortcuts import render

from app.models import NewsModel
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class NewsListView(ListView):
    model = NewsModel
    template_name = 'news_list.html'

class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'news_detail.html'

class NewsCreateView(CreateView):
    model = NewsModel
    template_name = 'news_create.html'
    fields = '__all__'
    success_url = reverse_lazy("news_list")

class NewsUpdateView(UpdateView):
    model = NewsModel
    template_name = 'news_create.html'
    fields = '__all__'
    success_url = reverse_lazy("news_list")

class NewsDeleteView(DeleteView):
    model = NewsModel
    template_name = 'news_delete.html'
    success_url = reverse_lazy("news_list")
