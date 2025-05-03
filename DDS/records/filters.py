import django_filters
from records.models import Record
from guides.models import Category, Subcategory, Type, Status


class RecordFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='created_dt', lookup_expr='gte', label='Дата от', input_formats=['%d.%m.%Y'])
    date_to = django_filters.DateFilter(field_name='created_dt', lookup_expr='lte', label='Дата до', input_formats=['%d.%m.%Y'])
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all(), label='Статус')
    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all(), label='Тип')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')
    subcategory = django_filters.ModelChoiceFilter(queryset=Subcategory.objects.none(), label='Подкатегория')

    class Meta:
        model = Record
        fields = ['date_from', 'date_to', 'status', 'type', 'category', 'subcategory']