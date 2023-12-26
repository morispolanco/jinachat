import streamlit as st
import claude2

st.title("Buscador de precios en Guatemala")

product = st.text_input("Ingrese el producto a buscar")

if product:
    with st.spinner("Buscando precios..."):
        search_query = f"{product} precio más bajo Guatemala"
        search_results = claude2.search(search_query, sources=["web"])

    min_price = None
    min_price_source = None
    for result in search_results["search_results"]:
        if result.get("price") and (not min_price or result["price"] < min_price):
            min_price = result["price"]  
            min_price_source = result["source"]

    if min_price:
        st.success(f"El precio más bajo encontrado de {product} es {min_price} en {min_price_source}")
    else: 
        st.error("No se encontraron resultados con precio para este producto")
