from web3 import Web3
import json
import time

# ------------------------------
# 1) Conexión a Ganache
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
# 3) Parámetros
# ------------------------------
cuentas = web3.eth.accounts
cuenta_prueba = cuentas[0]  # Usar siempre la misma

print(" Ejecutando prueba de detección de anomalía (doble voto)...")

# ------------------------------
# 4) Emitir voto válido (1ra vez)
# ------------------------------
try:
    tx_hash = contrato.functions.votar(1).transact({'from': cuenta_prueba})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(" Primer voto emitido correctamente.")
except Exception as e:
    print(" Error inesperado al emitir primer voto:", e)

# ------------------------------
# 5) Forzar intento de doble voto y medir tiempo de detección
# ------------------------------
inicio = time.time()

try:
    tx_hash = contrato.functions.votar(1).transact({'from': cuenta_prueba})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(" El doble voto NO fue detectado (error en la lógica).")
except Exception as e:
    fin = time.time()
    tiempo_deteccion = fin - inicio
    print(f" Tiempo de detección de la anomalía: {tiempo_deteccion:.4f} segundos")

# ------------------------------
# 6) Interpretación
# ------------------------------
print("\n Si el tiempo es cercano a cero, significa detección inmediata por validación del contrato.")
