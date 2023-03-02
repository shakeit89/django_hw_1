import csv
from pagination import settings

def get_bus_stations(filename=settings.BUS_STATION_CSV):

    with open(filename, 'r', encoding='UTF-8') as csvfile:
        bus_reader = csv.DictReader(csvfile)
        bus_reader2 = [x for x in bus_reader]

    return bus_reader2

if __name__ == '__main__':
    a = get_bus_stations()
    for row in a:
        print(a)

