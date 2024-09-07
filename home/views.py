from django.shortcuts import render, redirect
from .models import Ingredient
from mongoengine import Q


def ingredient_list(request):
    # Sort ingredients by category
    ingredients = Ingredient.objects.all().order_by('category')
    return render(request, 'ingredient_list.html', {'ingredients': ingredients})


def update_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    print(ingredient)
    if request.method == 'POST':
        # Update the ingredient directly with validation (add validation as needed)
        new_category = request.POST.get('category')
        new_name = request.POST.get('name')
        new_quantity = request.POST.get('quantity')  # Assuming a number field
        new_unit = request.POST.get('unit')
        new_price = request.POST.get('price')  # Assuming a number field

        # Basic validation example (you can add more as needed)
        if not new_category:
            # Handle missing category error
            return render(request, 'update_ingredient.html', {'ingredient': ingredient, 'error': 'Category is required'})

        ingredient.category = new_category
        ingredient.name = new_name
        ingredient.quantity = float(new_quantity) if new_quantity else 0.0  # Handle empty quantity
        ingredient.unit = new_unit
        ingredient.price = float(new_price) if new_price else 0.0  # Handle empty price

        ingredient.save()
        return redirect('ingredient_list')

    return render(request, 'update_ingredient.html', {'ingredient': ingredient})

def add_ingredient(request):
    if request.method == 'POST':
        new_category=request.POST.get('category')
        new_name = request.POST.get('name')
        new_quantity = float(request.POST.get('quantity'))
        new_unit = request.POST.get('unit')
        new_price = float(request.POST.get('price'))

        # Create a new Ingredient object
        ingredient = Ingredient.objects.create(
            category=new_category,
            name=new_name,
            quantity=new_quantity,
            unit=new_unit,
            price=new_price
        )
        ingredient.save()
        return redirect('ingredient_list')

    return render(request, 'add_ingredient.html')


