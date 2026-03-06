import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("AK Diams Etsy SEO Generator")

product = st.text_input("Product")
stone = st.text_input("Stone")
shape = st.text_input("Shape")
metal = st.text_input("Metal")
style = st.text_input("Style")
occasion = st.text_input("Occasion")

if st.button("Generate SEO Listing"):

    prompt = f"""
    Generate an Etsy SEO optimized listing.

    Product: {product}
    Stone: {stone}
    Shape: {shape}
    Metal: {metal}
    Style: {style}
    Occasion: {occasion}

    Generate:

    1 SEO Title
    13 Etsy Tags
    Etsy Attributes
    Keywords
    Description
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    st.write(response.output_text)
