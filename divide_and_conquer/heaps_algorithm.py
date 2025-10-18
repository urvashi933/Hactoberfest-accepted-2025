"""
Heap's algorithm returns the list of all permutations possible from a list.
It minimizes movement by generating each permutation from the previous one
by swapping only two elements.
More information:
https://en.wikipedia.org/wiki/Heap%27s_algorithm
"""

def heaps(arr: list) -> list:
    """
    Pure python implementation of Heap's algorithm (recursive version),
    returning all permutations of a list.

    Args:
        arr (list): The list of elements to permute.

    Returns:
        list of tuples: All permutations as tuples.

    Examples:
    >>> heaps([])
    [()]
    >>> heaps([0])
    [(0,)]
    >>> heaps([-1, 1])
    [(-1, 1), (1, -1)]
    >>> heaps([1, 2, 3])
    [(1, 2, 3), (2, 1, 3), (3, 1, 2), (1, 3, 2), (2, 3, 1), (3, 2, 1)]
    """

    # Handle base case
    if len(arr) <= 1:
        return [tuple(arr)]

    res = []

    def generate(k: int, arr: list):
        if k == 1:
            res.append(tuple(arr[:]))
            return

        generate(k - 1, arr)

        for i in range(k - 1):
            if k % 2 == 0:  # k is even
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
            else:  # k is odd
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            generate(k - 1, arr)

    generate(len(arr), arr)
    return res


def parse_input(input_str):
    """Parse input string to list of integers, with validation."""
    if not input_str.strip():
        return []
    try:
        arr = [int(item.strip()) for item in input_str.split(",")]
    except ValueError:
        raise ValueError("Input must be a comma-separated list of integers.")
    return arr


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma (e.g., 1,2,3):\n")
    try:
        arr = parse_input(user_input)
        permutations = heaps(arr)
        print(f"\nGenerated {len(permutations)} permutations:")
        for perm in permutations:
            print(perm)
    except ValueError as e:
        print("Invalid input:", e)
