import streamlit as st
import pandas as pd
import random

# Cargar Excel
df = pd.read_excel("productos.xlsx", sheet_name="Sheet1", dtype=str)

st.set_page_config(page_title="Buscador de Productos", layout="wide")
st.markdown("<h1 style='text-align:center; color:darkorange;'>🔎 Buscador de Productos</h1>", unsafe_allow_html=True)

# Input de búsqueda
sku_input = st.text_input("Escribe el SKU:")

# Colores de fondo alternados para las tarjetas
colores_fondo = ["#FFF9E6", "#E6F7FF", "#E6FFE6", "#FFE6F0", "#F0E6FF"]

if sku_input:
    productos = df[df['sku'] == sku_input]
    
    if not productos.empty:
        for idx, producto in productos.iterrows():
            color_tarjeta = random.choice(colores_fondo)  # fondo dinámico

            # Tarjeta llamativa
            st.markdown(f"""
                <div style="
                    border: 3px solid orange; 
                    border-radius: 20px; 
                    padding: 25px; 
                    margin-bottom: 25px;
                    background-color: {color_tarjeta};
                    box-shadow: 6px 6px 25px rgba(0,0,0,0.25);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                ">
                    <h2 style="
                        background-color: orange; 
                        color: white; 
                        text-align: center; 
                        padding: 15px; 
                        border-radius: 12px;
                        font-size: 24px;
                        margin-bottom: 20px;
                    ">{producto['titulo']}</h2>
            """, unsafe_allow_html=True)

            # Campos en dos columnas, con colores de contraste
            campos = {
                "Item ID": producto['item_id'],
                "SKU": producto['sku'],
                "Variantes": producto['variantes'],
                "Características Generales": producto['caracteristicas generales'],
                "Especificaciones Técnicas": producto['especificaciones tecnicas'],
                "Usos / Aplicaciones": producto['usos / aplicaciones'],
                "Modo de Uso Sugerido": producto['modo de uso sugerido'],
            }

            for key, value in campos.items():
                st.markdown(f"""
                    <div style="display: flex; padding: 8px 0;">
                        <div style="flex: 1; font-weight: bold; color:#444; background-color:#FFF3D6; padding:4px 8px; border-radius:5px;">{key}</div>
                        <div style="flex: 2; color:#222; background-color:#FFFFFF; padding:4px 8px; border-radius:5px; margin-left:5px;">{value}</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("SKU no encontrado")