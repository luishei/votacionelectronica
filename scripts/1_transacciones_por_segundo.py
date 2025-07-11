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
num_transacciones = 10000 

# ------------------------------
# 4) Medir tiempo de ejecución
# ------------------------------
print(f"⏱️ Ejecutando prueba de {num_transacciones} votos...")

start_time = time.time()

for i in range(num_transacciones):
    tx_hash = contrato.functions.votar(1).transact({'from': cuentas[i % len(cuentas)]})
    web3.eth.wait_for_transaction_receipt(tx_hash)

end_time = time.time()

# ------------------------------
# 5) Calcular TPS
# ------------------------------
tiempo_total = end_time - start_time
tps = num_transacciones / tiempo_total

print(f"\n Transacciones procesadas: {num_transacciones}")
print(f" Tiempo total: {tiempo_total:.2f} segundos")
print(f" Transacciones por Segundo (TPS): {tps:.2f}")
