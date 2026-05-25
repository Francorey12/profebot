"""
ProfeBot - Tutor de programación para adolescentes
Proyecto de portafolio para rol de AI Trainer
Autor: Jean Franco Rey Ardila
"""

import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os


# CONFIGURACIÓN INICIAL

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("⚠️ No se encontró GEMINI_API_KEY en el archivo .env")
    st.stop()
    
# Cliente del nuevo SDK - guardado en session_state para persistir 
# entre reejecuciones de Streamlit
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=API_KEY)

client = st.session_state.client

# CARGA DEL SYSTEM PROMPT

def cargar_system_prompt():
    """
    Lee el prompt activo desde system_prompt.md.
    Busca el contenido delimitado por las tags <prompt_activo>...</prompt_activo>.
    """
    try:
        with open("prompts/system_prompt.md", "r", encoding="utf-8") as f:
            contenido = f.read()
        
        tag_inicio = "<prompt_activo>"
        tag_fin = "</prompt_activo>"
        
        inicio = contenido.find(tag_inicio)
        fin = contenido.find(tag_fin)
        
        if inicio == -1 or fin == -1:
            st.warning("⚠️ No se encontraron las tags <prompt_activo>. Usando fallback.")
            return "Eres ProfeBot, un tutor de programación para adolescentes."
        
        inicio_contenido = inicio + len(tag_inicio)
        return contenido[inicio_contenido:fin].strip()
    
    except FileNotFoundError:
        st.error("⚠️ No se encontró el archivo prompts/system_prompt.md")
        return "Eres ProfeBot, un tutor de programación para adolescentes."

SYSTEM_PROMPT = cargar_system_prompt()
MODELO = "gemini-2.5-flash"

# INICIALIZACIÓN DEL ESTADO

# El nuevo SDK maneja chats con un objeto distinto
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model=MODELO,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )
    st.session_state.mensajes = []

# INTERFAZ

st.set_page_config(
    page_title="ProfeBot — Tutor de Programación",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ProfeBot")
st.caption("Tutor de programación para adolescentes — Powered by Gemini")

# Sidebar
with st.sidebar:
    st.header("Opciones")
    if st.button("🔄 Nueva conversación"):
        st.session_state.chat = client.chats.create(
            model=MODELO,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )
        st.session_state.mensajes = []
        st.rerun()
    
    st.divider()
    st.markdown("### Sobre este proyecto")
    st.markdown(
        "ProfeBot es un asistente educativo diseñado para enseñar "
        "programación a adolescentes (14-16 años).\n\n"
        "Proyecto de portafolio para rol de AI Trainer."
    )
    
    st.divider()
    st.markdown(f"**Modelo:** `{MODELO}`")
    st.markdown("**Stack:** Python · Streamlit · Google GenAI SDK")

# Mostrar historial
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["rol"]):
        st.markdown(mensaje["contenido"])

# Input y respuesta
if prompt_usuario := st.chat_input("Escribe tu pregunta sobre programación..."):
    
    st.session_state.mensajes.append({
        "rol": "user",
        "contenido": prompt_usuario
    })
    
    with st.chat_message("user"):
        st.markdown(prompt_usuario)
    
    with st.chat_message("assistant"):
        with st.spinner("ProfeBot está pensando..."):
            try:
                respuesta = st.session_state.chat.send_message(prompt_usuario)
                texto_respuesta = respuesta.text
                st.markdown(texto_respuesta)
                
                st.session_state.mensajes.append({
                    "rol": "assistant",
                    "contenido": texto_respuesta
                })
            except Exception as e:
                st.error(f"Ups, algo salió mal: {str(e)}")