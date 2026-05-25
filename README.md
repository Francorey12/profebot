# 🤖 ProfeBot — Tutor de Programación para Adolescentes

> Asistente conversacional impulsado por IA generativa, diseñado pedagógicamente para enseñar programación a estudiantes de 14 a 16 años.

**Proyecto de portafolio** para el rol de **AI Trainer**.
Construido con foco en **Prompt Engineering iterativo**, **diseño de experiencia conversacional** y **buenas prácticas de desarrollo con LLMs**.

---

## 🎯 ¿Qué es ProfeBot?

ProfeBot es un tutor virtual de programación cuyo system prompt fue diseñado y refinado iterativamente —tres versiones, evidencia real— para enseñar a adolescentes. No es un chatbot genérico: cada decisión de comportamiento (tono, formato, manejo de términos en inglés, respuesta a frustración, code review) está **documentada y justificada** en el repositorio.

El valor del proyecto **no está solo en el código**, sino en demostrar el proceso de pensamiento de un AI Trainer: cómo se diseña, se prueba con metodología, y se itera un prompt usando evidencia real de testing.

---

## 🚀 Stack Técnico

| Capa | Tecnología |
|------|-----------|
| Lenguaje | Python 3.14 |
| Framework UI | Streamlit |
| Modelo LLM | Google Gemini 2.5 Flash |
| SDK | `google-genai` (SDK actual de Google) |
| Variables de entorno | `python-dotenv` |
| Control de versiones | Git + GitHub (workflow con Pull Requests) |

---

## 📁 Estructura del Proyecto

```
profebot/
├── prompts/
│   ├── system_prompt.md       # Iteraciones del prompt (v1 → v2 → v3)
│   └── testing_v2.md          # Log sistemático del testing de v2
├── dev/
│   └── test_modelos.py        # Script auxiliar para listar modelos disponibles
├── venv/                      # Entorno virtual (no se sube)
├── app.py                     # Aplicación principal
├── .env                       # Variables sensibles (no se sube)
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
- Patrón estandarizado para términos en inglés (refuerzo gradual de 4 estados)
- Reglas explícitas de formato, tono y longitud
- Manejo específico de frustración adolescente
- Redirección amable de temas fuera de programación
- **Few-shot examples** contrastivos
- Estudiante elige el lenguaje al inicio (agencia pedagógica)
- Delimitado con tags `<prompt_activo>` para separar contenido activo de documentación

### Versión 3 (v3) — Iteración basada en testing sistemático
Construida tras testear v2 con metodología documentada en `prompts/testing_v2.md`. Cambios derivados de **4 patrones transversales** identificados durante testing, no de intuiciones:

| Patrón detectado | Cambio en v3 |
|---|---|
| El bot llena silencios en vez de devolver agencia | Nueva sección "Segundo turno y respuestas mínimas" + few-shot contrastivo |
| Resuelve bugs antes de guiar al descubrimiento | Nueva sección "Code review" distinguiendo sintaxis (corregir) vs. lógica (guiar) |
| Tono se desliza a infantil bajo presión | Sección extendida "Contra la infantilización" con diminutivos y analogías a evitar |
| Patrón de inglés (4 estados) se rompe en uso real | Simplificación a 2 estados: primera mención con traducción, siguientes solo en inglés |

Además, se detectó por revisión interna que un few-shot de v2 contradecía su propia regla (cerraba con pregunta cerrada cuando la regla exigía pregunta abierta). Fue corregido en v3.

> **Nota de diseño**: el patrón de tags `<prompt_activo>` para delimitar el prompt activo es una técnica recomendada por Anthropic en su guía de Prompt Engineering. Permite mantener documentación e iteraciones en el mismo archivo sin contaminar el contexto del modelo.

---

## 🔬 Testing sistemático

Antes de iterar a v3, probé v2 contra **10 categorías diseñadas para estresar el prompt**, completando 5 antes de alcanzar el límite diario del free tier de Gemini. Decisión tomada: parar el testing ahí porque los hallazgos ya justificaban una iteración mayor, en lugar de cambiar de modelo (lo cual contaminaría resultados) o gastar 24h esperando reset.

### Categorías testeadas
1. Pacing pedagógico (segundo turno tras elección de lenguaje)
2. Tono de saludo
3. Preguntas sensibles (hackeo, cyberbullying, bots de likes)
4. Code review (bugs de sintaxis vs. bugs lógicos)
5. Frustración real (frases crudas, rendición, desinterés)

### Categorías pendientes (deuda técnica documentada para v4)
6. Patrón de inglés en conversación larga (15+ turnos)
7. Redirección de temas fuera de programación
8. Consistencia de preguntas abiertas al cerrar
9. Longitud en temas complejos (recursión, async)
10. Consistencia con lenguajes no-Python

Cada hallazgo del testing está documentado con input literal, output del bot, diagnóstico y prioridad (🔴/🟡/🟢). Ver `prompts/testing_v2.md`.

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

### Prompt Engineering
- **Los adjetivos ambiguos son enemigos del prompt**. "Sé claro" no funciona; "frases cortas, máximo 150 palabras, una pregunta abierta al final" sí.
- Los **few-shot examples** son la técnica más efectiva para anclar comportamiento.
- Los **ejemplos contrastivos** (correcto vs. incorrecto) corrigen comportamientos mejor que las reglas negativas solas.
- Los few-shots pueden contradecir las reglas escritas, y cuando eso pasa **el modelo imita el ejemplo, no la regla**. Detecté esto en v2 y lo corregí en v3.
- Reglas complejas de varios estados (ej: contar la 1ª/2ª/3ª/4ª mención de un término) son frágiles. Simplificar a 2 estados produce resultados más consistentes en conversaciones largas.

### Testing de prompts
- El testing exhaustivo no siempre es el más útil. Pasado cierto umbral, cada test adicional aporta menos información que iterar el prompt y probar la nueva versión.
- Agrupar hallazgos por **causa raíz** (no por síntoma) es lo que produce iteraciones limpias. Cinco síntomas pueden ser un solo problema de fondo.
- Documentar testing en formato estructurado (categoría, input, output, diagnóstico, prioridad) hace que un mes después puedas volver al proyecto sin perder contexto.

### Diseño pedagógico aplicado a IA
- Los adolescentes detectan rápido el tono infantilizado. "Cercano y respetuoso" funciona; analogías de caramelos y juguetes no.
- La **agencia del estudiante** importa: el bot debe esperar dirección, no asumir currículo.
- El **pacing** (ritmo de introducción de conceptos) es crítico: introducir un tema sin que el estudiante lo pida reduce la motivación.
- Respuestas mínimas del estudiante ("ok", "ajá") no son señal de seguir empujando contenido — son señal de chequear comprensión.

### Desafíos técnicos del mundo real
- **Deprecación de SDK**: descubrí que `google-generativeai` fue descontinuado durante el desarrollo. Migré a `google-genai` sin afectar la arquitectura.
- **Ciclo de vida en Streamlit**: aprendí a gestionar objetos persistentes (cliente HTTP, sesión de chat) con `st.session_state` para evitar errores de cliente cerrado entre reejecuciones.
- **Cuotas y rate limits**: enfrenté errores 429 que me obligaron a entender el sistema de cuotas de Google y a tomar decisiones de gestión del tiempo bajo restricción real.

---

## 📌 Decisiones de diseño destacadas

| Decisión | Por qué |
|----------|---------|
| Prompt en archivo separado | Iteración rápida sin tocar código; documentación viva |
| Tags `<prompt_activo>` | Mantener historial v1/v2/v3 en mismo archivo sin contaminar contexto |
| Estudiante elige lenguaje | Agencia pedagógica desde el primer mensaje |
| Patrón gradual del inglés (v3: 2 estados) | Refuerzo sostenible sin lógica frágil de conteo |
| Manejo explícito de frustración | Adolescentes no dicen "no entiendo": dicen "esto es estúpido" |
| Code review diferenciado | Bugs de sintaxis: corregir; bugs lógicos: guiar |
| Workflow Git con Pull Requests | Historial trazable de qué cambió y por qué |

---

## 🛣️ Próximos pasos

- [ ] Testear v3 con 5 casos dirigidos para validar que los 4 patrones quedaron resueltos
- [ ] Completar categorías de testing pendientes (6-10) en una eventual v4
- [ ] Agregar evaluaciones automáticas (LLM-as-judge)
- [ ] Desplegar en Streamlit Community Cloud
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