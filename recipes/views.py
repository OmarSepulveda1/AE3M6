from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Receta
from .forms import ContactForm

class RecipeListView(ListView):
    model = Receta
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recetas'
    paginate_by = 6  # opcional

class RecipeDetailView(DetailView):
    model = Receta
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'receta'

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recetas': recetas})    

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí podrías enviar un email, guardar en DB o enviar a un servicio
            # Simulamos éxito y redirigimos
            messages.success(request, "Mensaje enviado correctamente. ¡Gracias!")
            return redirect('recipes:contact_success')
        else:
            messages.warning(request, "Por favor corrige los errores en el formulario.")
    else:
        form = ContactForm()
    return render(request, 'recipes/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'recipes/contact_success.html')
