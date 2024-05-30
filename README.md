# Cómo hablar con robots :robot:

Este repo contiene un proyecto utilizado para demostrar técnicas y mejores prácticas para la ingeniería de prompts durante la conferencia [DevOpsDays Medellín 2024](https://devopsdays.io/) :colombia:

El proyecto es un sencillo chatbot de DevOps que ayuda a los profesionales de DevOps con tareas comunes, como la generación de scripts, el diagnóstico de errores y la respuesta a preguntas relacionadas con DevOps.

El proyecto se compone de una serie de 5 prompts, cada uno mejorando incrementalmente al anterior mediante la incorporación de técnicas de ingeniería de prompts discutidas durante la charla. Además de los 5 prompts, hay tres archivos `utils` que contienen funciones auxiliares para clasificar tareas (`clasificar_tarea.py`), proporcionar un ejemplo relevante de acuerdo con el prompt del usuario (`ejemplos_oneshot.py`), y un prompt de usuario bien definido (`prompt_usuario.py`).

## Prerrequisitos :page_facing_up:

Para ejecutar los prompts, se requieren:
- Python 3.7.1
- Una clave API de Anthropic (Claude)
- Una clave API de PromptLayer - *PromptLayer es una plataforma gratuita (para individuos) para rastrear, administrar y compartir la ingeniería de prompts (opcional - consulta las instrucciones a continuación para usar/eliminar)*

### Python 3 and Anthropic API key
La guía de inicio rápido publicado por Anthropic indica los pasos necesarios para instalar Python 3 y configurar tu entorno con una clave API de Anthropic. Se puede generar una clave gratis - y recibir $5 en créditos (más que suficiente para este proyecto) - al seguir las instrucciones en español aqui: https://docs.anthropic.com/es/docs/getting-access-to-claude

### PromptLayer

PromptLayer registra tus solicitudes a los APIs de OpenAI y Anthropic, lo que te permite buscar y explorar el historial de solicitudes en el tablero de PromptLayer.

Para utilizar PromptLayer en este proyecto, hay que registarte en el sitio web y generar una clave API. Después de generar tu clave API, se puede configurarla de [la misma forma que la clave de Anthropic](https://docs.anthropic.com/es/docs/quickstart-guide#paso-3-opcional-configura-tu-clave-de-api).

**En macOS o Linux**:
- Abre tu terminal y escribe: `nano ~/.bash_profile` (o `nano ~/.zshrc` si estás usando una versión más reciente de macOS)
- Agrega esta línea al archivo, reemplazando `your-api-key-here` con tu clave de API: `export PROMPTLAYER_API_KEY='your-api-key-here'`
- Guarda el archivo y sal del editor (presiona Ctrl+O, luego Enter, luego Ctrl+X)
- Carga el perfil actualizado ejecutando: `source ~/.bash_profile` (o `source ~/.zshrc`)

**En Windows**:
- Abre el símbolo del sistema y escribe: `setx PROMPTLAYER_API_KEY= "your-api-key-here"`, reemplazando your-api-key-here con tu clave de API real
- Para hacer este cambio permanente, sigue estos pasos:
- Haz clic derecho en ‘Este equipo’ o ‘Mi PC’ y selecciona ‘Propiedades’
- Haz clic en ‘Configuración avanzada del sistema’
- Haz clic en el botón ‘Variables de entorno’
- En la sección ‘Variables del sistema’, haz clic en ‘Nuevo…’ e ingresa `PROMPTLAYER_API_KEY=` como el nombre de la variable y tu clave de API como el valor de la variable

> [!CAUTION]
> Si NO deseas utilizar PromptLayer, borra las siguientes líneas de los archivos `main-0.py`, `main-1.py`, `main-2.py`, `main-3.py`, `main-4.py`:
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

## ¡Comenzamos! :rocket:
Ahora podemos comenzar a ejecutar los scripts y ver cómo la aplicación de técnicas de ingeniería mejora la calidad de los resultados. Implementaremos estas técnicas con 2 parámetros de la API de Anthropic.

Los parámetros son `system` y `messages.content`:
- `system`: Se utiliza para establecer el mensaje del sistema que proporciona instrucciones o contexto al modelo de lenguaje. Este mensaje se procesa antes de los mensajes del usuario y ayuda a guiar el comportamiento y las respuestas del modelo.
- `messages.content`: Aquí se coloca todo el texto que deseas que el modelo procese y responda. Además del prompt de usuario, puedes estructurar el contenido de manera que incluya la clasificación de la consulta, ejemplos relevantes o cualquier otra información que ayude al modelo a entender mejor el contexto y generar una respuesta más precisa.

> [!WARNING]
> **Para hacer esta demostración más fácil de seguir y actualizar, inicialicé los valores de los parámetros `system` y `content` en las variables `system_msg` y `user_prompt`, respectivamente, y las definí anteriormente (fuera de la llamada a la API).**

Si lo deseas, también puedes cambiar los parámetros `model`, `temperature` y `max_tokens`, pero esto está fuera del alcance de este proyecto.

Si estás utilizando PromptLayer, también se puede modificar el valor de la etiqueta `pl_tags` a cualquier valor que deseas.

## Ejecutar los scripts :keyboard:
Para ejecutar los scripts:
1. Abre el proyecto en tu IDE
2. Asegúrate de estar en el directorio del proyecto `como-hablar-con-robots` o muévete a ese directorio ejecutando el comando `cd como-hablar-con-robots`
3. Ejecuta el script con el comando `python3 main-X.py` o ejecutando el debugger de Python en tu IDE - *reemplaza `X` con el número del script que desea ejecutar*

### main-0.py
`main-0.py` es el primer prompt que enviamos a la API de Anthropic. Se incluye el payload por defecto de [la guía de inicio rápido de Anthropic](https://docs.anthropic.com/es/docs/quickstart-guide#paso-4-envia-tu-primera-solicitud-de-api). El único cambio que se ha hecho al payload por defecto es cambiar el valor del parámetro `user_prompt` de "How are you today?" a "¿Puedes ayudarme a generar un script Terraform?".

:woman_technologist: :exclamation: **Ejecuta el script `main-0.py` con `python3 main-0.py` o con el debugger Python del IDE** :exclamation: :woman_technologist:

Al ejecutar el script, se nota que el LLM apenas nos confirma que, sí, está capaz de ayudar con scripts, pero no lo genera ni nos hace preguntas para recopilar los requisitos del script. Además la respuesta está en inglés. Claramente, el LLM no tuvo el contexto adecuado para para avanzar con el desarrollo del script. Avanzamos...

### main-1.py
En `main-1.py`, actualizamos los parámetros `system_msg` y `user_prompt` de la siguiente manera:
- `system_msg`
    - Aprovechar de la técnica "Juego de papel" al indicar al LLM *"Eres un asistente de DevOps..."*
    - Dejar el prompt de sistema más claro al incluir la audiencia prevista, el objetivo, y el estilo/tono de las respuestas deseadas
    - Darle al LLM tiempo a pensar y la opción de decir “no lo sé”
- `user_prompt`
    - Estructuar el prompt del usuario al ponerlo en etiquetas XML

:woman_technologist: :exclamation: **Ejecuta el script `main-1.py` con `python3 main-1.py` o con el debugger Python del IDE** :exclamation: :woman_technologist:

Al ejecutar el script, ya se nota mejoras en la respuesta. Esta vez, confirma (en español) que, sí, está capaz de ayudar con la generación de un script de Terraform, incluye detalles de Terraform para demostrar su familiaridad con la tecnologia, y nos hace preguntas para poder completar la tarea...

Sin embargo, debemos ayudamos a Claude a entender y realizar la tarea, ya que debe estar capaz de generar scripts, diagnosticar errores/problemas, y responder a preguntas relacionadas con DevOps.

### main-2.py
Esta vez, implementamos un poco de lógica en el script para clasificar la tarea solicitada por el usuario. Agregamos un helper function ([`clasificar_tarea.py`](/utils/clasificar_tarea.py)) para evaluar el prompt del usuario y clasificarla como "Pregunta relacionada con DevOps", "Solicitud de generación de script" o "Solución de problemas/errores", y después pasar todo junto al modelo.

En `main-2.py`, juntamos la clasificación de la tarea con el prompt del usuario, ambos estructurados en etiquetas XML, y se los pasamos al payload en la variable `complete_prompt`. Ahora, el modelo va a recibir la siguiente información:

```
Clasificación de la tarea: <clasificación> Solicitud de generación de script </clasificación>

Usuario: <prompt_usuario> ¿Puedes ayudarme a generar un script Terraform? </prompt_usuario>
```

:woman_technologist: :exclamation: **Ejecuta el script `main-2.py` con `python3 main-2.py` o con el debugger Python del IDE** :exclamation: :woman_technologist:

Con la clasificación de tareas, estamos haciendo que nuestra arquitectura rápida sea más modular, de modo que podamos beneficiarnos de la reutilización, la mantenibilidad, la extensibilidad y la personalización...

### main-3.py
Ahora, implementamos la técnica "One-shot prompting" a nuestro chatbot. Depués de clasificar la tarea indicado por el prompt del usuario, pasamos un ejemplo de una consulta parecida y una respuesta adecuada. Los ejemplos aclaran el nivel de detalle y también que queremos que la repuesta sea estructurada en subtareas, paso-por-paso. Al incluir un ejemplo relevante, se aumenta la probabilidad de que Claude genere una respuesta que cumpla con nuestras expectativas.

El helper function [`ejemplos_oneshot.py`](/utils/ejemplos_oneshot.py) incluye un ejemplo de cada tipo de tarea que el modelo tendrá que manejar ("Pregunta relacionada con DevOps", "Solicitud de generación de script", y "Solución de problemas/errores"). Depués de clasificar la tarea, el script agrega el ejemplo correspondiente a la clasificación, y pasa todo junto con el prompt de usuario en `complete_prompt`:

```
Clasificación de la tarea: <clasificación> Solicitud de generación de script </clasificación>

Ejemplo de prompt y respuesta: 
<ejemplo>
...

</ejemplo>

Usuario: <prompt_usuario> ¿Puedes ayudarme a generar un script Terraform? </prompt_usuario>

```

:woman_technologist: :exclamation: **Ejecuta el script `main-3.py` con `python3 main-3.py` o con el debugger Python del IDE** :exclamation: :woman_technologist:

Ahora se nota que la respuesta ha mejorado bastante desde `main-0.py`. Sin embargo, nuestro prompt de usuario es demasiado vago! Vamos a aplicar nuestras técnicas de la ingeniería de prompt...

### main-4.py
En [`prompt_usuario.py`](/utils/prompt_usuario.py), hay un prompt de usuario que - con todas las etiquetas del mundo - explica la tarea, todos los detalles necesarios para realizar la tarea, y instrucciones al final para incluir el paso-a-paso. Le pasamos este prompt al parámetero `user_prompt`.

Junto con el juego de papel, claridad, estructura, one-shot prompting, y otras mejores práticas que hemos implementado, deberíamos poder generar una respuesta bien refinada...

:woman_technologist: :exclamation: **Ejecuta el script `main-4.py` con `python3 main-4.py` o con el debugger Python del IDE** :exclamation: :woman_technologist:

Esta vez, vemos que el modelo nos proporciona un script funcional, repleto de las configuraciones indicadas por el prompt del usuario, y explicado en detalle, paso-por-paso. Hasta indica pasos de troubleshooting!
> Nota: Es posible que tengas que incrementar el parámetro max_tokens para generar la respuesta completa de Anthropic.

> [!TIP]
> **Cambia el mensaje del usuario a otra tarea y vea cómo responde el modelo!**


## Comentarios finales :thought_balloon:
Gracias por leer y probar este repo. Espero que te haya ayudado. Si tienes algún pregunta o duda relacionada al proyecto, no dudas [reportar un Issue](https://github.com/shanjon/como-hablar-con-robots/issues).