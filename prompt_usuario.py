prompt_usuario = """
<prompt_usuario>
    <task>Genera un script de Terraform que cree los siguientes recursos en AWS:</task>
        <resources>
            <ec2>
                <name>mi-instancia-web</name>
                <instance_type>t2.micro</instance_type>
                <ami>Utiliza la AMI más reciente de Amazon Linux 2</ami>
                <key_pair>mi-clave-ssh</key_pair>
                <security_group>
                    <name>mi-grupo-seguridad</name>
                    <inbound_rules>
                        <rule>
                            <port>80</port>
                            <protocol>TCP</protocol>
                            <description>HTTP</description>
                        </rule>
                        <rule>
                            <port>22</port>
                            <protocol>TCP</protocol>
                            <description>SSH</description>
                        </rule>
                    </inbound_rules>
                </security_group>
            </ec2>
            <rds>
                <name>mi-base-de-datos</name>
                <instance_type>db.t2.micro</instance_type>
                <engine>MySQL</engine>
                <engine_version>5.7</engine_version>
                <db_name>mi_base_de_datos</db_name>
                <username>admin</username>
                <password>Genera una contraseña aleatoria y guárdala en el archivo "db_password.txt"</password>
            </rds>
            <s3>
                <bucket_name>mi-bucket-terraform-<random_name></bucket_name>
                <versioning>true</versioning>
                <public_access>
                    <read>true</read>
                </public_access>
            </s3>
        </resources>
    <best_practices>
        <item>Utilizar las mejores prácticas de Terraform, como el uso de variables y la organización adecuada del código</item>
        <item>Agregar comentarios explicativos en el script para mejor comprensión</item>
        <item>Formatear correctamente el código utilizando el comando "terraform fmt"</item>
    </best_practices>
    <final_steps>
    Al final del script, incluye los comandos necesarios para:
    <step>Inicializar el directorio de trabajo de Terraform</step>
    <step>Aplicar los cambios</step>
    <step>Mostrar la salida de los recursos creados</step>
    </final_steps>
</prompt_usuario>
"""