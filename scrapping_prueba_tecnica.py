import requests
from bs4 import BeautifulSoup
import json

url = "https://www.bcentral.cl/inicio"

# Se realiza una solicitud GET a la página web
response = requests.get(url)

# Verificar que la solicitud a la pàgina fue exitosa
if response.status_code == 200:
    # Analizamos el contenido HTML de la pàgina con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        # Se utiliza soup.find para encontrar el elemento p que contiene el texto "UF".
        uf_element = soup.find('p', string="UF").find_next('p')
        uf_value = uf_element.get_text(strip=True) if uf_element else 'N/A'
        
        # Buscamos primero el elemento p con el texto "Dólar Observado" y luego el siguiente p que contiene el valor.
        usd_element = soup.find('p', string="Dólar Observado").find_next('p')
        usd_value = usd_element.get_text(strip=True) if usd_element else 'N/A'

        results = {
            "UF": uf_value,
            "USD": usd_value
        }

        print(json.dumps(results, indent=4))
    
    except Exception as e:
        print(f"Error al extraer los datos: {e}")
else:
    print(f"Error al acceder a la página: Status code {response.status_code}")
