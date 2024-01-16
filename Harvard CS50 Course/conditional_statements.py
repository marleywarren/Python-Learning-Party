# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/conditional_statements.py"

# % = modulo = remainder
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if (n % 2 == 0) else False

main()