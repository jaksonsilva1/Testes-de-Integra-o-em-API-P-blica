# Testes de Integração com a API OpenWeatherMap

## Descrição
Este projeto realiza testes de integração na API pública OpenWeatherMap, que fornece dados sobre clima e condições meteorológicas.

## Como Rodar os Testes
1. Obtenha uma chave de API gratuita no site [OpenWeatherMap](https://openweathermap.org/api).
2. Substitua `YOUR_API_KEY` no arquivo `test_api.py` pela sua chave de API.
3. Instale as dependências:
   ```bash
   pip install pytest requests
4. executar teste python -m pytest -v


🚀 Como executar os testes
Clone ou baixe este repositório.
Navegue até a pasta do projeto.
Execute os testes com o comando:
bash
Copiar código
pytest nome_do_arquivo.py
🧪 Testes Implementados
test_get_weather_success:

Verifica se a API retorna o status 200 para uma cidade válida (Manaus).
Valida que os campos principais (main e temp) estão presentes na resposta.
test_get_weather_invalid_city:

Testa o comportamento da API para uma cidade inexistente (CidadeInexistente).
Espera o status 404 e a mensagem "city not found".
test_weather_contains_coordinates:

Valida que a resposta contém as coordenadas (latitude e longitude) para uma cidade válida (São Paulo).
test_weather_temperature_range:

Testa se a temperatura retornada está dentro de uma faixa plausível (-50°C a 60°C) para a cidade (Rio de Janeiro).
test_get_weather_without_api_key:

Verifica o comportamento da API ao omitir a chave de API.
Espera o status 401 com a mensagem "Invalid API key".
🛠️ Estrutura do Código
Bibliotecas:

requests: Usada para realizar as requisições HTTP.
pytest: Framework para criação e execução de testes.
Parâmetros da API:

q: Nome da cidade.
appid: Chave de autenticação (obtida da variável de ambiente).
units: Unidade de medida (metric para Celsius).
⚠️ Observações
A API gratuita do OpenWeatherMap possui limites de requisições por minuto. Use-a com moderação para evitar bloqueios.
📖 Referências
Documentação da API do OpenWeatherMap
Guia de Uso do Pytest
