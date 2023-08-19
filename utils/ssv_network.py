import json
from collections import namedtuple

from web3 import Web3
from utils.eth_connector import EthNode


class SSVNetwork:
    abi = []
    contract = None
    web3: Web3 = None
    goerli: Web3 = None

    def __init__(self, ssv_address, _web3: Web3, _goerli: Web3, abi_path=None):
        self._import_abi(filepath=abi_path)
        self.web3 = _web3
        self.goerli = _goerli
        self.contract = self.web3.eth.contract(abi=self.abi, address=ssv_address)
        self.contract_goerli = self.goerli.eth.contract(abi=self.abi, address=ssv_address)

    def _import_abi(self, filepath):
        if filepath is None:
            with open("utils/ISSVNetwork.json", "r") as file:
                self.abi = json.load(file)["abi"]
            file.close()
        else:
            with open(filepath, "r") as file:
                self.abi = json.load(file)["abi"]
            file.close()

    def get_operator_pubkey(self, id):
        step = 50000
        from_block = self.goerli.eth.get_block_number() - step
        to_block = self.goerli.eth.get_block_number()
        while to_block > 8661727:
            filter = self.contract_goerli.events.OperatorAdded.createFilter(fromBlock=from_block, toBlock=to_block,
                                                                            argument_filters={'operatorId': id})
            result = filter.get_all_entries()
            if len(result) > 0:
                return str(result[0].args.publicKey).split("x02d")[1].split("\\x00\\x00")[0]
            to_block = from_block
            from_block -= step
        raise ValueError("Operator id doesn't exist")

    def get_latest_cluster(self, owner_address, operator_ids):
        step = 30000
        from_block = self.web3.eth.get_block_number() - step
        to_block = self.web3.eth.get_block_number()
        while to_block > 8661727:
            filters = [self.contract.events.ValidatorAdded.build_filter(),
                       self.contract.events.ValidatorRemoved.build_filter(),
                       self.contract.events.ClusterLiquidated.build_filter(),
                       self.contract.events.ClusterReactivated.build_filter(),
                       self.contract.events.ClusterWithdrawn.build_filter(),
                       self.contract.events.ClusterDeposited.build_filter()]
            results = {}
            for filter_result in filters:
                filter_result.fromBlock = from_block
                filter_result.toBlock = to_block
                filter_result.args.owner.match_single(owner_address)
                filter_deploy = filter_result.deploy(self.web3)
                result = filter_deploy.get_all_entries()
                if len(result) > 0:
                    for data in result:
                        if sorted(result[0].args.operatorIds) == sorted(operator_ids):
                            results[data.blockNumber] = data.args.cluster
            if len(results) > 0:
                return results[max(results)]
            to_block = from_block
            from_block -= step
        return [0, 0, 0, True, 0]

    def get_latest_nonce(self, owner_address):
        step = 30000
        from_block = self.web3.eth.get_block_number() - step
        to_block = self.web3.eth.get_block_number()
        nonce = 0
        while to_block > 8661727:
            filter = self.contract.events.ValidatorAdded.build_filter()
            results = {}
            filter.fromBlock = from_block
            filter.toBlock = to_block
            filter.args.owner.match_single(owner_address)
            filter_deploy = filter.deploy(self.web3)
            result = filter_deploy.get_all_entries()
            if len(result) > 0:
                nonce += len(result)
            to_block = from_block
            from_block -= step
        return nonce


class SSVNetworkview:
    abi = []
    web3: Web3 = None

    def __init__(self, ssv_address, web3: Web3, abi_path=None):

        self._import_abi(filepath=abi_path)
        self.contract = web3.eth.contract(abi=self.abi, address=ssv_address)

    def _import_abi(self, filepath):
        if filepath is None:
            with open("utils/SSVNetworkViews.json", "r") as file:
                self.abi = json.load(file)["abi"]
            file.close()
        else:
            with open(filepath, "r") as file:
                self.abi = json.load(file)["abi"]
            file.close()

    def get_operator_fee(self, id):
        return self.contract.functions.getOperatorFee(id).call()

    def get_network_fee(self):
        return self.contract.functions.getNetworkFee().call()


class SSVToken:
    abi = [{
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }, {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    }
    ]

    def __init__(self, ssv_address, web3: Web3):
        self.contract = web3.eth.contract(abi=self.abi, address=ssv_address)

    def get_balance(self, account_address):
        return self.contract.functions.balanceOf(account_address).call()

    def transfer_token(self, address, amount, account_address):
        return self.contract.functions.transfer(address, amount).buildTransaction(
            {"from": account_address})




