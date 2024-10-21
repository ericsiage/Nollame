import streamlit as st
import pandas as pd

st.write("""
# Hello *world!*
""")

# Especifica la ruta completa del archivo Excel
df = pd.read_excel(r"Nollame/Datos No llame - actual.xlsx", sheet_name="Hoja1")

# Verifica si el DataFrame tiene datos antes de graficar
if not df.empty:
    df[['Numeros']]
else:
    st.write("El DataFrame está vacío.")