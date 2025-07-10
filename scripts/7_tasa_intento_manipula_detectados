from web3 import Web3
import json

# Conexión a Ganache local
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
assert web3.is_connected(), "No se pudo conectar a Ganache"

# Dirección del contrato desplegado (ajusta la tuya)
direccion_contrato = '0xAbC1234567890Def1234567890aBCDef12345678'

# Cargar ABI del contrato
with open('VotacionABI.json', 'r') as f:
    abi = json.load(f)

# Instanciar contrato
contrato = web3.eth.contract(address=direccion_contrato, abi=abi)

# Lista de cuentas de Ganache
cuentas = web3.eth.accounts

# Parámetros de la simulación
total_votos_emitidos = 10000
intentos_manipulacion_real = 60

# Distribución de intentos detectados (según tu caso)
ataques_inyeccion = 25
modificacion_votos = 12
doble_votacion = 8
accesos_no_autorizados = 15

# -----------------------------
# 1) Simular votos válidos
# -----------------------------
print("\n Emitiendo votos válidos...")

for i in range(total_votos_emitidos):
    tx = contrato.functions.votar(1).transact({'from': cuentas[i % len(cuentas)]})
    web3.eth.wait_for_transaction_receipt(tx)

print(f"Votos emitidos correctamente: {total_votos_emitidos}")

# -----------------------------
# 2) Simular intentos de manipulación (no se ejecutan como transacciones válidas)
#    En la vida real, estos intentos se detectan y bloquean.
#    Aquí solo ilustramos cómo contarlos.
# -----------------------------

print("\n Simulando intentos de manipulación detectados...")
print(f"- Ataques de inyección detectados: {ataques_inyeccion}")
print(f"- Intentos de modificación de votos detectados: {modificacion_votos}")
print(f"- Intentos de doble votación detectados: {doble_votacion}")
print(f"- Accesos no autorizados detectados: {accesos_no_autorizados}")

total_intentos_detectados = (
    ataques_inyeccion +
    modificacion_votos +
    doble_votacion +
    accesos_no_autorizados
)

# -----------------------------
# 3) Calcular Tasa de Intentos de Manipulación Detectados (%)
# -----------------------------

tasa_detectada = (total_intentos_detectados / total_votos_emitidos) * 100
print(f"\n Tasa de Intentos de Manipulación Detectados: {tasa_detectada:.2f}%")

# -----------------------------
# 4) Verificar total de votos válidos en Blockchain
# -----------------------------

total_votos_blockchain = contrato.functions.totalVotos().call()
print(f" Total de votos registrados en Blockchain: {total_votos_blockchain}")
