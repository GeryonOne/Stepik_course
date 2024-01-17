def countries_and_cities():
    countries_count = int(input())
    country_dict = {}

    for i in range(countries_count):
        country_cities_string = input().split()
        country_dict[country_cities_string[0]] = country_cities_string[1:]

    requests_count = int(input())
    for i in range(requests_count):
        current_request = input()
        for key, value in country_dict.items():
            if current_request in value:
                print(key)


countries_and_cities()
