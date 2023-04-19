import streamlit as st

# Crear una lista de diccionarios con los datos financieros
datos_financieros = [
    {"Empresa": "Apple", "Ingresos (millones de USD)": 274515, "Ganancias netas (millones de USD)": 57411},
    {"Empresa": "Amazon", "Ingresos (millones de USD)": 386064, "Ganancias netas (millones de USD)": 21320},
    {"Empresa": "Microsoft", "Ingresos (millones de USD)": 165027, "Ganancias netas (millones de USD)": 44615},
    {"Empresa": "Alphabet", "Ingresos (millones de USD)": 181690, "Ganancias netas (millones de USD)": 40690},
    {"Empresa": "Facebook", "Ingresos (millones de USD)": 85727, "Ganancias netas (millones de USD)": 29456},
]

# Crear una tabla con los datos financieros
st.table(datos_financieros)
