import streamlit as st
import requests

def obtener_precio_mas_bajo(nombre_producto):
    url_api = "https://api.chat.jina.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 8eu3RBqG1GHlubaZwW4k:d16d7aaf71ae7b1f7ffcb2d009ba1df36b6132d85a6870c75b0ca8737db73edb",
    }

    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"Buscar precio más bajo de {nombre_producto} en Guatemala"
            }
        ]
    }

    response = requests.post(url_api, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result["completions"][0]["content"]
    else:
        return f"Error: {response.status_code}"

# Configuración de la interfaz de Streamlit
st.title("Buscador de Precio Más Bajo en Guatemala")

# Obtener el nombre del producto del usuario
nombre_producto = st.text_input("Ingrese el nombre del producto:")
if nombre_producto:
    # Obtener el precio más bajo utilizando la API
    precio_mas_bajo = obtener_precio_mas_bajo(nombre_producto)

    # Mostrar el resultado en la interfaz
    st.success(f"El precio más bajo de {nombre_producto} en Guatemala es: {precio_mas_bajo}")
