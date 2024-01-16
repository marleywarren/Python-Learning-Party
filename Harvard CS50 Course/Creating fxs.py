# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/Creating fxs.py"

def hello(to= "world"): # this equal sign sets a defualt value if the user just uses the hello fx without any arguments
    print("hello, ", to)

def main():
    name = input("What is your name? ")
    name = name.title().strip()
    hello(name)

main()