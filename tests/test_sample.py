def mult(*args):
    result = 1
    for number in args:
        result *= number
    return result


def test_mult():
    assert mult(3, 6) == 18
