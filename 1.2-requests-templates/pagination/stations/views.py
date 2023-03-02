from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from .bus_stations_from_csv import get_bus_stations



bus_station = get_bus_stations()
print(bus_station[0:6])
def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = request.GET.get('page', 1)
    paginator = Paginator(bus_station, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
