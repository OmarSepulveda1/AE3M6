from django.db import models
from django.urls import reverse

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas_images/', null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('recipes:recipe_detail', args=[str(self.id)])
