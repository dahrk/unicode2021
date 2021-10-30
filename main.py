import os
from uniswap import Uniswap
from dotenv import load_dotenv

load_dotenv()

address = os.environ.get("ADDRESS")
private_key = os.environ.get("SECRET_KEY")
version = 3
provider = os.environ.get("PROVIDER")

router_contract_addr = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
factory_contract_addr = "0x1F98431c8aD98523631AE4a59f267346ea31F984"

uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider,
                  factory_contract_addr=factory_contract_addr, router_contract_addr=router_contract_addr)
# uniswap.get_weth_address()

print(address, private_key, provider, uniswap.get_weth_address())
