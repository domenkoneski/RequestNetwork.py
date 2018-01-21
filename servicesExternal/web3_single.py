import asyncio

from typing import Any, List
from web3 import Web3 as WEB3
from config import config

class Web3Single:

    _instance = None

    @staticmethod
    def init(web3provider, network_id):
        Web3Single._instance = Web3Single(web3Provider, network_id)

    def __init__(self, web3Provider: Any = None, network_id: int = None):
        self.web3(web3Provider if web3Provider else WEB3.providers.HttpProvider(config["ethereum"]["nodeURLDefault"][config["ethereum"]["default"]]))
        self.networkId = Web3Single.get_network_name(networkId) if networkId else config["ethereum"]["default"]

    @staticmethod
    def get_instance():
        return _instance

    @staticmethod
    def BN():
        return WEB3.utils.BN

    @staticmethod
    def get_network_name(networkId: int ) -> str:
        return {1: 'main', 2: 'morden', 3: 'ropsten', 4: 'rinkeby', 42:'kovan'}.get(networkId, 'private')

    # Async
    async def broadcast_method(self,
                        method: Any,
                        callbackTranactionHash,
                        callbackTransactionReceipt,
                        callbackTransactionConfirmation,
                        callbackTransactionError,
                        options: Any = None):
        options = dict(options)
        options["numberOfConfirmation"] = None

        if not options["from"]:
            try:
                accounts = await self.web3.eth.get_accounts()
                options["from"] = accounts[0]
            except Exception as e:
                return callbackTransactionError(e)

        forced_gas = options["gas"]
        options["value"] = options["value"] if options["value"] else 0
        options["gasPrice"] = options["gasPrice"] if options["gasPrice"] else self.web3.utils.toWei(config["ethereum"]["gasPriceDefault"], config["ethereum"]["gasPriceDefaultUnity"])

        #   TODO method call and fee(gas) estimation

    async def call_method(self, method, options: Any = None):
        pass

    async def get_default_account(self):
        pass

    # Async
    def getDefaultAccountCallback(self, callback) -> None:
        pass

    def toSolidityBytes32(self, type: str, value) -> Any:
        pass

    def arrayToBytes32(self, array, length: int) -> List[Any]:
        pass

    def isAddressNoChecksum(self, address: str) -> bool:
        if not address :
            return False
        return address and self.web3.utils.isAddress(address.toLowerCase())

    def areSameAddressesNoChecksum(self, address1: str, address2: str) -> bool:
        if not address1 or not address2 :
            return False
        return address1.toLowerCase() == address2.toLowerCase()

    def isHexStrictBytes32(self, hex: str) -> bool:
        return self.web3.utils.isHexStrict(hex) and hex.length == 66

    def generateWeb3Method(self, contractInstance,
                           name: str,
                           parameters: List[Any]) -> Any:
        return contractInstance.methods[name].apply(None, parameters)

    def decodeInputData(self, abi: List[Any], data: str) -> Any:
        pass

    def decodeTransactionLog(self, abi: List[Any], event: str, log: Any) -> Any:
        eventInput : Any
        signature : str = ''
        #check here for some function no idea
        for o in abi:
            if o.name == event:
                eventInput = o.inputs
                signature = o.signature
                break
        if log.topics[0] != signature :
            return None
        return self.web3.eth.abi.decodelog(eventInput, log.data, log.topics[1:])


    def decodeEvent(self, abi: List[Any], eventName: str, event: Any) -> Any:
        eventInput : Any
        for o in abi:
            if o.name == event:
                eventInput = o.inputs
                signature = o.signature
                break
        return self.web3.eth.abi.decodelog(eventInput, event.raw.data, event.topics[1:])

    def setUpOptions(self, options: Any) -> Any:
        if not options :
            options = {}
        if not options['numberOfConfirmation'] :
            options['numberOfConfirmation'] = 0
        #BN is no here so i used different method check
        if options['gasPrice'] :
            options['asPrice'] = self.web3.eth.gasPrice
        if options['gas'] :
            options['gas'] = self.web3.eth.gas
        return options

    # Async
    def getTransactionReceipt(self, hash: str):
        pass

    # Async
    def getTransaction(self, hash: str):
        pass

    # Async
    def getBlockTimestamp(self, blockNumber: int):
        pass

    def resultToArray(self, obj: Any) -> List[Any]:
        result : List[Any] = List[]
        for i in range(len(obj)) :
            result.append(obj[i])
        return result
