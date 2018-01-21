import artifacts

from config import config
from servicesContracts.requestEthereum_service import RequestEthereumService
from servicesExtensions.requestSyncrhoneExtensionEscrow_service import RequestSynchroneExtensionEscrowService
from servicesExternal.ipfs_service import Ipfs
from servicesExternal.web3_single import Web3Single

'''Constants'''
REQUEST_ETHEREUM_ARTIFACT = artifacts.requestEthereumArtifact
REQUEST_CORE_ARTIFACT = artifacts.requestCoreArtifact
BN = Web3Single.BN()

class RequestCoreService:
    def __init__(self):
        self.web3single = Web3Single.getInstance()
        self.ipfs = Ipfs.get_instance()
        self.abi_request_core = REQUEST_CORE_ARTIFACT["abi"]
        self.abi_request_ethereum = REQUEST_ETHEREUM_ARTIFACT["abi"]
        self.request_core_services = RequestCoreService()
        
        if not REQUEST_ETHEREUM_ARTIFACT[self.web3single.networkName]:
            raise Exception("RequestEthereum Artifact: no config for network: " + self.web3single.networkName)

        self.address_request_ethereum = REQUEST_ETHEREUM_ARTIFACT["networks"][self.web3single.networkName].address
        self.instance_request_ethereum = self.web3single.web3.eth.Contract(self.abi_request_ethereum, self.address_request_ethereum)

    def getCurrentNumRequest(self):
        pass

    def getVersion(self):
        pass

    def getCollectEstimation(self, expectedAmount: any, currencyContract: str, extension: str):
        pass

    def getRequest(self, requestId: str):
        pass

    def getRequestByTransactionHash(self, hash:str):
        pass

    def getRequestEvents(self, requestId: str, fromBlock: int = None, toBlock: int = None):
        pass

    def getRequestsByAddress(self, address: str, fromBlock: int = None, toBlock: int = None):
        pass

    def getIpfsFile(self, hash: str):
        pass