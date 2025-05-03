from django.urls import path
from .import views

app_name = 'guides'
urlpatterns = [
    # url для категорий
    path('categories', views.Categories_list, name='categories_list'),
    path('categories/<int:category_id>/edit/', views.edit_category, name='edit_category'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),

    # url для подкатегорий
    path('subcategories', views.Subcategories_list, name='subcategories_list'),
    path('subcategories/<int:subcategory_id>/edit', views.edit_subcategory, name='edit_subcategory'),
    path('subcategories/create/', views.create_subcategory, name='create_subcategory'),
    path('subcategories/<int:subcategory_id>/delete/', views.delete_subcategory, name='delete_subcategory'),

    # url для типов
    path('types', views.Type_list, name='types_list'),
    path('types/<int:type_id>/edit', views.edit_type, name='edit_type'),
    path('types/create/', views.create_type, name='create_type'),
    path('types/<int:type_id>/delete/', views.delete_type, name='delete_type'),

    # url для статусов
    path('statuses', views.Status_list, name='statuses_list'),
    path('statuses/<int:status_id>/edit', views.edit_status, name='edit_status'),
    path('statuses/create/', views.create_status, name='create_status'),
    path('statuses/<int:status_id>/delete/', views.delete_status, name='delete_status'),

]
