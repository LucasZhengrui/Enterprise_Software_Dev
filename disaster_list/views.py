import csv
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import summary as DisasterList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_disasters():
    disasters = DisasterList.objects.filter(is_delete=0).order_by('Dis_ID')
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

    # Limit the page range to 3 pages
    page_range = paginator.get_elided_page_range(page, on_each_side=0, on_ends=1)

    return render(request, 'disaster_list/index.html', {'disasters': disasters, 'search_query': search_query,
                                                         'search_field': search_field, 'page_range': page_range})

def delete(request, dis_id):
    disaster = DisasterList.objects.get(dis_id=dis_id)
    disaster.is_delete = 1
    disaster.save()
    return index(request)

def download(request,  page_id, search_field, search_query):
    # Query the data of the form to be downloaded
    disasters_list = get_disasters()

    # Search
    if search_query and search_field != 'all':
        disasters_list = disasters_list.filter(**{search_field: search_query})

    # Pagination
    paginator = Paginator(disasters_list, 10)  # Show 10 items per page
    page = page_id
    
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

    # Create the HttpResponse object
    response = HttpResponse(content_type='text/csv')
    table_name = "Alldata_table_"+str(page_id)+".csv"
    response['Content-Disposition'] = 'attachment; filename='+table_name

    # Write to table data
    writer = csv.writer(response)
    for row in disasters:
        writer.writerow([
            row.Dis_ID, row.Year, row.Disaster_Group, row.Disaster_Type,
            row.Country, row.ISO, row.Total_Affected, row.Total_Damages
        ])

    return response




