import requests

def get_country_info(country_name:str):

    path_list = ["/population", "/positions", "/currency"]

    response_list = make_api_requisitions_in_bulk(
        path_list = path_list,
        country_name = country_name
    )

    measurement_year = response_list[0]["data"]["populationCounts"][-1]["year"]
    population_measure = response_list[0]["data"]["populationCounts"][-1]["value"]
    position_latitude = response_list[1]["data"]["lat"]
    position_longitude = response_list[1]["data"]["long"]
    currency_abreviation = response_list[2]["data"]["currency"]

    final_response = {
        f"{country_name}":{
            "population_measurement": 
                {"measurement_year": measurement_year, "population_measure": population_measure},
            "position_latitude": position_latitude,
            "position_longitude": position_longitude,
            "currency_abreviation": currency_abreviation}
    }

    return final_response

def make_api_requisitions_in_bulk(path_list:list, country_name:str):

    response_list = []

    country_payload = {
        "country": country_name
    }
    api_url = "https://countriesnow.space/api/v0.1/countries"

    for path in path_list:

        response = requests.post(
            url = api_url + path,
            data = country_payload
        )

        response_list.append(response.json())
    
    return response_list