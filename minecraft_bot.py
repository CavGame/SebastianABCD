import time
from minecraft import authentication, server

# Autenticazione con Minecraft
user = authentication.Authenticator('SebastianABCD', 'nocepandistelle2')
client = server.MinecraftClient('your.server.ip', 25565, user)

# Funzione per muovere l'AI
def move_to(x, y, z):
    client.send_command(f'tp {x} {y} {z}')

# Funzione per costruire
def build_structure():
    client.send_command('place block at coordinates')  # esempio di comando per costruire

# Funzione per mostrare lo stato
def get_status():
    position = client.get_position()
    inventory = client.get_inventory()
    return f'Posizione: {position}, Inventario: {inventory}'

# Esegui il bot in un loop
while True:
    # Decidi cosa fare
    move_to(100, 64, 100)  # esempio di movimento
    build_structure()  # esempio di costruzione
    print(get_status())  # mostra lo stato ogni tanto
    time.sleep(60)  # pausa tra le azioni
