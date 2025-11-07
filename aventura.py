import random
import time

mochila = []
mochila_backup = []  # cópia de segurança

itens_possiveis = ["Espada", "Poção", "Escudo", "Cristal Raro", "Mapa Antigo", "Tocha"]

print("🎒 Você iniciou sua aventura com uma mochila vazia!\n")

for rodada in range(5):
    time.sleep(0.8)
    evento = random.choice(["encontrou", "perdeu", "duplicou"])
    item = random.choice(itens_possiveis)

    if len(mochila) == 0:
        print('\033[3m' + "Voce caminha mas nao encontra nada" + '\033[0m')

    mochila_backup = mochila.copy()


    if evento == "encontrou":
        print(f"✨ Você encontrou um(a) {item} e guardou na mochila!\n")
        mochila.append(item)# adiciona o item encontrado na jornada

    elif evento == "perdeu" and len(mochila) > 0:
        print(f"💥 Você tropeçou e perdeu seu item {mochila[-1]}!")
        mochila.pop()

    elif evento == "duplicou" and len(mochila) > 0:
        print(f"🌀 Um feitiço duplicou seu item {mochila[0]}!")
        mochila.append(mochila[0])

    print(f"📦 Mochila atual: {mochila}\n")

time.sleep(1)
print("🔍 Verificando o conteúdo final da mochila...\n")



pocao = mochila.count("Poção")

if "Espada" in mochila:
    espada = mochila.index("Espada")
    print(f"\033[0;34mVocê tem {pocao} Poções\033[0m")
    print(f"\033[0;34mA espada está na posição {espada}\033[0m")
else:
    print(f"\033[0;34mVocê tem {pocao} Poções\033[0m")
    print("Você não encontrou nenhuma espada 😢")

    
print("\n📜 Aventura concluída!")
print(f"Mochila final: {mochila}")