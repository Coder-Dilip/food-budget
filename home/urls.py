from django.urls import path
from home import views

urlpatterns = [
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredient/update/<str:ingredient_id>/', views.update_ingredient, name='update_ingredient'),
    path('add-ingredient/', views.add_ingredient, name='add_ingredient'),

]
