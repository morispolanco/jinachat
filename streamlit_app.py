import streamlit as st
import requests

# Función para realizar la solicitud a la API
def get_lowest_price(product_name):
    api_url = "https://api.chat.jina.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 8eu3RBqG1GHlubaZwW4k:d16d7aaf71ae7b1f7ffcb2d009ba1df36b6132d85a6870c75b0ca8737db73edb",
    }

    payload = {
        "messages": [{"role": "user", "content": f"Find the lowest price of {product_name}"}]
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["completions"][0]["content"]
    else:
        return f"Error: {response.status_code}"

# Configuración de la interfaz de Streamlit
st.title("Lowest Price Finder")

# Obtener el nombre del producto del usuario
product_name = st.text_input("Enter the product name:")
if product_name:
    # Obtener el precio más bajo utilizando la API
    lowest_price = get_lowest_price(product_name)

    # Mostrar el resultado en la interfaz
    st.success(f"The lowest price of {product_name} is: {lowest_price}")
