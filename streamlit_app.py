import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection



st.set_page_config(page_title="No llame",page_icon="flowlogo.PNG")

hide_streamlit_style = """
            <style>
            .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{ display: none; } #MainMenu{ visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }
            </style>
                        """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#




#Title
st.title("""  App - No llame
""")

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)


df = conn.read()
#Columna Numeros - str datatype

telefonos = df["Numeros"].astype(str)

valor = ""
busqueda = st.text_input(label="Busca un número sin 0 adelante,sin espacios en blanco y sin código país. (ejemplo: 99123456)", value=valor, type="default", label_visibility="visible")

# Verifica si el input está vacío
if not busqueda:
    st.write("")
else:
    # Print results.
    if busqueda in telefonos.values:
        # Si el número exacto se encuentra, mostrar el mensaje correspondiente
        st.write("Número encontrado: ", busqueda)
    else:
        # Filtrar el DataFrame por el texto ingresado
        df_filtrado = df[telefonos.str.contains(busqueda, na=False)]
        df_filtrado = df_filtrado.astype(str)
        if not df_filtrado.empty:
            st.dataframe(df_filtrado, height=100, width=500, hide_index=True)
        else:
            st.write("No se encontraron coincidencias.")