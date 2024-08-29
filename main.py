from typing import Optional
from fastapi import FastAPI
from web3 import Web3
from ens import ENS

ENSw3 = Web3(Web3.HTTPProvider('https://ethereum-rpc.publicnode.com'))
ns = ENS.from_web3(ENSw3)
app = FastAPI()


@app.get("/address/{name}")
def read_item(name: str) -> set[str | None]:
    """
    Retrieve the address or reverse name for a given name.

    Args:
        name (str): The name or 0xaddress to retrieve information for.

    Returns:
        dict: returned resolved name .
    """
    if name.startswith('0x'):
        rev = ns.name(name)
        return {rev}
    else:
        address = ns.address(name)
        return {address}

@app.get("/")
async def root():
    return {"message": "yo bud you need something ?"}

