import json
import requests


def get_covid_info_json(country: str):
    url = 'https://rapidapi.p.rapidapi.com/statistics'
    query = {"country": f"{country}"}
    headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "f349d1ec63msh34618b0f4aa61f0p1a8188jsne72bc4735b2a"
    }
    response = requests.request("GET", url, headers=headers, params=query)
    return response.json()


def print_json_to_info(info: json):
    response = info['response'][0]
    cases = response['cases']
    deaths = response['deaths']
    tests = response['tests']

    date_unformatted = str(response['day'])
    date_array = date_unformatted.split('-')
    date = f'{date_array[2]}/{date_array[1]}/{date_array[0]}'

    time_unformatted = str(response['time'])
    time_array = time_unformatted.replace(f'{date_unformatted}T', '').split(':')
    time = f'{time_array[0]}:{time_array[1]}:{time_array[2][:-3]}'

    print(f'Country: {response["country"]}')
    print(f'Population: {response["population"]}')

    print(f'Total cases: {cases["total"]}')
    print(f'    New: {cases["new"]}')
    print(f'    Active: {cases["active"]}')
    print(f'    Critical: {cases["critical"]}')
    print(f'    Recovered: {cases["recovered"]}')

    print(f'Total deaths: {deaths["total"]}')
    print(f'    New: {deaths["new"]}')

    print(f'Total tests: {tests["total"]}')
    print(f'Date: {date}')
    print(f'Time: {time}')


def main():
    country = input('Enter the name of your country: ')
    info_json = get_covid_info_json(country=country)
    print_json_to_info(info_json)


if __name__ == '__main__':
    main()
