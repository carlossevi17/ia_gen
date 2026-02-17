import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Google AI Art", page_icon="🎨", layout="wide")

# Diseño Dark Mode personalizado
st.markdown("""
    <style>
    .stApp { background-color: #111; color: white; }
    .stButton>button { width: 100%; background-color: #4285F4; color: white; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Google Imagen AI Generator")

# 2. SIDEBAR - API KEY Y ESTILOS
with st.sidebar:
    st.header("🔑 Configuración")
    api_key = st.text_input("Introduce tu Google API Key", type="password")
    
    st.divider()
    
    st.header("🎨 Personalización")
    estilo = st.selectbox("Elige el estilo:", 
                          ["Fotorealista", "Arte Digital", "Óleo", "Cyberpunk", "Anime", "Sketch"])
    
    aspecto = st.radio("Relación de aspecto:", ["1:1", "16:9", "9:16"])

# 3. LÓGICA DE GENERACIÓN
if api_key:
    genai.configure(api_key=api_key)
    # Usamos el modelo imagen-3 (o el más reciente disponible en tu cuenta)
    model = genai.GenerativeModel('imagen-3.0-generate-001') 

prompt_usuario = st.text_area("¿Qué quieres que cree?", placeholder="Un paisaje futurista de una ciudad flotante...")

if st.button("GENERAR IMAGEN"):
    if not api_key:
        st.error("❌ Necesitas la API Key de Google.")
    elif not prompt_usuario:
        st.warning("⚠️ Escribe una descripción.")
    else:
        with st.spinner("✨ Google AI está trabajando en tu imagen..."):
            try:
                # Combinamos el prompt con el estilo seleccionado
                full_prompt = f"{prompt_usuario}, in {estilo} style, high quality, {aspecto} aspect ratio"
                
                # LLAMADA REAL A LA API
                response = model.generate_content(full_prompt)
                
                # La API de Google devuelve la imagen en la respuesta
                # Nota: Dependiendo de tu región, esto puede variar ligeramente en el objeto response
                image_data = response.candidates[0].content.parts[0].inline_data.data
                
                # Convertir bytes a imagen de PIL
                img = Image.open(io.BytesIO(image_data))
                
                # MOSTRAR EN APP
                st.image(img, caption="Tu imagen generada con Google AI", use_container_width=True)
                
                # BOTÓN DE DESCARGA
                buf = io.BytesIO()
                img.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="📥 Descargar Imagen",
                    data=byte_im,
                    file_name="google_ai_image.png",
                    mime="image/png"
                )
                
            except Exception as e:
                st.error(f"Error al generar: {e}")
                st.info("Asegúrate de que el modelo 'imagen-3' esté habilitado en tu Google AI Studio.")
            except Exception as e:
                st.error(f"Error al conectar con Nano Banana: {e}")

st.markdown("---")
st.caption("Si ves una imagen de carga, espera unos segundos a que el servidor responda.")
