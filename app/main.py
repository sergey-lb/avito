from lib import create_apartment, add_apartment, search_apartments

apartments = []

apartment1 = create_apartment(
    '2-х комнатная квартира',
    2,
    47,
    'Вахитовский район',
    'Вишневского',
    '51',
    '44',
    4_300_000
)

apartment2 = create_apartment(
    '1 комнатная квартира',
    1,
    27,
    'Авиастроительный район',
    'Лукина',
    '1',
    '25',
    2_000_000
)

apartment3 = create_apartment(
    '1 комнатная квартира',
    1,
    35,
    'Приволжский район',
    'Профессора Камая',
    '8',
    '45',
    3_200_000
)

add_apartment(apartments,apartment1)
add_apartment(apartments,apartment2)
add_apartment(apartments,apartment3)

print(search_apartments(apartments))
print(search_apartments(apartments, search_regions = ['Вахитовский район', 'Приволжский район']))
print(search_apartments(apartments, search_regions = ['Вахитовский район', 'Приволжский район'], search_price=3_500_000))
print(apartments)
