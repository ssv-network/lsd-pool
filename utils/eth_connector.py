from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
import web3
import requests


class EthNode:
    account = None
    eth_node = None
    local = False

    def __init__(self, rpc_url, private_key):
        self.eth_node = Web3(Web3.HTTPProvider(rpc_url))
        self.eth_node.eth.set_gas_price_strategy(rpc_gas_price_strategy)
        if '127.0.0.1' or 'localhost' in rpc_url:
            # w3.eth.accounts()[0]
            self.local = True
        else:
            pass
        self.account = self.eth_node.eth.account.from_key(
            private_key)

    def make_tx(self, tx):
        # self.eth_node.eth.call(tx)
        tx['nonce'] = self.eth_node.eth.get_transaction_count(
            self.account.address)
        # self.eth_node.eth.call(tx)
        # if self.local:
        #     tx.pop('maxFeePerGas')
        signed_tx = self.eth_node.eth.account.sign_transaction(
            tx, self.account.key)
        print(tx)
        tx_hash = self.eth_node.eth.send_raw_transaction(
            signed_tx.rawTransaction)
        tx_receipt = self.eth_node.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt.status == 1:
            print('TX successful')
            return True
        else:
            print('TX reverted')
            return False

    def get_balance(self, address):
        return self.eth_node.eth.get_balance(address) / 10 ** 18


class ConsensusNode:
    api_url = None
    VALIDATOR_EXIT = "/eth/v1/beacon/pool/voluntary_exits"
    API_VERSION = '/eth/v1/node/version'
    GENESIS_CALL = '/eth/v1/beacon/genesis'
    HEADERS = '/eth/v1/beacon/headers'
    VALIDATOR_STATE = '/eth/v1/beacon/states/finalized/validators/{}'

    def __init__(self, url):
        self.api_url = url
        self.__is_connected()

    def __is_connected(self):
        response = requests.get(self.api_url + self.GENESIS_CALL)
        if response.status_code == 200:
            return True
        else:
            raise response.raise_for_status()

    def submit_voluntary_exit(self, signed_message):
        response = requests.post(self.api_url + self.VALIDATOR_EXIT, json=signed_message)

        if response.status_code < 300:
            print("Validator exit submitted")
        else:
            response.raise_for_status()

    def get_validator_index(self,pubkey):
        response = requests.get(self.api_url + self.VALIDATOR_STATE.format(pubkey))

        if response.status_code < 300:

            return response.json()["data"]["index"]
        else:
            print("Validator pubkey not found")

            response.raise_for_status()

    def get_latest_epoch(self):
        response = requests.get(self.api_url + self.HEADERS)
        if response.status_code < 300:
            print("latest epoch ")
            return int(int(response.json()["data"][0]["header"]["message"]["slot"])/32)
        else:
            response.raise_for_status()
