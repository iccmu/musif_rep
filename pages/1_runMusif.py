import streamlit as st
import urllib.request
import zipfile
from pathlib import Path
import os
# Crear un selectbox para elegir entre Classical, Pop Rock y Subir contenido
genre = st.selectbox(
    'Elige un corpus',
    ('Classical', 'Pop Rock', 'Subir contenido')  # Añadida la opción 'Subir contenido'
)

# Mostrar el género seleccionado
st.write(f'Has seleccionado: {genre}')

# Puedes usar la variable 'genre' para realizar acciones específicas basadas en la selección
if genre == 'Classical':
    st.write('Has elegido música clásica. Aquí puedes agregar contenido relacionado con la música clásica.')
elif genre == 'Pop Rock':
    st.write('Has elegido Pop Rock.')

elif genre == 'Subir contenido':
    st.write('Has elegido subir contenido. Por favor, elige un archivo para subir.')
    uploaded_file = st.file_uploader("Elige un archivo")
    if uploaded_file is not None:
        # Procesar el archivo subido
        st.write("Archivo subido con éxito")
        # ... código adicional para manejar el archivo subido ...

