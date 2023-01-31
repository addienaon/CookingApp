from django import forms
from .models import MyFood, Ingredient

class MyFoodForm(forms.ModelForm):
    user_input = forms.CharField()

    def save(self, commit=True):
        instance = super(MyFoodForm, self).save(commit=False)
        ingredient = Ingredient.objects.get(name=self.cleaned_data['user_input'])
        instance = ingredient
        if commit:
            item = MyFood(user_input=instance.name, fk_ingredient=instance)
            item.save()

    class Meta:
        model = MyFood
        fields = ['user_input']
        labels = {
            'user_input':'Add Food Item'
        }

    def __init__(self, *args, **kwargs):
        super(MyFoodForm, self).__init__(*args, **kwargs)
        self.fields['user_input'].empty_label = "Select"
