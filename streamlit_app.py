# Importamos las bibliotecas necesarias
import streamlit as st
import requests

# Definimos la función para obtener el precio más bajo del producto
def get_lowest_price():
    # Configuramos los encabezados y el mensaje
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 8eu3RBqG1GHlubaZwW4k:d16d7aaf71ae7b1f7ffcb2d009ba1df36b6132d85a6870c75b0ca8737db73edb"
    }
    message = {
        "role": "user",
        "content": "¿Cuál es el precio más bajo de un producto en Guatemala?"
    }

    # Realizamos la solicitud a la API
    response = requests.post("https://api.chat.jina.ai/v1/chat/completions", headers=headers, json={"messages": [message]})

    # Extraemos el precio del producto de la respuesta
    price = float(response.json()["choices"][0]["message"]["content"].strip().split(":")[-1])

    # Devolvemos el precio
    return price

# Creamos la aplicación de Streamlit
st.title("Precio de Producto en Guatemala")

# Mostramos el precio más bajo del producto
price = get_lowest_price()
st.write(f"El precio más bajo de un producto en Gu
