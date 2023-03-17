from django.shortcuts import render
from .models import DisasterList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_disasters():
    disasters = DisasterList.objects.order_by('dis_id')
    return disasters

from django.shortcuts import render
from .models import DisasterList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_disasters():
    disasters = DisasterList.objects.order_by('dis_id')
    return disasters

def index(request):
    disasters_list = get_disasters()

    # Pagination
    paginator = Paginator(disasters_list, 10)  # Show 10 items per page
    page = request.GET.get('page', 1)

    try:
        # Convert page to an integer
        page = int(page)
        # Validate that the page is greater than or equal to 1
        if page <= 0:
            page = 1
        # Get the page from the paginator
        disasters = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        # If page is not an integer or out of range, deliver first page.
        disasters = paginator.page(1)

    return render(request, 'disaster_list/index.html', {'disasters': disasters})







