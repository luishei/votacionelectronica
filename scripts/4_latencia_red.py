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
num_consultas = 10000 

latencias_ms = []

print(f" Midiendo Latencia de red con {num_consultas} consultas a totalVotos() ...")

for i in range(num_consultas):
    inicio = time.time()
    contrato.functions.totalVotos().call()
    fin = time.time()
    
    latencia_ms = (fin - inicio) * 1000  # Convertir a milisegundos
    latencias_ms.append(latencia_ms)

# ------------------------------
# 4) Calcular latencia promedio
# ------------------------------
promedio_latencia = sum(latencias_ms) / num_consultas

print(f"\n Consultas realizadas: {num_consultas}")
print(f" Latencia promedio de red: {promedio_latencia:.4f} ms")
