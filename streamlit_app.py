import streamlit as st
import requests

# Definir la URL de la API para obtener precios
API_URL = "https://api.scrapy-prices.com/prices"

def get_lowest_price(product_name):
    params = {"query": product_name, "country": "GT"}  # Guatemala
    response = requests.get(API_URL, params=params)
    data = response.json()

    if "error" in data:
        return None
    else:
        prices = data.get("prices", [])
        if prices:
            lowest_price = min(prices, key=lambda x: x["price"])
            return lowest_price["price"]
        else:
            return None

def main():
    st.title("Buscar Precio Más Bajo en Guatemala")

    # Interfaz de usuario
    product_name = st.text_input("Ingrese el nombre del producto:")
    if st.button("Buscar Precio"):
        if product_name:
            st.write(f"Buscando precios para: {product_name}")
            lowest_price = get_lowest_price(product_name)
            if lowest_price is not None:
                st.success(f"Precio más bajo encontrado: {lowest_price} GTQ")
            else:
                st.warning("No se encontraron precios para el producto especificado.")
        else:
            st.warning("Ingrese un nombre de producto válido.")

if __name__ == "__main__":
    main()
