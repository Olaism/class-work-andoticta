# # 1. Creating and Inspecting Lists

# empty_bucket = []
# favorite_foods = [ "yam", "rice", "beans","okro","eba"]
# student_profile = ["Ugochukwu", 21, 5.4]

# # 2. Indexing and Accessing Items
# colours = ["Red", "Blue", "Green", "Yellow", "Purple"]
# print(colours[0])
# print(colours[4])
# print(colours[2])
# print(colours[-1])

# # 3. Modifying Lists (Append, Remove, Pop, and Del)
# fruits = ["apple", "banana", "cherry", "orange"]
# fruits.append("grape")
# fruits.remove("banana")
# removed_fruit = fruits.pop()
# print(fruits)
# print(removed_fruit)
# del fruits[0]
# print(fruits)

# # 4. Looping through lists
# numbers = [4, 8, 15, 16, 23, 42]
# for number in numbers:
#     print(number * 2)

# numbers = [4,8,6,7]
# for number in numbers :
#     print(number * 2)

numbers =[4, 8, 6, 7]
total = 0
for n in numbers :
    total = total + n
    print(total)

# Part 2
towns = ['Awka', 'Nibo', 'Onitsha', 'Ogidi']
towns.extend(['Nnewi', 'Ifite', 'Nise', 'Onitsha'])
towns.insert(2, "Enugu")
where_is = towns.index("Onitsha")
how_many = towns.count("Onitsha")
towns.sort(reverse=True)
print(towns)
towns.reverse()
print(towns)
print(len(towns))
new_town = towns.copy()
print(new_town)
another_towns = sorted(new_town)
print(another_towns)
towns.clear()
print(towns)
print(len(towns))
