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
## Testes Implementados
1. test_get_weather_success
Objetivo: Verifica se a API retorna o status 200 para uma cidade válida (Manaus).
Validações:
Confirma que os campos principais (main e temp) estão presentes na resposta.
2. test_get_weather_invalid_city
Objetivo: Testa o comportamento da API para uma cidade inexistente (CidadeInexistente).
Validações:
Espera o status 404.
Verifica se a mensagem retornada é "city not found".
3. test_weather_contains_coordinates
Objetivo: Valida que a resposta contém as coordenadas (latitude e longitude) para uma cidade válida (São Paulo).
Validações:
Garante que os campos lat e lon estão presentes na resposta.
4. test_weather_temperature_range
Objetivo: Testa se a temperatura retornada está dentro de uma faixa plausível para a cidade (Rio de Janeiro).
Validações:
Verifica se a temperatura está entre -50°C e 60°C.
5. test_get_weather_without_api_key
Objetivo: Verifica o comportamento da API ao omitir a chave de API.
Validações:
Espera o status 401.
Confirma que a mensagem retornada contém "Invalid API key".
## Estrutura do Código
Bibliotecas:

requests: Usada para realizar as requisições HTTP.
pytest: Framework para criação e execução de testes.
Parâmetros da API:

q: Nome da cidade.
appid: Chave de autenticação (obtida da variável de ambiente ou substituída no código).
units: Unidade de medida (metric para Celsius).
## Observações
Limites de Requisições:
A API gratuita do OpenWeatherMap possui limites de requisições por minuto. Use-a com moderação para evitar bloqueios.
Segurança da API Key:
Não inclua sua chave diretamente no código. Utilize variáveis de ambiente sempre que possível.
📖 Referências
Documentação da API do OpenWeatherMap
Guia de Uso do Pytest
