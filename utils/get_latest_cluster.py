import json
import sys
from web3 import Web3
from Crypto.Hash import keccak
from typing import Any, Dict, cast, Union

from eth_typing import HexStr
from eth_utils import event_abi_to_log_topic
from hexbytes import HexBytes
from web3._utils.abi import get_abi_input_names, get_abi_input_types, map_abi_data
from web3._utils.normalizers import BASE_RETURN_NORMALIZERS
from web3.contract import Contract


class EventLogDecoder:
    def __init__(self, contract: Contract):
        self.contract = contract
        self.event_abis = [abi for abi in self.contract.abi if abi['type'] == 'event']
        self._sign_abis = {event_abi_to_log_topic(abi): abi for abi in self.event_abis}
        self._name_abis = {abi['name']: abi for abi in self.event_abis}

    def decode_log(self, result: Dict[str, Any]):
        data = [t[2:] for t in result['topics']]
        data += [result['data'][2:]]
        data = "0x" + "".join(data)
        return self.decode_event_input(data)

    def decode_event_input(self, data: Union[HexStr, str], name: str = None) -> Dict[str, Any]:
        # type ignored b/c expects data arg to be HexBytes
        data = HexBytes(data)  # type: ignore
        selector, params = data[:32], data[32:]

        if name:
            func_abi = self._get_event_abi_by_name(event_name=name)
        else:
            func_abi = self._get_event_abi_by_selector(selector)

        names = get_abi_input_names(func_abi)
        types = get_abi_input_types(func_abi)

        decoded = self.contract.w3.codec.decode(types, cast(HexBytes, params))
        normalized = map_abi_data(BASE_RETURN_NORMALIZERS, types, decoded)

        return dict(zip(names, normalized))

    def _get_event_abi_by_selector(self, selector: HexBytes) -> Dict[str, Any]:
        try:
            return self._sign_abis[selector]
        except KeyError:
            raise ValueError("Event is not presented in contract ABI.")

    def _get_event_abi_by_name(self, event_name: str) -> Dict[str, Any]:
        try:
            return self._name_abis[event_name]
        except KeyError:
            raise KeyError(f"Event named '{event_name}' was not found in contract ABI.")


class SSVNetwork:
    abi = []
    contract = None
    web3: Web3 = None

    def __init__(self, ssv_address, _web3: Web3, abi_path=None):
        self._import_abi(filepath=abi_path)
        self.web3 = _web3
        self.contract = self.web3.eth.contract(
            abi=self.abi, address=ssv_address)

    def _import_abi(self, filepath):
        if filepath is None:
            with open("SSVNetwork.json", "r") as file:
                self.abi = json.load(file)["abi"]
            file.close()
        else:
            with open(filepath, "r") as file:
                self.abi = json.load(file)["abi"]
            file.close()

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
            print(results)
            if len(results) > 0:
                return results[max(results)]
            to_block = from_block
            from_block -= step
        return [0, 0, 0, 0, True]


if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider(sys.argv[1]))
    operator_id = sys.argv[2]
    owner_address = sys.argv[3]
    print(operator_id)
    print(owner_address)
    ssv = SSVNetwork(sys.argv[4], web3)
    print(ssv.get_latest_cluster(owner_address,operator_id))

    # TO run: python get_latest_cluster.py <eth_rpc> <operator_ids_comma_separated> <owner_address> <ssv_address>
