import json
import os
from web3 import Web3
from dotenv import load_env

load_dotenv()

server = os.environ.get("SERVER")
web3 = Web3(Web3.HTTPProvider(server))
address1 = os.environ.get("ADDRESS")
privateKey1 = os.environ.get("SECRET_KEY")

# WeightedOracleLibrary from UniswapV3
abi = '[]'
bytecode = '0x602d6023600b82828239805160001a607314601657fe5b30600052607381538281f3fe73000000000000000000000000000000000000000030146080604052600080fdfea164736f6c6343000706000a'


def intializeContract(web3, ABI, bytecode):
    '''

    Parameters
    ----------
    web3 : web3 object
    ABI : a string of the abi of the smart contract
    bytecode : string of the bytecode of smart contract
    Returns
    -------
    A contract object
    '''

    abi = json.loads(ABI)
    return web3.eth.contract(abi=abi, bytecode=bytecode)


def deployContract(web3, contract, address, privateKey, **kwargs):
    '''

    Parameters
    ----------
    web3 : web3 object
    contract : web3.eth.contract object returned from intializeContract
    address : string of sender's address
    privateKey : private key of sender
    **kwargs : constructor arguments
    Returns
    -------
    A reciept for the transactions
    Note
    -------
    This should be updated so that the constructor deployContract 
    accepts constructor variables
    '''

    nonce = web3.eth.getTransactionCount(address)
    tx = contract.constructor(
        **kwargs).buildTransaction({'nonce': nonce, 'from': address})
    signed_tx = web3.eth.account.signTransaction(tx, privateKey)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.eth.waitForTransactionReceipt(tx_hash)


contract = intializeContract(web3, abi, bytecode)
receipt = deployContract(web3, contract, address1, privateKey1)
caddress = receipt['contractAddress']


##
# Obtain contract instance
##
def contractInstance(web3, abi, Address):
    '''

    Parameters
    ----------
    web3 : web3 instance
    abi  : contract abi
    Address : contracts address
    Returns
    -------
    Returns a contract instance. This instance interacts with the original 
    smart contract that has been deployed to the blockchain.
    '''
    address = web3.toChecksumAddress(Address)
    return web3.eth.contract(abi=abi, address=address)


oracle = contractInstance(web3, abi, caddress)
print(oracle.functions.consult().call())
