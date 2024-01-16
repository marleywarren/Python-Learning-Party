# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/harvard_course.py"
# docs.python.org

# can also chan special functions together
name = input("What is your name? ")

name = name.strip().title()

first_name, last_name = name.split(" ") # demostrates that you can assign multiple variables at once
print(f"hello, {first_name}") #f indiaces special formatting, and the {} indicates a special string

# print("hello,", name, sep=" ", end= "")





