import requests
from bs4 import BeautifulSoup


def first_site_json():
    result = []
    URL = "https://www.mebelshara.ru/contacts"
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    offices = soup.body.find_all('div', attrs={'class': 'shop-list-item'})
    cities = soup.body.find_all('h4', attrs={'class': 'js-city-name'})
    cityNames = [cities[i].string for i in range(len(cities))]
    currCityNum = -1
    currCity = cityNames[0]

    for office in offices:
        if office.attrs.get('data-shop-number') == "1":
            currCityNum += 1
            currCity = cityNames[currCityNum] + ", "
        address = currCity + office.attrs.get('data-shop-address')
        latlon = [float(office.attrs.get('data-shop-latitude')), float(office.attrs.get('data-shop-longitude'))]
        name = office.attrs.get('data-shop-name')
        phones = "0"
        mode1, mode2 = office.attrs.get('data-shop-mode1'), office.attrs.get('data-shop-mode2')
        if mode1 == "Без выходных:" or mode1 == "Без выходных":
            working_hours = ["пн-вс: {}".format(mode2)]
        else:
            working_hours = [mode1, mode2]

        parsedOffice = {
            "address": address,
            "latlon": latlon,
            "name": name,
            "phones": phones,
            "working_hours": working_hours,
        }
        result.append(parsedOffice)

    return result
