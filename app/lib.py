def create_apartment(title, number_of_rooms, area, region, street, house, apartment_number, price):

    region = region.strip()

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

    result = container
    if search_regions is not None:
        search_regions = map(str.strip, search_regions)
        search_regions = map(str.lower, search_regions)

        for apartment in result:
            apartment_region = apartment['region']
            apartment_region = apartment_region.lower()

            if apartment_region not in search_regions:
                result.remove(apartment)

    if search_price is not None:
        for apartment in result:
            if apartment['price'] >= search_price:
                result.remove(apartment)

    return result
