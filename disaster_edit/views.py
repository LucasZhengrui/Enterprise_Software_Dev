from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import details
# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 

def list():
    list = ['Dis_id', 'Year', 'Disaster_Group', 'Disaster_Type', 'Country', 'ISO', 'Total_Affected', 'Total_Damages', 'is_delete']
    return list

def index(request):
    myList = list()
    return render(request, 'disaster_edit/index.html', {'list': myList})

class SummaryUpdate(UpdateView):
    model = details
    fields = list
    # template_name = 'disaster_edit/index.html'
    success_url = reverse_lazy('index')