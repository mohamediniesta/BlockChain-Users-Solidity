from web3 import Web3
import json

f = open('compiled_code.json')
  
compiled_sol = json.load(f)
    
# get bytecode
bytecode = compiled_sol["contracts"]["UsersList.sol"]["UsersList"]["evm"]["bytecode"]["object"]
# get abi
abi = json.loads(compiled_sol["contracts"]["UsersList.sol"]["UsersList"]["metadata"])["output"]["abi"]

# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"
contract_address = "0xC89Ce4735882C9F0f0FE26686c53074E09B0D550"

users_list = w3.eth.contract(address=contract_address, abi=abi)

# Get the number of latest transaction
nonce = w3.eth.get_transaction_count(address)


first_name = input("First name > ")
last_name = input("Last name > ")
username = input("Username > ")
password = input("Password > ")
email = input("Email > ")
role = input("Role > ")
phone = input("Phone number > ")

store_user = users_list.functions.addUser(
    first_name, last_name, username, password, email, role, phone
).build_transaction({"chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce})


# Sign the transaction
sign_store_user = w3.eth.account.sign_transaction(
    store_user, private_key=private_key
)
# Send the transaction
send_store_user = w3.eth.send_raw_transaction(sign_store_user.rawTransaction)
transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_user)

print("User has been added to the blockchain")