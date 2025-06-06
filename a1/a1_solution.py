"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    return -1 * n if n < 0 else n    


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    # 4! = 4 * 3 * 2 * 1
    # 5! = 5 * 4 * 3 * 2 * 1
    result = 1
    # print(range(1, 5))
    for x in range(1, n + 1):
        result *= x
    # print(result)
    return result



T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    # return lst[::2] - pythonic way
    # Java Way #1
    # new_lst = []
    # for i in range(len(lst)):
    #     if i % 2 == 0:
    #         new_lst.append(lst[i])
    # return new_lst
    new_lst = []
    for i in range(0,len(lst),2):
        new_lst.append(lst[i])
    return new_lst



def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    s = 0
    for el in lst:
        s += el
    return s


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    # s = sum_list(lst)
    # num_values = len(lst)
    # if lst:
    #     return s/num_values
    # else:
    #     return 0
    return sum_list(lst) / len(lst) if lst else 0
    


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    if len(lst) % 2 == 1:
        # print(len(lst)//2)
        return lst[len(lst)//2]
    else:
        in1 = len(lst)//2
        in2 = in1 - 1
        # print(in1, in2)
        return (lst[in1] + lst[in2]) / 2


def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
    knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
    'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    i = 0
    current = "duck1"
    while len(lst) > 2:
        if current == "duck1":
            current = "duck2"
            i += 1
        elif current == "duck2":
            current = "goose"
            i += 1
        else:
            current = "duck1"
            lst.pop(i)
        
        # wrap around if we get to the end
        if i == len(lst):
            i = 0
        # alternate i %= len(lst)
    
    return lst


# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert factorial(5) == 120, "factorial of 5 failed"
    assert factorial(0) == 1, "factorial of 0 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert sum_list([1, 2, 3, 4]) == 10, "sum_list of [1,2,3,4] failed"
    assert sum_list([]) == 0, "sum_list of [] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert mean([]) == 0, "mean of [] failed"
    assert mean([1, 2, 3, 4, 5, 6]) == 3.5, "mean of [1,2,3,4,5,6] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5, 6]) == 3.5, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]
    names = ["roscoe", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "remess"]

    print("All tests passed!")