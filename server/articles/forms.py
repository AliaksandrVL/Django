from django import forms

from . import models

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = models.Article
        fields = ['name', 'category', 'image', 'content']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'image': forms.widgets.ClearableFileInput(attrs={'class': 'form-control'}),
            'content': forms.widgets.Textarea(attrs={'class': 'form-control'}),
            'category':forms.widgets.Select(attrs={'class': 'form-control'})
        }
