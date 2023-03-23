# BlockChain-Users
An example of adding and removing users in the blockchain using the smart contract.


# :exclamation: Requirements 

Please use the following command to install the requirements so that the framework can operate properly :

```
pip install pip install py-solc-x web3
```

or 

```
python3 -m pip install py-solc-x web3
```

# :grey_question: Usage

The initial step is to compile the Solidity code ([UsersList.sol](UsersList.sol)) utilizing the script [compile_contract.py](compile_contract.py) and create a file named ([compiled_code.json](compiled_code.json)) that will be utilized subsequently. To perform the compilation, utilize the following command:

```
python compile_contract.py
```

After compiling the smart contract, the next step is to deploy it on the blockchain. However, before doing so, it is essential to use a simulated blockchain by using the [Ganache CLI](https://www.npmjs.com/package/ganache-cli) and executing the following command.

```
ganache-cli --deterministic
```

And then deploy the contract with : 

```
python deploy_contract.py
```

Subsequently, we will employ the address generated during the deployment process to interact with our smart contract.

To add users on the blockchain. :

```
python add_user.py
```

To display the users saved on the blockchain : 

```
python display_users.py
```

