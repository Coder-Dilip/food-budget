from mongoengine import Document, StringField, FloatField, IntField

class Ingredient(Document):
    category = StringField(required=True)
    name = StringField(required=True)
    quantity = FloatField(default=0)  # You can leave it blank for now
    unit = StringField(default="")
    price = FloatField(default=0.0)
    
    meta = {'collection': 'ingredients'}
