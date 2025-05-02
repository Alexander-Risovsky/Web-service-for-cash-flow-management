from django import forms
from .models import Category, Subcategory, Type, Status

class CategoryForm(forms.ModelForm):
    subcategories = forms.ModelMultipleChoiceField(
        queryset=Subcategory.objects.all(),  # Все подкатегории
        widget=forms.CheckboxSelectMultiple,  # Выводим подкатегории как чекбоксы
    )
    class Meta:
        model=Category
        fields = ['name','type','subcategories']

class TypeForm(forms.ModelForm):

    class Meta:
        model=Type
        fields = ['name']

class StatusForm(forms.ModelForm):

    class Meta:
        model=Status
        fields = ['name']

class SubcategoryForm(forms.ModelForm):

    class Meta:
        model=Subcategory
        fields = ['name','category']
        