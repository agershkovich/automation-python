from fibonacci.fibonacci import generateFibonacci


def test_fibonacci_1():
    assert generateFibonacci(1) == [1]


def test_fibonacci_10():
    assert generateFibonacci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fibonacci_5():
    assert generateFibonacci(5) == [1, 1, 2, 3, 5]
