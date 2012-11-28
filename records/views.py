from django.shortcuts import render
from records.models import Record

def old_sample(request):
        return render(request, 'records/old_sample.html',)

def sample(request):
        return render(request, 'records/sample.html',)

