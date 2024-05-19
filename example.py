# Examples without any asserts 

from typing import Any, List

from hicopy import atom, leval


example_inputs = [
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
]

exp_responses = [
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
    50
]



def main(examples: List[Any]) -> None:
    #from pudb import set_trace; set_trace()
    for n, ex in enumerate(examples):
        try:
            print(f"{n}: [{ex}] -> {leval(ex)}")
        except Exception as e:
            print(f"{n}: EXCEPTION [{ex}], {e}")


if __name__ == "__main__":
    main(example_inputs)
