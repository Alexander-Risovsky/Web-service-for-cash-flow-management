from django.shortcuts import render
# Create your views here.
from records.models import Record
from records.filters import RecordFilter


def index(request):
    Records = Record.objects.all()

    filter = RecordFilter(request.GET, queryset=Records)

    Records = filter.qs
    context = {
        'Records': Records,
        'filter': filter
    }
    return render(request, 'main/main.html', context)
