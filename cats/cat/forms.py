from django.forms import ModelForm
from cat.models import Cat

class Catforms(ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'

