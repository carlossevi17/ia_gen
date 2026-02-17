import streamlit as st
import requests  # Para conectar con la API de Nano Banana

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Nano Banana Art Gen", page_icon="🍌", layout="centered")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .stTextInput > div > div > input { background-color: #fffde7; }
    .stTextArea > div > div > textarea { background-color: #f1f8e9; }
    .generate-btn { font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍌 Nano Banana Image Generator")
st.info("Introduce tu API Key en la barra lateral para comenzar a crear.")

# --- SIDEBAR: CONFIGURACIÓN Y API KEY ---
with st.sidebar:
    st.header("🔑 Autenticación")
    api_key = st.text_input("Nano Banana API Key", type="password", help="Tu clave se mantendrá segura durante la sesión.")
    
    st.divider()
    st.header("🎨 Ajustes de Imagen")
    aspect_ratio = st.selectbox("Relación de aspecto", ["1:1", "16:9", "9:16", "4:3"])
    style_preset = st.selectbox("Estilo", ["Cinematic", "Digital Art", "Photorealistic", "Anime", "Cyberpunk"])
    seed = st.number_input("Seed (Opcional)", value=0, help="Usa el mismo número para resultados similares")

# --- CUERPO PRINCIPAL ---
prompt = st.text_area("✍️ Describe tu imagen...", placeholder="Un volcán de chocolate erupcionando sobre una ciudad de gominola, estilo macro...")

if st.button("🚀 Generar Imagen", use_container_width=True):
    if not api_key:
        st.error("⚠️ Por favor, introduce tu API Key en la barra lateral.")
    elif not prompt:
        st.warning("⚠️ El prompt no puede estar vacío.")
    else:
        with st.spinner("⏳ Nano Banana está procesando tu visión artística..."):
            # Aquí simulamos la llamada a la API de Nano Banana
            # Debes sustituir el endpoint por el real de tu proveedor
            try:
                # Ejemplo de estructura de llamada (ajustar según doc de Nano Banana)
                headers = {"Authorization": f"Bearer {api_key}"}
                payload = {
                    "prompt": f"{prompt}, {style_preset} style",
                    "aspect_ratio": aspect_ratio,
                    "seed": seed
                }
                
                # NOTA: Sustituye 'URL_DE_LA_API' por la dirección real del endpoint
                # response = requests.post("https://api.nanobanana.ai/v1/generate", json=payload, headers=headers)
                # image_url = response.json().get("url")
                
                # Simulación para visualización
                st.success("¡Imagen generada con éxito!")
                # st.image(image_url) 
                st.balloons()
                
            except Exception as e:
                st.error(f"Error de conexión: {e}")

st.markdown("---")
st.caption("Hecho con ❤️ y Nano Banana AI")
