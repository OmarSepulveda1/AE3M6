from django.urls import path
from .views import RecipeListView, RecipeDetailView, contact_view, contact_success

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='index'),
    path('recetas/', RecipeListView.as_view(), name='recipe_list'),
    path('receta/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('contacto/', contact_view, name='contact'),
    path('contacto/enviado/', contact_success, name='contact_success'),
]
