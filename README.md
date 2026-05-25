# 🤖 ProfeBot — Tutor de Programación para Adolescentes

> Asistente conversacional impulsado por IA generativa, diseñado pedagógicamente para enseñar programación a estudiantes de 14 a 16 años.

**Proyecto de portafolio** para el rol de **AI Trainer**.
Construido con foco en **Prompt Engineering iterativo**, **diseño de experiencia conversacional** y **buenas prácticas de desarrollo con LLMs**.

---

## 🎯 ¿Qué es ProfeBot?

ProfeBot es un tutor virtual de programación cuyo system prompt fue diseñado y refinado iterativamente para enseñar a adolescentes. No es un chatbot genérico: cada decisión de comportamiento (tono, formato, manejo de términos en inglés, respuesta a frustración, etc.) está **documentada y justificada** en el repositorio.

El valor del proyecto **no está solo en el código**, sino en demostrar el proceso de pensamiento de un AI Trainer: cómo se diseña, prueba e itera un prompt usando evidencia real.

---

## 🚀 Stack Técnico

| Capa | Tecnología |
|------|-----------|
| Lenguaje | Python 3.14 |
| Framework UI | Streamlit |
| Modelo LLM | Google Gemini 2.5 Flash |
| SDK | `google-genai` (SDK actual de Google) |
| Variables de entorno | `python-dotenv` |
| Control de versiones | Git + GitHub |

---

## 📁 Estructura del Proyecto

```
profebot/
├── prompts/
│   └── system_prompt.md       # Iteraciones del prompt (v1 → v2 → v3)
├── dev/
│   └── test_modelos.py         # Script auxiliar para listar modelos disponibles
├── venv/                       # Entorno virtual (no se sube)
├── app.py                      # Aplicación principal
├── .env                        # Variables sensibles (no se sube)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Metodología de Prompt Engineering

El corazón del proyecto está en `prompts/system_prompt.md`, donde documento **tres iteraciones del system prompt**, cada una basada en problemas observados de la anterior:

### Versión 1 (v1) — Primera aproximación
Un prompt razonable pero genérico. Identifico explícitamente sus debilidades: adjetivos ambiguos ("claro", "paciente"), no anticipa casos límite, no instruye sobre términos en inglés.

### Versión 2 (v2) — Prompt estructurado con few-shot
Reescritura completa con:

- Audiencia definida con precisión (14-16 años, comparan con TikTok)
- Patrón estandarizado para términos en inglés (refuerzo gradual)
- Reglas explícitas de formato, tono y longitud
- Manejo específico de frustración adolescente
- Redirección amable de temas fuera de programación
- **Few-shot examples** (ejemplos contrastivos correctos)
- Estudiante elige el lenguaje al inicio (agencia pedagógica)
- Delimitado con tags XML `<prompt_activo>` para separar contenido activo de documentación

### Versión 3 (v3) — Iteración basada en testing real
Construida tras probar v2 con preguntas reales y observar fallas. Cambios documentados con evidencia:

- **Pacing pedagógico**: el bot esperaba la respuesta del estudiante antes de proponer temas (detectado durante testing: asumía currículo sin consultar)
- Manejo de preguntas sensibles
- Estrategia de code review (guiar al descubrimiento vs. corregir directamente)

> **Nota de diseño**: el patrón de tags XML para delimitar el prompt activo es una técnica recomendada por Anthropic en su guía de Prompt Engineering. Permite mantener documentación e iteraciones en el mismo archivo sin contaminar el contexto del modelo.

---

## ⚙️ Cómo ejecutar localmente

### Requisitos previos
- Python 3.10+
- Una API key de Google Gemini ([obtenerla aquí](https://aistudio.google.com/apikey))

### Pasos

```bash
# Clonar el repositorio
git clone https://github.com/Francorey12/profebot.git
cd profebot

# Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
# source venv/bin/activate     # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
# Crear archivo .env con:
# GEMINI_API_KEY=tu_api_key_aqui

# Ejecutar la app
streamlit run app.py
```

La app abrirá en `http://localhost:8501`.

---

## 🎓 Lo que aprendí construyendo esto

Este proyecto no fue solo "subir un chatbot a GitHub". Documentaré aquí los aprendizajes técnicos y pedagógicos para mostrar el proceso real:

### Prompt Engineering
- **Los adjetivos ambiguos son enemigos del prompt**. "Sé claro" no funciona; "frases cortas, máximo 150 palabras, una pregunta al final" sí.
- Los **few-shot examples** son la técnica más efectiva para anclar el comportamiento del modelo.
- Los **ejemplos contrastivos** (correcto vs. incorrecto) corrigen comportamientos no deseados mejor que las reglas negativas solas.
- Lo que es claro para un humano puede ser ambiguo para un modelo: hay que **escribir reglas explícitas y contables** ("primera vez", "siguientes 2 veces", "a partir de la cuarta").

### Diseño pedagógico aplicado a IA
- Los adolescentes detectan rápido el tono infantilizado. "Cercano y respetuoso" funciona mejor que "serio" o "amigable".
- La **agencia del estudiante** importa: el bot debe esperar dirección, no asumir currículo.
- El **pacing** (ritmo de introducción de conceptos) es crítico: introducir un tema sin que el estudiante lo pida reduce la motivación.

### Desafíos técnicos del mundo real
- **Deprecación de SDK**: descubrí que `google-generativeai` fue descontinuado durante el desarrollo. Migré a `google-genai` sin afectar la arquitectura.
- **Ciclo de vida en Streamlit**: aprendí a gestionar objetos persistentes (cliente HTTP, sesión de chat) con `st.session_state` para evitar errores de cliente cerrado entre reejecuciones.
- **Cuotas y rate limits**: enfrenté errores 429 que me obligaron a entender el sistema de cuotas de Google y diagnosticar problemas de la propia librería.

---

## 🔬 Testing y validación

El bot fue probado contra **6 categorías de escenarios** diseñadas para estresar el prompt:

1. **Baseline conversacional** — saludo y primer mensaje
2. **Concepto técnico** — explicación de variables, loops, funciones
3. **Frustración del estudiante** — "esto es muy difícil"
4. **Pregunta fuera de tema** — redirección amable
5. **Pregunta sensible** — manejo responsable
6. **Code review** — guiar al descubrimiento vs. corregir directamente

Los resultados del testing alimentan las iteraciones del prompt documentadas en `prompts/system_prompt.md`.

---

## 📌 Decisiones de diseño destacadas

| Decisión | Por qué |
|----------|---------|
| Prompt en archivo separado | Iteración rápida sin tocar código; documentación viva |
| Tags XML para delimitar | Mantener historial v1/v2/v3 en mismo archivo sin contaminar contexto |
| Estudiante elige lenguaje | Agencia pedagógica desde el primer mensaje |
| Patrón gradual del inglés | Refuerzo espaciado para memorización real |
| Manejo explícito de frustración | Adolescentes no dicen "no entiendo": dicen "esto es estúpido" |

---

## 🛣️ Próximos pasos

- [ ] Implementar v3 del prompt con base en testing
- [ ] Agregar evaluaciones automáticas (LLM-as-judge)
- [ ] Desplegar en Streamlit Community Cloud
- [ ] Agregar selector visible de modelo (Gemini 2.5 Flash vs. Pro)
- [ ] Capturar feedback del usuario en cada respuesta

---

## 👤 Autor

**Jean Franco Rey Ardila**
Estudiante de Ingeniería de Sistemas (3er semestre) — Bucaramanga, Colombia
Interesado en IA Generativa aplicada a educación tecnológica.

📫 jeanfrancoardilarey@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/jean-franco-rey-ardila-197b8a300)
💻 [GitHub](https://github.com/Francorey12)

---

## 📄 Licencia

MIT — Uso libre con atribución.