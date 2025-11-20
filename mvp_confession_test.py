import os
import json
import unicodedata
import re
import google.generativeai as genai

# 1) Setup your API key safely via environment variable:
#    Example in terminal (Mac/Linux):
#       export GEMINI_API_KEY="your_api_key_here"
#    Then run:
#       python mvp_confession_test.py
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2) Configuration
MODEL_NAME = "gemini-2.5-flash"
TEST_FILE = "lopez_gomez.txt"

def normalize(text):
    """Lowercase and remove accent marks."""
    text = text.lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return text

def classify_text(text):
    """Send a single text to Gemini and get JSON classification, focused on sexual violence."""
    prompt = f"""
Tarea: Lee el siguiente fragmento en español y clasifícalo ÚNICAMENTE en relación con violencia sexual o abuso sexual.
Evalúa si el texto describe una confesión, admisión, o referencia directa a actos sexuales forzados cometidos durante el conflicto armado.

Categorías:
A) Confesión directa de violencia sexual o violación – el compareciente o perpetrador admite explícitamente haber cometido violación, abuso sexual, acceso carnal violento u otro acto sexual forzado.
B) Admisión procesal o aceptación de cargos por violencia sexual – se reconoce haber sido acusado o haberse declarado culpable de un delito sexual, pero sin narrar los hechos.
C) Lenguaje judicial o de sentencia sobre delitos sexuales – texto institucional, resoluciones o decisiones judiciales que informan condenas, autos o sentencias sobre violencia sexual (no palabras del perpetrador).
D) Testimonio o denuncia de terceros – la víctima, testigos o terceros describen un hecho de violencia sexual, pero no es una confesión del perpetrador.
E) No relacionado / ambiguo – el fragmento no contiene información sobre violencia sexual o es demasiado vago para clasificar.

Devuelve una sola línea de JSON en este formato:
{{"label": "<A|B|C|D|E>", "quote": "<cita mínima del texto que apoya la clasificación>", "confidence": <0..1>, "rationale": "<explica brevemente por qué>"}}

Texto a analizar:
<<<
{text}
>>>
"""
    import re, json
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    try:
        text_out = response.text.strip()
        text_out = re.sub(r"^```(?:json)?", "", text_out).strip()
        text_out = re.sub(r"```$", "", text_out).strip()
        result = json.loads(text_out)
    except Exception as e:
        print("Could not parse JSON, showing raw output:\n", response.text)
        result = {
            "label": "E",
            "quote": "",
            "confidence": 0.0,
            "rationale": f"error parsing output: {e}"
        }
    return result



def main():
    # Load your test file
    if not os.path.exists(TEST_FILE):
        print(f"Test file not found: {TEST_FILE}")
        return

    with open(TEST_FILE, encoding="utf-8") as f:
        text = f.read()

    print(f"Analyzing {TEST_FILE} ({len(text)} characters)...")
    result = classify_text(text)

    print("\nModel classification result:\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
