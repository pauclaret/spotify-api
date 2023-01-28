import streamlit as st
import src.soporte_api as sa
import src.soporte_imagenes as si

st.write("Hola, buenos dias")

lista_sp = st.text_input("Introduce el link a tu lista de reproduccion")
num_canciones = st.text_input("¿Cuantas canciones tiene tu lista?")

if lista_sp != "" and num_canciones != "":
    num_canciones2 = sa.sacar_numero_canciones(num_canciones)
    print(num_canciones2)

    sp = sa.credenciales()

    lista_canciones = sa.sacar_canciones(lista_sp, num_canciones2, sp)
    df_canciones = sa.limpiar_datos(lista_canciones)
    st.dataframe(df_canciones[["usuario", "song"]], width = 700, height = 200)
    num_can, num_art, num_usu = sa.sacar_big_numbers(df_canciones)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"# Numero Ironhackers, {num_usu}")
    with col2:
        st.markdown(f"# Numero artistas, {num_art}")
    with col3:
        st.markdown(f"# Numero canciones, {num_can}")

    si.sacar_populares(df_canciones)
    st.image("images/popularidad.png")

    



else:
    st.write("necesito tu informacion")

