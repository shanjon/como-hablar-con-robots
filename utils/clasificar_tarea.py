import re

# Buscar palabras claves para clasificar la tarea
def classify_task(query):
    question_keywords = ["cómo", "qué", "por qué", "cuándo", "dónde", "explica", "describe"]
    script_keywords = ["generar un script", "crear un script", "escribir un script", "script para"]
    error_keywords = ["error", "problema", "solucionar", "arreglar", "depurar"]

    if any(keyword in query.lower() for keyword in question_keywords):
        return "question_answering"
    elif any(keyword in query.lower() for keyword in script_keywords):
        return "script_generation"
    elif any(keyword in query.lower() for keyword in error_keywords):
        return "error_troubleshooting"
    else:
        return "general"

# Clasificar la tarea como "question_answering", "script_generation", o "error_troubleshooting"
def get_task_specific_prompt(task_type):
    if task_type == "question_answering":
        return "<clasificación> Pregunta relacionada con DevOps </clasificación>"
    elif task_type == "script_generation":
        return "<clasificación> Solicitud de generación de script </clasificación>"
    elif task_type == "error_troubleshooting":
        return "<clasificación> Solución de problemas/errores </clasificación>"
    else:
        return ""