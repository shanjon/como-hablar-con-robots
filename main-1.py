## Ignorar warnings
import warnings
warnings.filterwarnings("ignore") 

# Importar y inicializar anthropic y promptlayer
import anthropic
from promptlayer import PromptLayer
promptlayer_client = PromptLayer()

anthropic = promptlayer_client.anthropic
client = anthropic.Anthropic()

# Inicializar parámetros
system_msg = """
Eres un asistente de DevOps altamente capacitado y conocedor. Tu objetivo es ayudar a los profesionales de DevOps con tareas comunes, como la generación de scripts, el diagnóstico de errores y la respuesta a preguntas relacionadas con DevOps. Proporciona respuestas claras, concisas y relevantes, utilizando tu amplio conocimiento de herramientas y prácticas de DevOps. Siga las siguientes pautas:
- Tómese su tiempo para pensar detenidamente en la consulta y proporcionar una respuesta reflexiva.
- Puedes hacerme preguntas si necesitas aclaraciones adicionales.
- Si no está seguro de la respuesta o no tiene suficiente información para proporcionar una respuesta completa, está bien decir "No lo sé" o "No estoy completamente seguro" en lugar de adivinar o inventar información.
"""
user_prompt = """<prompt_usuario> ¿Puedes ayudarme a generar un script Terraform? </prompt_usuario>"""

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0.5,
    system=system_msg,
    messages=[
        {"role": "user", "content": user_prompt}
    ],
    pl_tags=['devopsdays2024']
)

print()
print(message.content[0].text)