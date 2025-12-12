from src.BubbleSort import BubbleSort
import pytest

@pytest.mark.parametrize(
    ["input", "output"],
    [
        ([], []),
        ([1], [1]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([3, -1, 4, -2, 5], [-2, -1, 3, 4, 5])
    ]
)

def test_bubble_sort(input, output):
    assert BubbleSort(input) == output



