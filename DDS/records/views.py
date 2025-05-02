from django.shortcuts import render,redirect
from .models import Record
from.forms import RecordForm
from django.http import JsonResponse
from guides.models import Subcategory,Category
# Create your views here.
def records_list(request):
    Records = Record.objects.all()
    context={
        'Records':Records
    }
    return render(request,'records/list.html',context=context)

def create_record(request):
    RForm=RecordForm(request.POST or None)
    if request.POST:
        if RForm.is_valid():
            RForm.save()
            return redirect('records:records_list')
    else:
        RForm=RecordForm()
    return render(request,'records/add_record.html',context={'Form':RForm})

def delete_record(request,id_record):
    if request.POST:
        Record_to_del=Record.objects.filter(pk=id_record)
        Record_to_del.delete()
        return redirect('records:records_list')
    return render(request,'records/list.html')

def edit_record(request,id_record):
    record=Record.objects.get(pk=id_record)
    if request.POST:
        form=RecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('records:records_list')
    else:
        form=RecordForm(instance=record)
    context={
        'form':form,
        'model_name':'Запись',
    }
    return render(request,'guides/edit_guide.html',context)


def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

def get_categories_by_type(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)
