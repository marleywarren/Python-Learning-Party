# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/cat.py"

def main():
    number = get_number()
    meow(number)

def meow(n):
    for i in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("What is the number? "))
        if n > 0:
            break
    return n

main()
