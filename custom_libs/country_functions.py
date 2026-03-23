import requests

def get_country_info(country_name):

    api_url = "https://countriesnow.space/api/v0.1/countries"

    country_payload = {
        "country": country_name
    }

    response_population = requests.post(
        url = api_url + "/population",
        data = country_payload
    )

    # TODO: Fazer o resto das requisições e juntar tudo

    return response_population.json()