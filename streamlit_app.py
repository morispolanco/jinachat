import streamlit as st
import requests
from bs4 import BeautifulSoup

def obtener_precio_mas_bajo(nombre_producto):
    # Utilizar Google para realizar una búsqueda
    url_busqueda_google = f"https://www.google.com/search?q={nombre_producto}+precio+site:gt"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    respuesta = requests.get(url_busqueda_google, headers=headers)

    if respuesta.status_code == 200:
        # Utilizar BeautifulSoup para analizar la página y extraer información
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        # Ajustar según la estructura HTML de los resultados de búsqueda
        elemento_precio = soup.find("span", class_="BNeawe iBp4i AP7Wnd")
        if elemento_precio:
            return elemento_precio.text
        else:
            return "Precio no encontrado en los resultados de búsqueda"
    else:
        return f"Error al realizar la búsqueda: {respuesta.status_code}"

# Configuración de la interfaz de Streamlit
st.title("Buscador de Precio Más Bajo en Guatemala")

# Obtener el nombre del producto del usuario
nombre_producto = st.text_input("Ingrese el nombre del producto:")
if nombre_producto:
    # Obtener el precio más bajo utilizando la búsqueda de Google
    precio_mas_bajo = obtener_precio_mas_bajo(nombre_producto)

    # Mostrar el resultado en la interfaz
    st.success(f"El precio más bajo de {nombre_producto} en Guatemala es: {precio_mas_bajo}")
