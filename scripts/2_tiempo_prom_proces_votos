
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
direccion_contrato = '0xAbC1234567890Def1234567890aBCDef12345678'

with open('VotacionABI.json', 'r') as f:
    abi = json.load(f)

contrato = web3.eth.contract(address=direccion_contrato, abi=abi)

# ------------------------------
# 3) Parámetros de prueba
# ------------------------------
cuentas = web3.eth.accounts
num_votos = 10000

# ------------------------------
# 4) Ejecutar prueba y medir tiempos individuales
# ------------------------------
print(f" Ejecutando prueba de {num_votos} votos para medir tiempo promedio por voto...")

tiempos_individuales = []

for i in range(num_votos):
    inicio = time.time()
    tx_hash = contrato.functions.votar(1).transact({'from': cuentas[i % len(cuentas)]})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    fin = time.time()
    
    tiempo_procesamiento = fin - inicio
    tiempos_individuales.append(tiempo_procesamiento)

# ------------------------------
# 5) Calcular tiempo promedio
# ------------------------------
promedio_procesamiento = sum(tiempos_individuales) / num_votos

print(f"\n Votos procesados: {num_votos}")
print(f" Tiempo promedio de procesamiento por voto: {promedio_procesamiento:.4f} segundos")

