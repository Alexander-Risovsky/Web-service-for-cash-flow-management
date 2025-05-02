from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from records.models import Record
from records.filters import RecordFilter
from guides.models import Subcategory

def index(request):
    Records = Record.objects.all()
    
    filter=RecordFilter(request.GET,queryset=Records)
    
    Records=filter.qs
    context={
        'Records':Records,
        'filter':filter
    }
    return render(request, 'main/main.html',context)   
