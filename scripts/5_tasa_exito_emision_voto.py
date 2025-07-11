from web3 import Web3
import json

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
num_intentos = 10000  # Intentos totales de votar
votos_exitosos = 0
votos_fallidos = 0

print(f" Ejecutando simulación de {num_intentos} intentos de voto...")

for i in range(num_intentos):
    try:
        # Ejemplo de escenario: los primeros N votos son válidos
        # y luego se fuerza doble voto desde la misma cuenta para provocar fallos
        cuenta = cuentas[i % len(cuentas)]
        tx_hash = contrato.functions.votar(1).transact({'from': cuenta})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        votos_exitosos += 1
    except Exception as e:
        votos_fallidos += 1

# ------------------------------
# 4) Calcular tasa de éxito
# ------------------------------
tasa_exito = (votos_exitosos / num_intentos) * 100

print(f"\n Votos emitidos exitosamente: {votos_exitosos}")
print(f" Votos fallidos: {votos_fallidos}")
print(f" Tasa de Éxito en la Emisión del Voto: {tasa_exito:.2f}%")
