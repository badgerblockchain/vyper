contract_data1: public(int32)
contract_data2: public(int32)

@external
def __init__(val1: int32, val2: int32):
    self.contract_data1 = val1
    self.contract_data2 = val2

@external
def set_v1(new_value: int32):
    if(new_value > 1000):
        raise "MaxValueExceeded"
    self.contract_data1 = new_value

@external
def set_v2(new_value: int32):
    self.contract_data2 = new_value

@external
@view
def get_v1() -> int32:
    return self.contract_data1

@external
@view
def get_v2() -> int32:
    return self.contract_data2