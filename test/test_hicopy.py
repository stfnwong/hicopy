# All the tests should fit in a single file

from hicopy import (
    atom,
    car,
    cdr,
    leval,
    assoc,
    pairlis
)


# Tests for basic stuff - honestly isn't life a bit short to write all these?
def test_atomic_ops():
    inp = ["atom", ["quote", [1, 2, 3]]]

    #from pudb import set_trace; set_trace()
    assert car(inp) == "atom"
    assert cdr(inp) == [["quote", [1, 2, 3]]]
    assert car(cdr(inp)) == ["quote", [1, 2, 3]]


def test_car_cdr():
    inp = ["atom", [1, 2, 3], [4, 5, 6]]

    assert car(inp) == "atom"


def test_eval_const():
    assert isinstance(leval(42), int)
    assert isinstance(leval(42.0), float)


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


def test_eval():
    inputs = [
        [atom],
        42,
        ["quote", [10, 20]],
        ["atom", 1],
        ["atom", ["quote", 1]],
        ["atom", ["quote", [1, 2, 3]]],
        ["eq", 1, 1],
        ["eq", 1, 2],
        ["car", ["quote", [1000, 20]]],
        ["cdr", ["quote", [1000, 20, 1.1]]],
        ["car", ["car", ["cdr", ["cdr", ["cdr", ["quote", [1, 2, 10, [50, 100]]]]]]]],
        ["cons", 1, ["quote", [10, 20]]],
        ["cons", ["quote", [1, 2]], ["quote", [10, 20]]],
        ["cond", [["eq", 1, 1], "true"], [["atom", ["quote", 2]], "false"], ["t", "default"]],
        ["cond", [["atom", ["quote", 2]], "cake"], ["t", "default"]],
        ["cond", [["atom", ["quote", [1, 2]]], "false"], ["t", "default"]],
    ]

    exp_outputs = [
        [],
        42,
        [10, 20],
        True,
        True,
        False,
        True,
        False,
        1000,
        [20, 1.1],
        50,
        [1, 10, 20],
        [[1, 2], 10, 20],
        "true",
        "cake",
        "default",
    ]

    # Check we didn't fuck up the spec
    assert len(inputs) == len(exp_outputs)

    for inp, exp_out in zip(inputs, exp_outputs):
        assert leval(inp) == exp_out


def test_assoc():
    # Format is (target, input)
    inputs = [
        ("a", [["a", 1], ["b", 2], ["c", 3]]),
        ("d", [["a", 1], ["b", 2], ["c", 3]]),
    ]

    exp_outputs = [
        ["a", 1],
        [],
    ]

    for inp, exp_out in zip(inputs, exp_outputs):
        assert assoc(inp[0], inp[1]) == exp_out


def test_pairlis():
    # Format is (x, y)
    inputs = [
        (["x", "y"], [1, 2]),
        (["x", "y"], [1, 2, 5]),
    ]

    exp_outputs = [
        [["x", 1], ["y", 2]],
        [["x", 1], ["y", 2]],
    ]

    for inp, exp_out in zip(inputs, exp_outputs):
        assert pairlis(inp[0], inp[1]) == exp_out
