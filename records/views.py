from django.shortcuts import render
from records.models import Record

def sample(request):
        return render(request, 'records/sample.html',)
