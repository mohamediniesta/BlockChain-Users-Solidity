from web3 import Web3
import json

f = open('compiled_code.json')

compiled_sol = json.load(f)
    
bytecode = compiled_sol["contracts"]["UsersList.sol"]["UsersList"]["evm"]["bytecode"]["object"]

abi = json.loads(compiled_sol["contracts"]["UsersList.sol"]["UsersList"]["metadata"])["output"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"
contract_address = "0xC89Ce4735882C9F0f0FE26686c53074E09B0D550"

users_list = w3.eth.contract(address=contract_address, abi=abi)

print(users_list.functions.retrieve().call())