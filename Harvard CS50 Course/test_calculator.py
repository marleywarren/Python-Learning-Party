# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/test_calculator.py"

from calculator import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0


def main():
    test_square()

if __name__ == "__main__":
    main()


# test git - this is a second test