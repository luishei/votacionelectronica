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
num_votos_esperados = 10000

print(f" Simulando {num_votos_esperados} votos para medir Tasa de Integridad del Voto Registrado...")

# ------------------------------
# 4) Emitir votos válidos
# ------------------------------
for i in range(num_votos_esperados):
    cuenta = cuentas[i % len(cuentas)]
    try:
        tx_hash = contrato.functions.votar(1).transact({'from': cuenta})
        web3.eth.wait_for_transaction_receipt(tx_hash)
    except Exception as e:
        # Si falla, por ejemplo por doble voto, no cuenta como voto emitido válido
        pass

# ------------------------------
# 5) Contar votos registrados en Blockchain
# ------------------------------
votos_registrados = contrato.functions.totalVotos().call()

# ------------------------------
# 6) Calcular tasa de integridad
# ------------------------------
tasa_integridad = (votos_registrados / num_votos_esperados) * 100

print(f"\n Votos esperados: {num_votos_esperados}")
print(f" Votos efectivamente registrados: {votos_registrados}")
print(f" Tasa de Integridad del Voto Registrado: {tasa_integridad:.2f}%")
