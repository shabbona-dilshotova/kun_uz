from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/detail/', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),


]