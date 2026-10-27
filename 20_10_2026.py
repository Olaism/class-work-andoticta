# 1) Store the names of few of your friends to a list called names. Let it be at least five items long. 
# Print each person's name by accessing what is in the list, one at a time
names = ["ayo", "dayo", "tayo", "shayo", "bayo"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

# 2) Start with the list you created in (1) but instead of just printing each person's name, 
# print a message to them.
print("how are you doing over there, " + names[0].title() + "?")
print("how are you doing over there, " + names[1].title() + "?")
print("how are you doing over there, " + names[2].title() + "?")
print("how are you doing over there, " + names[3].title() + "?")
print("how are you doing over there, " + names[4].title() + "?")
# 3) Access the names of your friends in index 0 to 3 and store in a variable
names = names[0:3]

# 4) Print a message to each of the names in (3).
print("You are my best friend " + names[0].title() + ".")
print("You are my best friend " + names[1].title() + ".")
print("You are my best friend " + names[2].title() + ".")

# 5) Get the first and last item in (3) separately and print another message to them.
first_friend = names[0].title()
last_friend = names[2].title()

print("You are the first friend in my list " + first_friend)
print("You are the last friend in my list " + last_friend)