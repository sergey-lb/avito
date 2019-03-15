def create_apartment(title, number_of_rooms, area, region, street, house, apartment_number, price):

    return {
        'title': title,
        'number_of_rooms': number_of_rooms,
        'area': area,
        'region': region,
        'street': street,
        'house': house,
        'apartment_number': apartment_number,
        'price': price
    }


def add_apartment(container, apartment):
    container.append(apartment)


def search_apartments(container, search_regions=None, search_price=None):

    result = container.copy()

    if search_regions is not None:
        search_regions = map(str.strip, search_regions)
        search_regions = list(map(str.lower, search_regions))

        def filter_by_regions(apartment):
            apartment_region = apartment['region']
            apartment_region = apartment_region.strip().lower()
            return apartment_region in search_regions

        result = list(filter(filter_by_regions, result))

    if search_price is not None:
        result = list(filter(lambda apartment: apartment['price'] < search_price, result))

    return result
