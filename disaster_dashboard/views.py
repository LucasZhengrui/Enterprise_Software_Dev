from django.shortcuts import render
import plotly.graph_objs as go
from .models import DisasterList
from django.db import models

def create_top_10_affected_countries():
    # Get top 10 countries by total affected
    top_10_affected = (
        DisasterList.objects
        .values('country')
        .annotate(total_affected=models.Sum('total_affected'))
        .order_by('-total_affected')[:10]
    )

    # Create list of list for table data
    table_data = [[c['country'], c['total_affected']] for c in top_10_affected]

    # Create Plotly table object
    table = go.Figure(data=[go.Table(header=dict(values=['Country', 'Total Affected']),
                                     cells=dict(values=list(zip(*table_data))))
                            ])

    # Get HTML code for Plotly table
    table_html = table.to_html(full_html=False)

    return table_html


def create_top_10_damaged_countries():
    # Get top 10 countries by total damages in USD
    top_10_damaged = (
        DisasterList.objects
        .values('country')
        .annotate(total_damages_usd=models.Sum('total_damages_usd'))
        .order_by('-total_damages_usd')[:10]
    )

    # Create list of list for table data
    table_data = [[c['country'], c['total_damages_usd']] for c in top_10_damaged]

    # Create Plotly table object
    table = go.Figure(data=[go.Table(header=dict(values=['Country', 'Total Damages (USD)']),
                                     cells=dict(values=list(zip(*table_data))))
                            ])

    # Get HTML code for Plotly table
    table_html = table.to_html(full_html=False)

    return table_html


def create_disaster_pie_chart():
    # Count disasters by disaster group using Django ORM
    counts = (
        DisasterList.objects
        .values('disaster_group')
        .annotate(disaster_count=models.Count('dis_id'))
    )

    # Convert data to Plotly format
    labels = list(counts.values_list('disaster_group', flat=True))
    values = list(counts.values_list('disaster_count', flat=True))
    data = [go.Pie(labels=labels, values=values)]

    # Create Plotly figure object
    fig = go.Figure(data=data, layout=go.Layout(
        title=go.layout.Title(text='Disaster Group Pie Chart')
    ))

    # Get HTML code for Plotly figure
    pie_chart_html = fig.to_html(full_html=False)

    return pie_chart_html


def create_disaster_line_chart():
    # Count disasters by year using Django ORM
    counts = (
        DisasterList.objects
        .values('year')
        .annotate(disaster_count=models.Count('dis_id'))
    )

    # Convert data to Plotly format
    x = list(counts.values_list('year', flat=True))
    y = list(counts.values_list('disaster_count', flat=True))

    # Create Plotly figure object
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))
    fig.update_layout(title='Disaster Counts by Year', xaxis_title='Year', yaxis_title='Disaster Count')

    # Get HTML code for Plotly figure
    line_chart_html = fig.to_html(full_html=False)
    return line_chart_html


def create_disaster_map():
    # Count disasters by country using Django ORM
    counts = (
        DisasterList.objects
        .values('country')
        .annotate(disaster_count=models.Count('dis_id'))
    )

    # Convert data to Plotly format
    data = [go.Choropleth(
        locations=list(counts.values_list('country', flat=True)),
        z=list(counts.values_list('disaster_count', flat=True)),
        locationmode='country names',
        colorscale='Reds',
        colorbar_title='Disaster Count'
    )]
    # Create Plotly figure object
    fig = go.Figure(data=data, layout=go.Layout(
        title=go.layout.Title(text='Disaster Map'),
        geo=go.layout.Geo(
            projection_type='natural earth',
            showcoastlines=True
        )
    ))
    # Get HTML code for Plotly figure
    map_chart_html = fig.to_html(full_html=False)
    return map_chart_html


def index(request):
    # Create pie chart object by disaster_group
    pie_chart_html = create_disaster_pie_chart()

    # Create Plotly line chart of disaster counts by year
    line_chart_html = create_disaster_line_chart()

    # Create Plotly map of disaster countries
    map_chart_html = create_disaster_map()

    # Count the number of records in the database
    num_disasters = DisasterList.objects.count()

    # Count the number of unique years in the database
    num_years = DisasterList.objects.order_by().values('year').distinct().count()

    # Count the number of unique disaster types in the database
    num_disaster_types = DisasterList.objects.order_by().values('disaster_type').distinct().count()

    # Count the number of unique countries in the database
    num_countries = DisasterList.objects.order_by().values('country').distinct().count()

    # Create tables of top 10 affected and damaged countries
    top_10_affected_table = create_top_10_affected_countries()
    top_10_damaged_table = create_top_10_damaged_countries()

    # Render the template with the data
    return render(request, 'disaster_dashboard/index.html', {
        'pie_chart_html': pie_chart_html,
        'line_chart_html': line_chart_html,
        'map_chart_html': map_chart_html,
        'num_disasters': num_disasters,
        'num_years': num_years,
        'num_disaster_types': num_disaster_types,
        'num_countries': num_countries,
        'top_10_affected_table': top_10_affected_table,
        'top_10_damaged_table': top_10_damaged_table,
    })


