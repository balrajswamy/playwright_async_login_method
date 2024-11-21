import requests
import time
import pytest

api_key = "xxxxxx"
def fetch_weather(city,api_key):
    """Fetch weather data for a city synchronously."""

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,  # City name
        'appid': api_key,  # Your API key
    }
    headers = {"USER_AGENT":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}

    #response = requests.get(base_url, params=params)
    try:
        response = requests.get(base_url,params=params,headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("data\n", data)
            temp = data.get('main', {}).get('temp')
            #return f"weather in {city}: {temp}"
            temperature = data['main']['temp']
            return f"Weather in {city}: {data['weather'][0]['description']}, Temp: {temperature}°C"
        else:
            return f"Failed to fetch weather for {city} (HTTP {response.status_code})"
    except requests.RequestException as e:
        return f"Error fetching weather for {city}: {e}"


def synchronous_fetch(cities):
    """Fetch weather data for all cities synchronously."""
    results = []
    for city in cities:
        result = fetch_weather(city,api_key)
        results.append(result)
    return results


@pytest.fixture
def cities():
    """Fixture to provide the list of cities for testing."""
    return ["London", "New York", "Tokyo", "Delhi","Thanjavur"]


@pytest.mark.parametrize("city", ["London", "New York", "Tokyo", "Delhi"])
def test_synchronous(cities,city):
    start_time = time.time()
    results = synchronous_fetch(cities)
    end_time = time.time()

    # Assert that the results are in the correct format
    print("xxx=>", results)
    for result in results:
        #print("result=>",result)
        assert f"Weather in" in result
        assert f"Temp:" in result

    # Output the results and time spent
    for result in results:
        print(result)
    print(f"\nSynchronous approach took: {end_time - start_time:.2f} seconds")
