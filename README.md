# Cómo hablar con robots

Este repo contiene un proyecto utilizado para demostrar técnicas y mejores prácticas para la ingeniería de prompts durante la conferencia [DevOpsDays Medellín 2024](https://devopsdays.io/).

El proyecto es un sencillo chatbot de DevOps que ayuda a los profesionales de DevOps con tareas comunes, como la generación de scripts, el diagnóstico de errores y la respuesta a preguntas relacionadas con DevOps.

The project is made up of a series of 5 prompts, each an incremental improvement upon the last by incorporating prompt engineering techniques discussed during the talk. In addition to the 5 prompts, there are three `utils` files that contain helper functions to classify tasks (`clasificar_tarea.py`), provide a relevant example according to the user prompt provided (`ejemplos_oneshot.py`), and a well-defined user prompt (`prompt_usuario.py`).

## Prerrequisitos

In order to execute the prompts, you will need to have:
- Python 3.7.1
- Anthropic API key
- PromptLayer API key - *PromptLayer is a free (for individuals) platform to track, manage, and share your prompt engineering (optional - see instructions below for using/removing)*

#### PythonV3
Before you begin, you must have Python3 (>= `3.7.1`) installed on your computer. Open your terminal (on macOS) or command prompt (on Windows) and type:
```
python --version
```

If you see a version number like `Python 3.12.2`, you’re all set. If not, visit the [official Python website and download the latest version](https://www.python.org/downloads/).

#### Anthropic Claude
You will need an Anthropic Claude API key. You can generate one for free - and get $5 in free credits (more than enough to run these scripts) - by accessing the instructions here.

Once you have the API key generated, you will run:

[instructions for Windows]

[instructions for Mac]

Full instructions here: https://docs.anthropic.com/es/docs/getting-access-to-claude


#### PromptLayer
PromptLayer records your OpenAI and Anthropic API requests, allowing you to search and explore request history in the PromptLayer dashboard.

In order to use PromptLayer as part of this project, you will need to sign up for an account and generate an API key

Once you have the API key generated, you will run:
[instructions for Windows]

[instructions for Mac] 

Full instructions here: https://docs.promptlayer.com/languages/python#anthropic

If you do NOT want to use PromptLayer, you can remove the following lines from `main-0.py`, `main-1.py`, `main-2.py`, `main-3.py`, `main-4.py`

[LINES TO BE REMOVED]

## Parameters to be modified
The parameters we modify in this project are `system` and `messages.content`:
- `system` refers to the system prompt, etc.
- `messages.content` refers to the prompt sent to the LLM that contains the user’s prompt, as well as additional context provided to aid in contextualizing the prompt

To make this demo easier to follow and update, I set the values for the `system` and `message.content` parameters to variables `system_msg` and `user_prompt`, respectively, and defined them above (outside of the API call).

If you want, you can also change the parameters `model`, `temperature`, and `max_tokens`, but this is outside the scope of this project.

## main-0.py
`main-0.py` is the  that is made to the API endpoint. It includes the default 
https://docs.anthropic.com/es/docs/quickstart-guide