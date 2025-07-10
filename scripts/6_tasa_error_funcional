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
direccion_contrato = '0xAbC1234567890Def1234567890aBCDef12345678'

with open('VotacionABI.json', 'r') as f:
    abi = json.load(f)

contrato = web3.eth.contract(address=direccion_contrato, abi=abi)

# ------------------------------
# 3) Parámetros
# ------------------------------
cuentas = web3.eth.accounts
num_intentos = 10000  # Total de votos simulados
errores_funcionales = 0
votos_exitosos = 0

print(f" Ejecutando simulación de {num_intentos} votos para medir Tasa de Error Funcional...")

for i in range(num_intentos):
    try:
        # Simula: forzar errores usando misma cuenta para generar doble voto
        cuenta = cuentas[i % len(cuentas)]
        tx_hash = contrato.functions.votar(1).transact({'from': cuenta})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        votos_exitosos += 1
    except Exception as e:
        errores_funcionales += 1

# ------------------------------
# 4) Calcular Tasa de Error Funcional
# ------------------------------
tasa_error_funcional = (errores_funcionales / num_intentos) * 100

print(f"\n Votos exitosos: {votos_exitosos}")
print(f" Errores funcionales: {errores_funcionales}")
print(f" Tasa de Error Funcional: {tasa_error_funcional:.2f}%")
