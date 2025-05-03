from django.urls import path
from .import views
app_name = 'records'
urlpatterns = [
    path('', views.records_list, name='records_list'),
    path('create/', views.create_record, name='create_record'),
    path('<int:id_record>/delete/', views.delete_record, name='delete_record'),
    path('<int:id_record>/edit/', views.edit_record, name='edit_record'),
    path('ajax/get-subcategories/', views.get_subcategories, name='get_subcategories'),
    path('ajax/get-categories/', views.get_categories_by_type, name='get_categories_by_type'),
]
