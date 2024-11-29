import os
import requests
import pytest

# URL base e chave de API 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY", "ce44d5563dc0f1ec0513a3f154b87181")  # chave da api
def test_get_weather_success():
    """Teste de sucesso: verificar se a requisição retorna status 200 para uma cidade válida."""
    params = {"q": "Manaus", "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200
    data = response.json()
    assert "main" in data
    assert "temp" in data["main"]

def test_get_weather_invalid_city():
    """Teste de erro: simula uma cidade inexistente."""
    params = {"q": "CidadeInexistente", "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 404
    data = response.json()
    assert data.get("message") == "city not found"

def test_weather_contains_coordinates():
    """Valida se a resposta contém as coordenadas da cidade."""
    params = {"q": "São Paulo", "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200
    data = response.json()
    assert "coord" in data
    assert "lat" in data["coord"] and "lon" in data["coord"]

def test_weather_temperature_range():
    """Valida se a temperatura está em uma faixa plausível para o local."""
    params = {"q": "Rio de Janeiro", "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200
    data = response.json()
    temp = data["main"]["temp"]
    assert -50 <= temp <= 60

def test_get_weather_without_api_key():
    """Teste de erro: verificar comportamento ao omitir a chave de API."""
    params = {"q": "Manaus", "units": "metric"}  # Sem 'appid'
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 401
    data = response.json()
    assert "Invalid API key" in data.get("message", "")

