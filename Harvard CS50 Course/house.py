# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/house.py"

name = input("What is your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Herimone":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# else:
#     print("Who?")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# else:
#     print("who"?)

match name:
    case "Harry"| "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # whatever case is not already entered
        print("Who?")