import os
from uniswap import Uniswap
from dotenv import load_dotenv
from web3 import Web3


load_dotenv()

#############################################
# Variables to intialize the uniswap object
#############################################


#Your Address
address = os.environ.get("ADDRESS")

#Key to sign transactions
private_key = os.environ.get("SECRET_KEY")

#Uni version
version = 3

#Infura Node Provider
provider = os.environ.get("PROVIDER")

#Addresses for Router and factor
#
router_contract_addr =  "0xE592427A0AEce92De3Edee1F18E0157C05861564"
factory_contract_addr = "0x1F98431c8aD98523631AE4a59f267346ea31F984"




# Uniswap and web3 objects intialized
#

uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider,
                  factory_contract_addr=factory_contract_addr, router_contract_addr=router_contract_addr)
                  
web3 = Web3(Web3.HTTPProvider(provider))

#############################################
# End of object intializations
#############################################




#############################################
# SAMPLE ERC20 Addresses - RINKEBY TESTNET
##############################################

dai = '0xc7ad46e0b8a400bb3c915120d284aafba8fc4735'
weth = '0xc778417e063141139fce010982780140aa0cd5ab'

dai = web3.toChecksumAddress(dai)
weth = web3.toChecksumAddress(weth)
#############################################
#############################################


#############################################
# Need to quote swap rates. Found this in Uni gituhub:
    
# @dev These functions are not gas efficient and should
#_not_ be called on chain. Instead, optimistically execute
# the swap and check the amounts in the callback.

# Therefore to check swap rates we need to call correct
# swap function without changing state of ethereum

# Maybe we can work on this later
##############################################



##############################################
# Make a swap from dai to weth
#
# Problems to fix in future:
# API uses legacy transaction format
# this may cause small latency issues
# Update API to accept current eth Transaction format
##############################################



# This trades 1 dai for as much eth as possible
uniswap.make_trade(dai, weth, 1*10**18)



##############################################
# Oracles! We need a pricing oracle
# For this we will use uni price feeds and chain link
# In the future build a oracle aggerator of more dexes on eth
# and other chains. Want resistance versus large swap orders
##############################################



