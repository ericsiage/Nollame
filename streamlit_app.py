import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection


PAGE_CONFIG = {"page_title":"No llame","page_icon":":phone:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

st.write("""
# App - No llame :phone:
""")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)


df = conn.read()
#Columna Numeros - str datatype
df['Numeros'] = df['Numeros'].astype(str)
# Print results.
if not df.empty:
    st.dataframe(df[['Numeros']], height=200, width=500,hide_index=True)
else:
    st.write("El DataFrame está vacío.")


#OLD
#st.logo(image="flowblanco.jpg")
# Especifica la ruta completa del archivo Excel
#df = pd.read_excel(r"Datos No llame - actual.xlsx")
#df['Numeros'] = df['Numeros'].astype(str)
# Verifica si el DataFrame tiene datos antes de graficar
#if not df.empty:
#    st.dataframe(df[['Numeros']], height=200, width=500,hide_index=True)
#else:
#    st.write("El DataFrame está vacío.")
