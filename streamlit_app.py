import streamlit as st
import requests

# Define the API endpoint and authorization header
api_endpoint = "https://api.chat.jina.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 8eu3RBqG1GHlubaZwW4k:d16d7aaf71ae7b1f7ffcb2d009ba1df36b6132d85a6870c75b0ca8737db73edb",
}

# Create a Streamlit app
st.title("Guatemala Product Price Finder")
product_name = st.text_input("Enter the name of the product you want to find the price of:")

# Send a request to the API with the product name
if st.button("Find Price"):
    data = {
        "messages": [
            {
                "role": "user",
                "content": f"What is the lowest price of {product_name} in Guatemala?",
            }
        ]
    }
    response = requests.post(api_endpoint, headers=headers, json=data)

    # Extract the price from the API response
    if response.status_code == 200:
        result = response.json()["completions"][0]["content"]
        price = float(result.split(" ")[2])
        st.write(f"The lowest price of {product_name} in Guatemala is {price} {result.split(' ')[3]}")
    else:
        st.error("Sorry, there was an error getting the price. Please try again.")
