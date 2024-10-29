import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Configuración de la página
st.set_page_config(page_title="No llame", page_icon="flowlogo.PNG", initial_sidebar_state="expanded", layout="wide")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;}
        .stAppDeployButton {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden !important;}
        .css-1yi6l {display: none}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Título
st.title("App - No llame")

# Crear objeto de conexión
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

# Columna Numeros - convertir a tipo str sin .0
telefonos = df["Numeros"].astype(int).astype(str)

# Input de búsqueda
busqueda = st.text_input(label="Busca un número sin 0 adelante, sin espacios en blanco y sin código país (ejemplo: 99123456)", value="", label_visibility="visible")

# Verifica si el input tiene más de 8 caracteres
if busqueda and len(busqueda) > 8:
    st.error("Error: La búsqueda debe tener 8 caracteres o menos.")
else:
    # Procesar la búsqueda solo si el input no está vacío
    if busqueda:
        # Print results.
        if busqueda in telefonos.values:
            st.write("Número encontrado:", busqueda)
        else:
            # Filtrar el DataFrame por el texto ingresado
            df_filtrado = df[telefonos.str.contains(busqueda, na=False)]
            df_filtrado = df_filtrado.astype(int).astype(str)
            if not df_filtrado.empty:
                st.dataframe(df_filtrado, height=100, width=500, hide_index=True)
            else:
                st.write("No se encontraron coincidencias.")
