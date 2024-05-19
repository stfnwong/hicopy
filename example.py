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
]



def main(examples: List[Any]) -> None:
    for n, ex in enumerate(examples):
        try:
            print(f"{n}: [{ex}] -> {leval(ex)}")
        except Exception as e:
            print(f"{n}: [{ex}], {e}")


if __name__ == "__main__":
    main(example_inputs)
