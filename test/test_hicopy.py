# All the tests should fit in a single file

from hicopy import (
    atom, 
    car,
    cdr,
    leval
)


# Tests for basic stuff - honestly isn't life a bit short to write all these?
def test_atomic_ops():
    inp = ["atom", ["quote", [1, 2, 3]]]

    #from pudb import set_trace; set_trace()
    assert car(inp) == "atom"
    assert cdr(inp) == [["quote", [1, 2, 3]]]    # TODO: legit?
    assert car(cdr(inp)) == ["quote", [1, 2, 3]]
    #assert car(cdr(cdr(inp))) == [1, 2, 3]




def test_car_cdr():
    inp = ["atom", [1, 2, 3], [4, 5, 6]]

    assert car(inp) == "atom"


#def test_eval_atom():
#    ret = leval([atom])
#
#    assert isinstance(ret, list)
#    assert len(ret) == 0
#
#    ret = leval(["atom", 1])
#    print(ret)
#

def test_eval_const():
    assert isinstance(leval(42), int)
    assert isinstance(leval(42.0), float)


def test_quote():
    # quote bypasses the evaluation rule and passes the data along exactly
    pass


def test_eq():
    inp = ["eq", 1, 1]
    assert car(inp) == "eq"
    assert cdr(inp) == [1, 1]
    assert car(cdr(inp)) == 1
    assert car(cdr(cdr(inp))) == 1



def test_eval_atom():
    inp = ["atom", 1]

    try:
        print(leval(inp))
    except Exception as e:
        print(e)

    assert leval(inp)       # Returns True

