# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/hello.py"

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

main()