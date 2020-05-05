from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from recipes.models import Recipe, Author
from recipes.forms import RecipeAddForm, AuthorAddForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def recipe_add(request):
    html = "recipeaddform.html"
    form = RecipeAddForm()

    return render(request, html, {"form": form})


def author_add(request):
    pass


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes_list'


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['personal_recipe_list'] = Recipe.objects.all()
        return context
