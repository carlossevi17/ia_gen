import streamlit as st
import requests
from io import BytesIO

# Configuración estética
st.set_page_config(page_title="Nano Banana AI", page_icon="🍌", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    stButton>button { width: 100%; border-radius: 10px; background-color: #f4d03f; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍌 Nano Banana Image Generator")
st.write("Crea imágenes increíbles con IA y descárgalas al instante.")

# Sidebar para la Key
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu API Key", type="password")
    st.info("La API de Nano Banana requiere una clave válida para procesar el prompt.")

# Entrada del usuario
prompt = st.text_area("¿Qué quieres que la IA dibuje?", placeholder="Un gato astronauta en Marte...")

if st.button("🚀 Generar Imagen"):
    if not api_key:
        st.error("⚠️ Falta la API Key en la barra lateral.")
    elif not prompt:
        st.warning("⚠️ Por favor, escribe un prompt.")
    else:
        with st.spinner("🎨 Pintando tu idea..."):
            try:
                # --- LLAMADA REAL A LA API ---
                # Sustituye 'URL_DE_NANO_BANANA' por el endpoint real (ej. https://api.nanobanana.ai/v1/generate)
                # response = requests.post("URL_DE_NANO_BANANA", 
                #                          headers={"Authorization": f"Bearer {api_key}"},
                #                          json={"prompt": prompt})
                
                # SIMULACIÓN DE RECEPCIÓN DE IMAGEN (Para que veas cómo se muestra)
                # En producción, usa: image_bytes = response.content
                # Aquí usamos una imagen de prueba real para que no veas el icono roto:
                img_url = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop"
                response = requests.get(img_url)
                image_bytes = response.content

                # 1. Mostrar la imagen
                st.image(image_bytes, caption="Tu creación artística", use_container_width=True)
                
                # 2. Crear botón de descarga
                st.download_button(
                    label="💾 Descargar Imagen (PNG)",
                    data=image_bytes,
                    file_name="mi_generacion_banana.png",
                    mime="image/png"
                )
                st.success("¡Imagen lista!")

            except Exception as e:
                st.error(f"Hubo un error en la conexión: {e}")

st.divider()
st.caption("Desarrollado con Streamlit y Nano Banana")
