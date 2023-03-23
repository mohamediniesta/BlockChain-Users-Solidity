with open("UsersList.sol", "r") as file:
    users_list_file = file.read()
    
    
import json #to save the output in a JSON file
from solcx import compile_standard, install_solc

# install_solc('0.8.18')

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"UsersList.sol": {"content": users_list_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] 
                }
            }
        },
    },
    solc_version="0.8.18",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)