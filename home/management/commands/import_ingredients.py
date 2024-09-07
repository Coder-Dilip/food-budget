from django.core.management.base import BaseCommand # type: ignore
from home.models import Ingredient

INGREDIENT_DATA = {
    "Grains_and_Staples": ["Rice", "Wheat", "Lentils", "Corn", "Barley", "Millet", "Buckwheat", "Flattened Rice", "Beaten Rice"],
    "Vegetables": ["Potato", "Spinach", "Cauliflower", "Tomato", "Onion", "Garlic", "Green Peas", "Carrot", "Cabbage", "Radish", "Pumpkin", "Bitter Gourd"],
    "Proteins": ["Chicken", "Eggs", "Buffalo Meat", "Fish", "Goat", "Pork", "Duck", "Paneer"],
    "Fruits": ["Banana", "Mango", "Apple", "Papaya", "Pineapple", "Litchi", "Pomegranate", "Guava", "Coconut", "Jackfruit", "Orange"],
    "Dairy": ["Milk", "Yogurt", "Ghee", "Cheese", "Butter"]
}

class Command(BaseCommand):
    help = 'Imports ingredients into MongoDB'

    def handle(self, *args, **kwargs):
        for category, ingredients in INGREDIENT_DATA.items():
            for ingredient in ingredients:
                Ingredient(
                    category=category,
                    name=ingredient,
                    quantity=0,  # Leave blank for now
                    unit="",  # Leave blank for now
                    price=0.0  # Leave blank for now
                ).save()
        self.stdout.write(self.style.SUCCESS('Successfully imported ingredients'))
