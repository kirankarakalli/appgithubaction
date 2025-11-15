from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(5,3)==2


def test_sub():
    assert sub(2,2)==0
    assert sub(2,1)==1
    assert sub(1,2)==0
    assert sub(1,3)==-1




