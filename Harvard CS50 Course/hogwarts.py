# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/hogwarts.py"

students = [
    {"name": "Herminoe", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell Terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep= ", ")