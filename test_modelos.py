print("PASO 1: Script iniciado")

try:
    from google import genai
    print("PASO 2: Import de google.genai exitoso")
except Exception as e:
    print(f"ERROR EN IMPORT: {e}")
    exit()

try:
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"PASO 3: API key cargada (primeros 10 chars: {api_key[:10]}...)")
except Exception as e:
    print(f"ERROR EN .ENV: {e}")
    exit()

try:
    client = genai.Client(api_key=api_key)
    print("PASO 4: Cliente creado exitosamente")
except Exception as e:
    print(f"ERROR AL CREAR CLIENTE: {e}")
    exit()

print("PASO 5: Intentando listar modelos...")
print("=" * 60)

try:
    modelos = list(client.models.list())
    print(f"Cantidad de modelos encontrados: {len(modelos)}")
    print("=" * 60)
    for m in modelos:
        print(f"✅ {m.name}")
except Exception as e:
    print(f"ERROR AL LISTAR MODELOS:")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Mensaje: {e}")

print("\nFIN DEL SCRIPT")