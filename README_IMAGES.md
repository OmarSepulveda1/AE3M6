Where to place `recetas1.jpg` so it shows on the recipes page

- Put your image file at: `recetas_project/recipes/static/recipes/images/recetas1.jpg`
  - This file will be used as the default image in the recipes list when a recipe has no uploaded image.
  - Recommended size: 1200x800 or similar landscape ratio. Web-optimized JPEG (quality ~80) is fine.

- Alternatively, to show a specific image for a recipe, upload the image via Django admin (or assign the file into `media/recetas_images/` and set the `Receta.imagen` field for that record).
