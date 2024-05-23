## Ejemplo para pregunta relacionada con DevOps
def get_question_answering_examples():
    return """
<ejemplo>
- Usuario: ¿Cómo puedo configurar un balanceador de carga en AWS usando ELB?
- Asistente: Para configurar un balanceador de carga en AWS usando Elastic Load Balancing (ELB), puedes seguir estos pasos:
1. Abre la consola de administración de AWS y navega hasta el servicio EC2.
2. En el panel de navegación izquierdo, selecciona "Load Balancers" y haz clic en "Create Load Balancer".
3. Elige el tipo de balanceador de carga que deseas crear: Application Load Balancer (ALB), Network Load Balancer (NLB) o Classic Load Balancer (CLB). Selecciona el tipo adecuado según tus requisitos.
4. Configura los ajustes básicos del balanceador de carga, como el nombre, el esquema (interno o orientado a Internet) y la red (VPC).
5. Configura los listeners para el balanceador de carga. Especifica los puertos y protocolos en los que el balanceador de carga escuchará el tráfico entrante.
6. Configura los target groups para el balanceador de carga. Define las instancias EC2, los contenedores o las funciones Lambda a las que el balanceador de carga distribuirá el tráfico.
7. Configura las health checks para monitorear la salud de los targets registrados. Especifica el protocolo, el puerto y la ruta para las health checks.
8. Configura cualquier ajuste adicional, como reglas de enrutamiento, sticky sessions o integración con AWS WAF (Web Application Firewall).
9. Revisa la configuración y crea el balanceador de carga.

Una vez creado, el balanceador de carga comenzará a distribuir el tráfico entrante entre los targets registrados según la configuración especificada. Puedes monitorear el rendimiento y la salud del balanceador de carga utilizando CloudWatch y realizar ajustes según sea necesario.

Recuerda que la configuración específica puede variar según el tipo de balanceador de carga y tus requisitos de aplicación. Consulta la documentación oficial de AWS para obtener instrucciones detalladas y mejores prácticas al configurar un balanceador de carga en ELB.
</ejemplo>
"""

## Ejemplo para solicitud de generación de script
def get_script_generation_examples():
    return """
<ejemplo>
- Usuario: Genera un script de Bash para hacer backup de una base de datos MySQL y subirlo a un bucket de S3.
- Asistente: Aquí te proporciono un script de Bash para hacer backup de una base de datos MySQL y subirlo a un bucket de S3:

#!/bin/bash

# Variables de configuración
DB_HOST="localhost"
DB_NAME="mydatabase"
DB_USER="myuser"
DB_PASSWORD="mypassword"
BACKUP_DIR="/path/to/backup/directory"
S3_BUCKET="my-s3-bucket"
S3_PATH="backups/"
DATE=$(date +%Y-%m-%d_%H-%M-%S)

# Crear directorio de backup si no existe
mkdir -p $BACKUP_DIR

# Generar nombre de archivo de backup
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$DATE.sql.gz"

# Realizar el backup de la base de datos MySQL
mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME | gzip > $BACKUP_FILE

# Subir el archivo de backup a S3
aws s3 cp $BACKUP_FILE s3://$S3_BUCKET/$S3_PATH

# Eliminar archivos de backup antiguos (opcional)
find $BACKUP_DIR -type f -name "$DB_NAME-*.sql.gz" -mtime +7 -delete

echo "Backup completado y subido a S3 exitosamente."

Asegúrate de reemplazar las variables de configuración con tus propios valores:
- DB_HOST: El host o la IP de tu servidor de base de datos MySQL.
- DB_NAME: El nombre de la base de datos que deseas respaldar.
- DB_USER: El usuario de MySQL con permisos para hacer el backup.
- DB_PASSWORD: La contraseña del usuario de MySQL.
- BACKUP_DIR: El directorio local donde se guardarán los backups.
- S3_BUCKET: El nombre de tu bucket de S3.
- S3_PATH: La ruta dentro del bucket de S3 donde se subirán los backups.

Antes de ejecutar el script, asegúrate de tener instalado y configurado el CLI de AWS con las credenciales adecuadas para acceder a tu bucket de S3.

El script realiza las siguientes acciones:
1. Crea el directorio de backup si no existe.
2. Genera un nombre de archivo único para el backup basado en la fecha y hora actual.
3. Utiliza mysqldump para hacer el backup de la base de datos MySQL y lo comprime con gzip.
4. Sube el archivo de backup al bucket de S3 especificado utilizando el comando aws s3 cp.
5. Opcionalmente, elimina los archivos de backup antiguos (mayores a 7 días) del directorio local.

Recuerda otorgar permisos de ejecución al script (chmod +x backup.sh) antes de ejecutarlo.

Espero que este script te sea útil para hacer backups de tu base de datos MySQL y subirlos a S3. Si tienes alguna otra pregunta, no dudes en preguntar.
</ejemplo>
"""


## Ejemplo para solución de problemas/errores
def get_error_troubleshooting_examples():
    return """
<ejemplo>
- Usuario: Estoy recibiendo un error "Connection refused" al intentar conectarme a un servidor remoto a través de SSH. ¿Cómo puedo solucionar este problema?
- Asistente: El error "Connection refused" al intentar conectarse a un servidor remoto a través de SSH puede tener varias causas. Aquí te presento algunos pasos para solucionar este problema:

1. Verifica que el servicio SSH esté en ejecución en el servidor remoto. Puedes usar el comando `sudo systemctl status ssh` para verificar el estado del servicio SSH.

2. Asegúrate de que el servidor remoto esté escuchando en el puerto SSH correctamente. Por defecto, el puerto SSH es el 22. Puedes verificar la configuración del puerto en el archivo `/etc/ssh/sshd_config` en el servidor remoto.

3. Comprueba que el firewall del servidor remoto permita conexiones entrantes en el puerto SSH. Utiliza comandos como `sudo ufw status` para verificar las reglas del firewall. Asegúrate de que el puerto SSH esté abierto para conexiones entrantes.

4. Verifica que estás utilizando la dirección IP o el nombre de host correctos para conectarte al servidor remoto. Asegúrate de que la dirección IP o el nombre de host sean accesibles desde tu máquina local.

5. Si estás conectándote a través de una red pública, verifica que tu proveedor de servicios de Internet (ISP) no esté bloqueando el puerto SSH. Algunos ISP pueden bloquear ciertos puertos por motivos de seguridad.

6. Intenta conectarte al servidor remoto utilizando la dirección IP en lugar del nombre de host, o viceversa, para descartar problemas de resolución de nombres de dominio (DNS).

7. Verifica que tu clave SSH sea válida y esté configurada correctamente en el servidor remoto. Asegúrate de que los permisos de los archivos de clave sean los adecuados (por ejemplo, `chmod 600 ~/.ssh/id_rsa`).

8. Si has realizado cambios recientes en la configuración de SSH en el servidor remoto, reinicia el servicio SSH ejecutando el comando `sudo systemctl restart ssh`.

9. Consulta los registros del sistema en el servidor remoto para obtener más información sobre el error. Puedes revisar los registros de SSH en `/var/log/auth.log` o `/var/log/secure` (dependiendo de la distribución de Linux) para buscar mensajes de error relacionados con SSH.

Si después de seguir estos pasos aún no puedes conectarte al servidor remoto, es posible que necesites investigar más a fondo la configuración de red y de seguridad tanto en el servidor remoto como en tu máquina local. También puede ser útil consultar la documentación oficial de SSH y buscar recursos adicionales en línea relacionados con la solución de problemas de conexión SSH.

Si el problema persiste, te recomiendo contactar al administrador del servidor o al equipo de soporte técnico correspondiente para obtener asistencia adicional.
</ejemplo>
"""

# few_shot_examples.py

def get_example_for_task(task_type):
    if task_type == "question_answering":
        return get_question_answering_examples()
    elif task_type == "script_generation":
        return get_script_generation_examples()
    elif task_type == "error_troubleshooting":
        return get_error_troubleshooting_examples()
    else:
        return ""