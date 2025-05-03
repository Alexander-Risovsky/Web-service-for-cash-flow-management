from django.shortcuts import get_object_or_404, redirect, render
from .models import Type, Status, Category, Subcategory
from .forms import CategoryForm, TypeForm, StatusForm, SubcategoryForm

# -------------------- Types Views --------------------


def types_list(request):
    types = Type.objects.all()
    context = {
        'list': types,
        'model_name': 'Type',
    }
    return render(request, 'guides/guides_list.html', context)


def edit_type(request, type_id):
    type_obj = get_object_or_404(Type, id=type_id)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()
            return redirect('guides:types_list')
    else:
        form = TypeForm(instance=type_obj)
    context = {
        'form': form,
        'model_name': 'Тип',
    }
    return render(request, 'guides/edit_guide.html', context)


def create_type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guides:types_list')
    else:
        form = TypeForm()
    context = {
        'form': form,
        'model_name': 'Тип',
    }
    return render(request, 'guides/edit_guide.html', context)


def delete_type(request, type_id):
    type_obj = get_object_or_404(Type, id=type_id)
    if request.method == 'POST':
        type_obj.delete()
        return redirect('guides:types_list')
    return render(request, 'guides/types/delete_type.html', {'type': type_obj})

# -------------------- Status Views --------------------


def statuses_list(request):
    statuses = Status.objects.all()
    context = {
        'list': statuses,
        'model_name': 'Status',
    }
    return render(request, 'guides/guides_list.html', context)


def edit_status(request, status_id):
    status_obj = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status_obj)
        if form.is_valid():
            form.save()
            return redirect('guides:statuses_list')
    else:
        form = StatusForm(instance=status_obj)
    context = {
        'form': form,
        'model_name': 'Статус',
    }
    return render(request, 'guides/edit_guide.html', context)


def create_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guides:statuses_list')
    else:
        form = StatusForm()
    context = {
        'form': form,
        'model_name': 'Статус',
    }
    return render(request, 'guides/edit_guide.html', context)


def delete_status(request, status_id):
    status_obj = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        status_obj.delete()
        return redirect('guides:statuses_list')
    return render(request, 'guides/statuses/delete_status.html', {'status': status_obj})

# -------------------- Category Views --------------------


def categories_list(request):
    categories = Category.objects.prefetch_related('subcategory_set').all()
    context = {
        'list': categories,
        'model_name': 'Category',
    }
    return render(request, 'guides/guides_list.html', context)


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category.subcategory_set.set(form.cleaned_data['subcategories'])
            category.save()
            return redirect('guides:categories_list')
    else:
        form = CategoryForm(instance=category)
        form.fields['subcategories'].initial = category.subcategory_set.all()
    context = {
        'form': form,
        'model_name': 'Категория',
    }
    return render(request, 'guides/edit_guide.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            category.subcategory_set.set(form.cleaned_data['subcategories'])
            form.save_m2m()
            return redirect('guides:categories_list')
    else:
        form = CategoryForm()
    context = {
        'form': form,
        'model_name': 'Категория',
    }
    return render(request, 'guides/edit_guide.html', context)


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('guides:categories_list')
    return render(request, 'guides/category/delete_category.html', {'category': category})

# -------------------- Subcategory Views --------------------


def subcategories_list(request):
    subcategories = Subcategory.objects.all()
    context = {
        'list': subcategories,
        'model_name': 'Subcategory',
    }
    return render(request, 'guides/guides_list.html', context)


def edit_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('guides:subcategories_list')
    else:
        form = SubcategoryForm(instance=subcategory)
    context = {
        'form': form,
        'model_name': 'Подкатегория',
    }
    return render(request, 'guides/edit_guide.html', context)


def create_subcategory(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guides:subcategories_list')
    else:
        form = SubcategoryForm()
    context = {
        'form': form,
        'model_name': 'Подкатегория',
    }
    return render(request, 'guides/edit_guide.html', context)


def delete_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('guides:subcategories_list')
    return render(request, 'guides/subcategory/delete_subcategory.html', {'subcategory': subcategory})