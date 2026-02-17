import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# Configuración de la interfaz
st.set_page_config(page_title="Nano Banana Pro", page_icon="🍌", layout="wide")

# CSS para que se vea "chula" de verdad
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextArea textarea { border: 2px solid #f4d03f !important; }
    .generate-btn { 
        background-color: #f4d03f !important; 
        color: black !important; 
        font-weight: bold !important;
        padding: 0.5rem 2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ PixelForge: Nano Banana AI")
st.write("Generación de imágenes de alta fidelidad en tiempo real.")

# --- SIDEBAR ---
with st.sidebar:
    st.header("🔑 Configuración")
    api_key = st.text_input("Nano Banana API Key", type="password")
    
    st.divider()
    st.header("⚙️ Parámetros")
    style = st.selectbox("Estilo", ["Cinematic", "Photorealistic", "Digital Art", "Anime", "Cyberpunk"])
    aspect_ratio = st.radio("Formato", ["1:1", "16:9", "9:16"])

# --- ÁREA PRINCIPAL ---
col1, col2 = st.columns([1, 1])

with col1:
    prompt = st.text_area("Describe tu visión:", height=150, placeholder="Un astronauta cabalgando un unicornio en los anillos de Saturno, estilo 8k...")
    generate_btn = st.button("🚀 GENERAR IMAGEN", use_container_width=True)

with col2:
    if generate_btn:
        if not api_key:
            st.error("❌ Introduce tu API Key para continuar.")
        elif not prompt:
            st.warning("⚠️ El prompt está vacío.")
        else:
            with st.spinner("🧠 Nano Banana está procesando..."):
                try:
                    # CONFIGURACIÓN DE LA LLAMADA (Ajusta la URL a la de tu proveedor)
                    # Nano Banana suele ser un modelo servido vía API (ej. Replicate, Together, o propia)
                    api_url = "TU_URL_DE_ENDPOINT_AQUÍ" 
                    headers = {"Authorization": f"Bearer {api_key}"}
                    payload = {
                        "prompt": f"{prompt}, {style} style",
                        "aspect_ratio": aspect_ratio
                    }

                    # Petición real
                    response = requests.post(api_url, json=payload, headers=headers)
                    
                    if response.status_code == 200:
                        # LEER BYTES DE LA IMAGEN
                        # Si la API devuelve la imagen directa:
                        img_data = response.content 
                        img = Image.open(BytesIO(img_data))
                        
                        # MOSTRAR IMAGEN REAL
                        st.image(img, caption="Resultado final", use_container_width=True)
                        
                        # BOTÓN DE DESCARGA
                        buf = BytesIO()
                        img.save(buf, format="PNG")
                        st.download_button(
                            label="📥 Descargar en alta calidad",
                            data=buf.getvalue(),
                            file_name="generacion_banana.png",
                            mime="image/png"
                        )
                    else:
                        st.error(f"Error de API: {response.status_code} - {response.text}")
                
                except Exception as e:
                    st.error(f"Error crítico: {e}")
    else:
        # Estado vacío para que no se vea feo al principio
        st.info("Escribe algo y dale a generar para ver el resultado aquí.")

st.divider()
st.caption("Desarrollado con Streamlit y Nano Banana")
