import requests


def all():
    # Get all countries from api
    try:
        url = f"https://restcountries.com/v3.1/all"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        countries = response.json()
        mod_countries = []
        mod_country = {}
        for country in countries:
            mod_country["flag"] = country["flags"]["svg"]
            mod_country["name"] = country["name"]["common"]
            mod_country["population"] = "{:,}".format(country["population"])
            mod_country["region"] = country["region"]
            if "capital" in country:
                mod_country["capital"] = country["capital"][0]
            mod_countries.append(mod_country)
            mod_country = {}
        return mod_countries
    except (KeyError, TypeError, ValueError):
        return None


def get_country(q_country):
    try:
        url = f"https://restcountries.com/v3.1/name/{q_country}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        countries = response.json()
        mod_country = {}
        mod_country["currencies"] = []
        mod_country["languages"] = []
        mod_country["borders"] = []
        for country in countries:
            if country["name"]["common"].lower() == q_country.lower():
                mod_country["flag"] = country["flags"]["svg"]
                mod_country["name"] = country["name"]["common"]
                mod_country["population"] = "{:,}".format(
                    country["population"])
                mod_country["region"] = country["region"]
                if "capital" in country:
                    mod_country["capital"] = country["capital"][0]
                mod_country["tld"] = country["tld"]
                mod_country["subregion"] = country["subregion"]
                for currency in country["currencies"]:
                    mod_country["currencies"].append(
                        country["currencies"][currency]["name"])
                for language in country["languages"]:
                    mod_country["languages"].append(
                        country["languages"][language])
                if "borders" in country:
                    for border in country["borders"]:
                        mod_country["borders"].append(border)
                    codes = ",".join(mod_country["borders"])
                    names = get_names(codes)
                    mod_country["borders"] = names
        return mod_country
    except (KeyError, TypeError, ValueError):
        return None


def get_names(code):
    try:
        url = f"https://restcountries.com/v3.1/alpha?codes={code}"
        res = requests.get(url)
        res.raise_for_status()
    except requests.RequestException:
        return "None3"

    countries = res.json()
    names = []
    for country in countries:
        names.append(country["name"]["common"])
    return names
