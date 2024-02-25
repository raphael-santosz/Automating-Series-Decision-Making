import random

n = int(input("Enter the number of elements: "))
my_list = []

for i in range(n):
    animes = input("Enter anime`s options: ")
    my_list.append(animes)
    
choosen = random.choice(my_list)
print("You should watch " + choosen)

