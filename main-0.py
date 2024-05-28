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
system_msg = """Respond only in Yoda-speak"""
user_prompt = """Me puedes generar un script de Terraform"""

# Payload
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

# Imprimir la respuesta
print()
print(message.content[0].text)