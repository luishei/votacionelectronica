import time
from web3 import Web3
import json

# ------------------------------
# 1) Conexión a Ganache local
# ------------------------------
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
assert web3.is_connected(), "No se pudo conectar a Ganache"

# ------------------------------
# 2) Cargar contrato
# ------------------------------
direccion_contrato = '0xEe9E39e3780a4b9407c98194f52b6D3ae20F2754'

with open('VotacionABI.json', 'r') as f:
    abi = json.load(f)

contrato = web3.eth.contract(address=direccion_contrato, abi=abi)

# ------------------------------
# 3) Parámetros de prueba
# ------------------------------
cuentas = web3.eth.accounts
num_votos = 10000

# ------------------------------
# 4) Ejecutar prueba de tiempo de respuesta
# ------------------------------
print(f"⏱ Ejecutando simulación de {num_votos} votos para medir Tiempo de Respuesta por voto...")

tiempos_respuesta = []

for i in range(num_votos):
    inicio = time.time()  # Momento en que el usuario envía el voto
    tx_hash = contrato.functions.votar(1).transact({'from': cuentas[i % len(cuentas)]})
    web3.eth.wait_for_transaction_receipt(tx_hash)  # Momento en que recibe confirmación (hash)
    fin = time.time()
    
    tiempo_respuesta = fin - inicio
    tiempos_respuesta.append(tiempo_respuesta)

# ------------------------------
# 5) Calcular tiempo promedio de respuesta por voto
# ------------------------------
promedio_respuesta = sum(tiempos_respuesta) / num_votos

print(f"\n Votos simulados: {num_votos}")
print(f" Tiempo promedio de respuesta por voto: {promedio_respuesta:.4f} segundos")
