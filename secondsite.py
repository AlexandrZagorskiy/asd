import requests


def second_site_json():
    result = []
    cities = requests.get("https://www.tui.ru/api/office/cities/")

    for city in range(len(cities.json())):
        URL = "https://www.tui.ru/api/office/list/"
        PARAMS = {
            'cityId': cities.json()[city]['cityId'],
            'subwayId': "",
            'hoursFrom': "",
            'hoursTo': "",
            'serviceIds': "all",
            'toBeOpenOnHolidays': 'false'
        }
        r = requests.get(url=URL, params=PARAMS)
        offices = r.json()

        for officeId in range(len(offices)):
            address = offices[officeId]['address']
            latlon = [offices[officeId]['latitude'], offices[officeId]['longitude']]
            name = offices[officeId]['name']
            phones = [offices[officeId]['phones'][phonesCount]['phone']
                      for phonesCount in range(len(offices[officeId]['phones']))]

            working_hours = ["пн-пт: {} до {}".format(offices[officeId]['hoursOfOperation']['workdays']['start'],
                                                     offices[officeId]['hoursOfOperation']['workdays']['end']),
                             "сб: {} до {}".format(offices[officeId]['hoursOfOperation']['saturday']['start'],
                                                  offices[officeId]['hoursOfOperation']['saturday']['end']),
                             "вс: {} до {}".format(offices[officeId]['hoursOfOperation']['sunday']['start'],
                                                  offices[officeId]['hoursOfOperation']['sunday']['end']),
                             ]

            parsedOffices = {
                "address": address,
                "latlon": latlon,
                "name": name,
                "phones": phones,
                "working_hours": working_hours,
            }
            result.append(parsedOffices)

    return result
