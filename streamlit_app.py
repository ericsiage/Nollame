import streamlit as st
import pandas as pd

st.write("""
# App - No llame
""")
#st.logo(image="flowblanco.jpg")

# Especifica la ruta completa del archivo Excel
df = pd.read_excel(r"Datos No llame - actual.xlsx")
df['Numeros'] = df['Numeros'].astype(str)
# Verifica si el DataFrame tiene datos antes de graficar
if not df.empty:
    st.dataframe(df[['Numeros']], height=200, width=500,hide_index=True)
else:
    st.write("El DataFrame está vacío.")
