from django.shortcuts import render
from .models import DisasterList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

def get_delete_disasters():
    disasters = DisasterList.objects.filter(is_delete=1).order_by('Dis_ID')
    return disasters

def index(request):
    disasters_list = get_delete_disasters()
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

    # Limit the page range to 3 pages
    page_range = paginator.get_elided_page_range(page, on_each_side=0, on_ends=1)

    return render(request, 'disaster_trash_list/index.html', {'disasters': disasters, 'page_range': page_range})


def recovery(request, dis_id):
    disaster = DisasterList.objects.get(Dis_ID=dis_id)
    disaster.is_delete = 0
    disaster.save()
    return HttpResponseRedirect('/trash')