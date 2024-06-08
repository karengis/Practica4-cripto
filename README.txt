
## Práctica 4: Desarrollo de un Keylogger Remoto

### Descripción
Esta práctica consiste en el desarrollo de un software malicioso conocido como keylogger, el cual registra las pulsaciones de teclas realizadas en un sistema y envía la información recopilada por correo electrónico. El keylogger también cuenta con la capacidad de guardar un registro local en un archivo de texto plano.

### Versiones de los elementos utilizados
- Python: 3.9.7
- Pynput: 1.7.3
- Smtplib (módulo incluido en la biblioteca estándar de Python)
- Email (módulo incluido en la biblioteca estándar de Python)

### Método de ejecución de la práctica
1. Asegúrate de tener Python instalado en tu sistema.
2. Instala la biblioteca Pynput ejecutando el siguiente comando en tu terminal:
sudo pip install pynput

3. Guarda el script de Python (`keylogger.py`) en tu directorio de trabajo.
4. Abre una terminal y navega hasta el directorio que contiene el script de Python.
5. Ejecuta el script de Python con el siguiente comando:
sudo python practica.py

6. Sigue las instrucciones que aparecen en la terminal para configurar si deseas enviar los registros por correo electrónico, guardarlos en un archivo de texto plano .

### Ejecución del script de borrado (`cleanup.sh`)
1. Abre una terminal y navega hasta el directorio que contiene el script de borrado (`borrar_practica.sh`).
2. Otorga permisos de ejecución al script con el siguiente comando:
chmod +x cleanup.sh

3. Ejecuta el script de borrado con el siguiente comando:
./cleanup.sh

Asegúrate de estar en un directorio donde sea seguro borrar los archivos especificados en el script.

