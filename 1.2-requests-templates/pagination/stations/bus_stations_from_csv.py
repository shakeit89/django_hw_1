import csv
from django.conf import settings

def get_bus_stations(filename=settings.BUS_STATION_CSV):

    with open(filename, 'r', encoding='UTF-8') as csvfile:
        bus_reader = list(csv.DictReader(csvfile))
        # bus_reader2 = [x for x in bus_reader]

    return bus_reader

if __name__ == '__main__':
    a = get_bus_stations()
    print(a[0])

