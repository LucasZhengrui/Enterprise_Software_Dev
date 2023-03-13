from django.shortcuts import render

# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 

def list():
    list = []
    return list

def index(request):
    myList = list()
    return render(request, 'disaster_dashboard/index.html', {'list': myList})