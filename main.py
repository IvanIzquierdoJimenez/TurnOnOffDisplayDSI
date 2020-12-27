import shlex, subprocess, socket, threading
#import RPi.GPIO as GPIO

# Creamos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.50", 5090))

# vamos a crear una register() para el server y lo mandamos
command = "register(asfa::pulsador::conex)\n"
try:
    s.send(command.encode())
except socket.error:
    print("No se ha conectado el socket...")

# vamos a crear las lineas de comandos 

Encendido = 'sudo bash -c \'echo 0 > /sys/class/backlight/rpi_backlight/bl_power\''
Apagado = 'sudo bash -c \'echo 1 > /sys/class/backlight/rpi_backlight/bl_power\''

# Vamos a recibir el estado del pulsador de encendido 

"""GPIO.setMode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)
GPIO.setup()"""

def command():
    while True:
        r = s.recv(128)
        #print(str(r))
        if r == b'connected=true\r\n':
            if r == b'asfa::pulsador::conex=1\r\n':
                conex = shlex.split(Encendido)
                subprocess.call(conex)
            elif r == b'asfa::pulsador::conex=0\r\n':
                Deconex = shlex.split(Apagado)
                subprocess.call(Deconex)
        else:
            break

main = threading.Thread(target=command)
main.start()


