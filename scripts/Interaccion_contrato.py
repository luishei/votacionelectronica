from web3 import Web3
import json

# Conectar a Ganache
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Dirección del contrato y del usuario
direccion_contrato = '0xEe9E39e3780a4b9407c98194f52b6D3ae20F2754'
direccion_usuario = web3.eth.accounts[0]

# ABI del contrato
with open('VotacionABI.json', 'r') as f:
    abi = json.load(f)

# Instanciar el contrato
contrato = web3.eth.contract(address=direccion_contrato, abi=abi)

# Enviar voto al candidato 1
tx_hash = contrato.functions.votar(1).transact({'from': direccion_usuario})
web3.eth.wait_for_transaction_receipt(tx_hash)

# Ver total de votos
total = contrato.functions.totalVotos().call()
print(f"Total de votos: {total}")
