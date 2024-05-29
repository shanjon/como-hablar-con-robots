# Cómo hablar con robots

Este repo contiene un proyecto utilizado para demostrar técnicas y mejores prácticas para la ingeniería de prompts durante la conferencia [DevOpsDays Medellín 2024](https://devopsdays.io/).

El proyecto es un sencillo chatbot de DevOps que ayuda a los profesionales de DevOps con tareas comunes, como la generación de scripts, el diagnóstico de errores y la respuesta a preguntas relacionadas con DevOps.

El proyecto se compone de una serie de 5 prompts, cada uno mejorando incrementalmente al anterior mediante la incorporación de técnicas de ingeniería de prompts discutidas durante la charla. Además de los 5 prompts, hay tres archivos `utils` que contienen funciones auxiliares para clasificar tareas (`clasificar_tarea.py`), proporcionar un ejemplo relevante de acuerdo con el prompt del usuario (`ejemplos_oneshot.py`), y un prompt de usuario bien definido (`prompt_usuario.py`).

## Prerrequisitos

Para ejecutar los prompts, se requieren:
- Python 3.7.1
- Una clave API de Anthropic
- Una clave API de PromptLayer - *PromptLayer es una plataforma gratuita (para individuos) para rastrear, administrar y compartir la ingeniería de prompts (opcional - consulta las instrucciones a continuación para usar/eliminar)*

#### PythonV3 and Anthropic API key
La guía de inicio rápido publicado por Anthropic indica los pasos necesarios para instalar PythonV3 y configurar tu entorno con una clave API de Anthropic. Se puede generar una clave gratis - y recibir $5 en créditos (más que suficiente para este proyecto) - al acceder las instrucciones en español aqui: https://docs.anthropic.com/es/docs/getting-access-to-claude

#### PromptLayer

PromptLayer registra tus solicitudes a los APIs de OpenAI y Anthropic, lo que te permite buscar y explorar el historial de solicitudes en el tablero de PromptLayer.

Para utilizar PromptLayer en este proyecto, hay que registarte en el sitio web y generar una clave API. Después de generar tu clave API, se puede configurarla de [la misma forma que la clave de Anthropic](https://docs.anthropic.com/es/docs/quickstart-guide#paso-3-opcional-configura-tu-clave-de-api).

En macOS o Linux:
- Abre tu terminal y escribe: nano ~/.bash_profile (o nano ~/.zshrc si estás usando una versión más reciente de macOS)
- Agrega esta línea al archivo, reemplazando your-api-key-here con tu clave de API real: export PROMPTLAYER_API_KEY='your-api-key-here'
- Guarda el archivo y sal del editor (presiona Ctrl+O, luego Enter, luego Ctrl+X)
- Carga el perfil actualizado ejecutando: source ~/.bash_profile (o source ~/.zshrc)

En Windows:
- Abre el símbolo del sistema y escribe: setx PROMPTLAYER_API_KEY= "your-api-key-here", reemplazando your-api-key-here con tu clave de API real
- Para hacer este cambio permanente, sigue estos pasos:
- Haz clic derecho en ‘Este equipo’ o ‘Mi PC’ y selecciona ‘Propiedades’
- Haz clic en ‘Configuración avanzada del sistema’
- Haz clic en el botón ‘Variables de entorno’
- En la sección ‘Variables del sistema’, haz clic en ‘Nuevo…’ e ingresa PROMPTLAYER_API_KEY= como el nombre de la variable y tu clave de API como el valor de la variable

Si NO deseas utilizar PromptLayer, borra las siguientes líneas de los archivos `main-0.py`, `main-1.py`, `main-2.py`, `main-3.py`, `main-4.py`:
```
from promptlayer import PromptLayer
promptlayer_client = PromptLayer()
```
```
anthropic = promptlayer_client.anthropic
```
```
pl_tags=['devopsdays2024']
```

## Parámetros a modificar
Los parámetros de la solicitud a la API de Anthropic que modificamos en este proyecto incluyen `system` y `messages.content`
The parameters we modify in this project are `system` and `messages.content`:
- `system`: Se utiliza para establecer el mensaje del sistema que proporciona instrucciones o contexto al modelo de lenguaje. Este mensaje se procesa antes de los mensajes del usuario y ayuda a guiar el comportamiento y las respuestas del modelo.
- `messages.content`: Aquí se coloca todo el texto que deseas que el modelo procese y responda. Puedes estructurar el contenido de manera que incluya la clasificación de la consulta, ejemplos relevantes o cualquier otra información que ayude al modelo a entender mejor el contexto y generar una respuesta más precisa.

> [!WARNING]
> Para hacer esta demostración más fácil de seguir y actualizar, inicialicé los valores de los parámetros `system` y `content` en las variables `system_msg` y `user_prompt`, respectivamente, y las definí anteriormente (fuera de la llamada a la API).

Si lo deseas, también puedes cambiar los parámetros `model`, `temperature` y `max_tokens`, pero esto está fuera del alcance de este proyecto.

*Si estás utilizando PromptLayer, también se puede modificar el valor de la etiqueta `pl_tags` a cualquier valor que deseas.*

## Ejecutar los scripts
Para ejecutar los scripts:
1. Abre el proyecto en tu IDE
2. Asegúrate de estar en el directorio del proyecto `como-hablar-con-robots` o muévete a ese directorio ejecutando el comando `cd como-hablar-con-robots`
3. Ejecuta el script con el comando `python3 main-X.py` o ejecutando el depurador de Python en tu IDE - *reemplaza `x` con el número del script que desea ejecutar*

### main-0.py
`main-0.py` es el primer prompt que enviamos a la API de Anthropic. Se incluye el payload por defecto de [la guía de inicio rápido de Anthropic](https://docs.anthropic.com/es/docs/quickstart-guide#paso-4-envia-tu-primera-solicitud-de-api). El único cambio que se ha hecho al payload por defecto es cambiar el valor del parámetro `user_prompt` de "How are you today?" a "¿Puedes ayudarme a generar un script Terraform?".

> [!TIP]
> Ejecuta el script `main-0.py` con `python3 main-0.py` o con el debugger Python del IDE

Como se ve al ejecutar el script, la respuesta está en inglés, y el LLM no tuvo el contexto para responder adecuadamente al prompt. Sólo nos confirma que puede ayudar con el script, pero no nos da información para realizar la tarea.

### main-1.py
En `main-1.py`, actualizamos los parámetros `system_msg` y `user_prompt` de la siguiente manera:
- `system_msg`
    - Juego de papel
    - Clara
    - Tiempo a pensar y la opción de decir “no lo sé”
- `user_prompt`
    - Estructurado - XML tags

