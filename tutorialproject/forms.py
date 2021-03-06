from django import forms
from .models import Tutorial

# from . import forms
#......
class NewTutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields=['title','description','image','content','Author', 'Published','Unpublished','url']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }