# Examples without any asserts 

from typing import Any, List

from hicopy import atom, leval, assoc, pairlis


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
    ["cons", 1, ["quote", [10, 20]]],
    ["cons", ["quote", [1, 2]], ["quote", [10, 20]]],  # [1, 2, 10, 20]
    ["cond", [["eq", 1, 1], "true"], [["atom", ["quote", 2]], "false"], ["t", "default"]],
    ["cond", [["atom", ["quote", 2]], "cake"], ["t", "default"]],
    ["cond", [["atom", ["quote", [1, 2]]], "false"], ["t", "default"]],
    # assoc 
    #assoc("a", [["a", 1], ["b", 2], ["c", 3]]),   # ["a", 1]
    #assoc("d", [["a", 1], ["b", 2], ["c", 3]]),   # []
    ## pairlis
    #pairlis(["x", "y"], [1, 2]),     # zip, so [[x, 1], [y, 2]]
    #pairlis(["x", "y"], [1, 2, 5]),  # zip, so [[x, 1], [y, 2]]
]



def main(examples: List[Any]) -> None:
    for n, ex in enumerate(examples):
        try:
            print(f"{n}: [{ex}] -> {leval(ex)}")
        except Exception as e:
            print(f"{n}: EXCEPTION [{ex}], {e}")


if __name__ == "__main__":
    main(example_inputs)
