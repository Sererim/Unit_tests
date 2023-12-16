from src.compare_averages_of_list import (
    compare, find_average, msgs)

def test_average() -> None:
    """
    Testing work of average function.
    """
    assert find_average([2, 2]) == 2
    assert find_average([10, 10]) == 10
    assert find_average([-1, 1]) == 0

def test_compare_message_one() -> None:
    """
    Testing work of the first stream flow.
    """
    assert compare([1, 2], [1]) == msgs[0]

def test_compare_message_two() -> None:
    """
    Testing work of the second stream flow.
    """
    assert compare([1, 1, 1], [1, 3]) == msgs[1]

def test_compare_message_three() -> None:
    """
    Testing work of the third stream flow.
    """
    assert compare([1, 1], [1, 1]) == msgs[2]
