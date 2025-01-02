import json
from server_connector import connect_to_server
from bot_commands import move_to, mine_block

# Funzione per salvare lo stato
def save_state(position, inventory):
    state = {
        "position": position,
        "inventory": inventory
    }
    with open("bot_state.json", "w") as file:
        json.dump(state, file, indent=4)

# Funzione per caricare lo stato
def load_state():
    try:
        with open("bot_state.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"position": [0, 64, 0], "inventory": []}

# Carica lo stato del bot
bot_state = load_state()
position = bot_state["position"]
inventory = bot_state["inventory"]

# Connessione a un server
server_ip = "play.examplemc.com"
nickname = "SebastianABCD"
password = "nocepandistelle2"
connect_to_server(server_ip, nickname, password)

# Esegui alcune azioni
new_position = [100, 65, 200]
position = move_to(position, new_position)
inventory.append("minecraft:diamond")
save_state(position, inventory)

# Stampa lo stato aggiornato
print(f"Posizione aggiornata: {position}")
print(f"Inventario aggiornato: {inventory}")
