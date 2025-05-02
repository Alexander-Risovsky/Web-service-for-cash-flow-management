from django import forms
from .models import Record
from guides.models import  Subcategory

class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields = ['status', 'type', 'category', 'subcategory', 'summa', 'Comment']
        help_texts = {
            'summa': 'Обязательное поле.',
            'type': 'Обязательное поле.',
            'category': 'Обязательное поле.',
            'subcategory': 'Обязательное поле.',
        }
    #Прописываем метод init, чтобы при редактировании записи в поле subcategory отображались только подкатегории, относящиеся к выбранной категории
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.category:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)
        