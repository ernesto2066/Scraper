#Dependencias requeridas para correr el script pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import urllib.parse

# Archivo donde se guardarán los resultados
output_file = "resultados.txt"

# Set para evitar URLs repetidas
visited_urls = set()

def scrape(url, depth=0, max_depth=3):
    if url in visited_urls or depth > max_depth:
        return
    
    visited_urls.add(url)
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"Escaneando: {url}\n")
        
        print(f"Escaneando: {url}")
        
        for link in soup.find_all('a', href=True):
            next_url = urllib.parse.urljoin(url, link['href'])  # Maneja URLs relativas
            if next_url.startswith("http"):
                scrape(next_url, depth + 1, max_depth)
    except Exception as e:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"Error en {url}: {str(e)}\n")
        print(f"Error en {url}: {str(e)}")

# Limpiar archivo antes de iniciar
open(output_file, "w").close()

# URL inicial para escanear
#scrape("https://ernesto2066.github.io/Gomsoft-HTML5/")
#scrape("https://gomsoft.site/")
scrape("https://cctunja.org.co/")
