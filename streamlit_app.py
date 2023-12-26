import streamlit as st
import requests
import json

# Configura las credenciales de la API
api_url = "https://api.chat.jina.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 8eu3RBqG1GHlubaZwW4k:d16d7aaf71ae7b1f7ffcb2d009ba1df36b6132d85a6870c75b0ca8737db73edb"
}

# Función que envía una solicitud a la API y devuelve el resultado
def get_prices(product_name):
    data = {
        "messages": [
            {
                "role": "user",
                "content": f"What is the lowest price for {product_name} in Guatemala?"
            }
        ]
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return response.json()

# Crea una interfaz de usuario para el usuario que permite ingresar el nombre del producto
st.title("Precio más bajo de un producto en Guatemala")
product_name = st.text_input
