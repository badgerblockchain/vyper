import pytest

from eth_tester.exceptions import TransactionFailed

@pytest.fixture
def set_get_contract(w3, get_vyper_contract):
    with open("set_get_example.vy", encoding='utf-8') as file:
        smart_contract = file.read()
    return get_vyper_contract(smart_contract, 10, 20)

def test_initial(set_get_contract):
    assert set_get_contract.contract_data1() == 10
    assert set_get_contract.contract_data2() == 20

def test_set(w3, set_get_contract):
    account = w3.eth.accounts[0]
    set_get_contract.set_v1(30, transact={"from": account})
    set_get_contract.set_v2(40, transact={"from": account})
    
    assert set_get_contract.contract_data1() == 30
    assert set_get_contract.contract_data2() == 40

    set_get_contract.set_v1(100, transact={"from": account})
    set_get_contract.set_v2(200, transact={"from": account})

    assert set_get_contract.contract_data1() == 100
    assert set_get_contract.contract_data2() == 200

def test_set_exception(w3, set_get_contract):
    account = w3.eth.accounts[0]
    with pytest.raises(TransactionFailed):
        set_get_contract.set_v1(100000, transact={"from": account})

    assert set_get_contract.contract_data1() == 10
    assert set_get_contract.contract_data2() == 20