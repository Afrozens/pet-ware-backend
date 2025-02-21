import subprocess

def handler(event, context):
    try:
        # Ejecutar el archivo startup.sh
        subprocess.run(["/bin/bash", "/var/task/startup.sh"])
    except Exception as e:
        print(f"Error al ejecutar startup.sh: {e}")
        raise e