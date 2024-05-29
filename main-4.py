## Ignorar warnings
import warnings
warnings.filterwarnings("ignore") 

# Importar y inicializar anthropic y promptlayer
import anthropic
from promptlayer import PromptLayer

# Importar las funciones de clasificar_tarea y ejemplos_fewshot, y el prompt usuario
from utils.clasificar_tarea import classify_task, get_task_specific_prompt
from utils.ejemplos_oneshot import get_example_for_task
from utils.prompt_usuario import prompt_usuario

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
user_prompt = prompt_usuario

# Classificar la tarea basada en el prompt del usuario
task_type = classify_task(user_prompt)

# Obtener el prompt específico de la tarea
task_specific_prompt = get_task_specific_prompt(task_type)

# Obtener un ejemplo relacionado a la tarea
task_example = get_example_for_task(task_type)

# Combinar el prompt del usuario, el prompt específico de la tarea, y ejemplo relacionado
complete_prompt = f"Clasificación de la tarea: {task_specific_prompt}\n\nEjemplo de prompt y respuesta: {task_example}\n\nUsuario: {user_prompt}"
print(complete_prompt)

# Payload
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0.5,
    system=system_msg,
    messages=[
        {"role": "user", "content": complete_prompt}
    ],
    pl_tags=['devopsdays2024']
)

# Imprimir la respuesta
print()
print("Asistente:",message.content[0].text)