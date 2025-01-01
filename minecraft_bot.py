# minecraft_bot.py
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()  # Connessione a Minecraft

def start_mining():
    x, y, z = mc.player.getTilePos()  # Posizione del giocatore
    for i in range(10):  # Esegui mining di base
        mc.setBlock(x + i, y, z, block.STONE.id)  # Mette pietra al posto della posizione
    return "Mining completato!"

def build_house():
    x, y, z = mc.player.getTilePos()  # Posizione del giocatore
    for i in range(5):
        for j in range(5):
            for k in range(5):
                mc.setBlock(x + i, y + j, z + k, block.BRICK.id)  # Costruisce una casa di mattoni
    return "Casa costruita!"
