person = {
    "name": "Ali", 
    "age": 25, 
    "city": "Samarqand"
}

key = input("Kalit nomini kiriting: ")

if key in person:

    del person[key]

    print(f"{key} kalit o'chirildi.")

else:
    
    print("Bunday kalit mavjud emas!")
