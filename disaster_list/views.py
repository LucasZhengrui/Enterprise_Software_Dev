from django.shortcuts import redirect, render
from .models import DisasterList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_disasters():
    disasters = DisasterList.objects.filter(is_delete=0).order_by('dis_id')
    return disasters

def index(request):
    disasters_list = get_disasters()

    # Search
    search_query = request.GET.get('search_query')
    search_field = request.GET.get('search_field', 'all')
    if search_query and search_field != 'all':
        disasters_list = disasters_list.filter(**{search_field: search_query})

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

    return render(request, 'disaster_list/index.html', {'disasters': disasters,'search_query':search_query,'search_field':search_field})

def delete(request, dis_id):
    disaster = DisasterList.objects.get(dis_id=dis_id)
    disaster.is_delete = 1
    disaster.save()
    return index(request)





