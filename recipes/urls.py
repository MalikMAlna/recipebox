from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe-lists'),
    path('recipes/<int:pk>',
         views.RecipeDetailView.as_view(),
         name='recipe-detail'),
    path('authors/<int:pk>',
         views.AuthorDetailView.as_view(),
         name='author-detail'),

]
