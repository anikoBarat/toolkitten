import random
import string
'''

#### Things to try

1. 

for i in range(65,65+2*26):
    print(i, " stands for ", chr(i))


- There is something small that needs fixing. Can you spot it and fix it? 
    (Hint, we only want A-Z and a-z)

- Make a function that prints A-Z and a-z

- Make a function that asks the user for a message, and turns it into a list of numbers. 
    (It's a cypher ;))
    "I LOVE YOU" [ 73, , 76, ...]

- Optional: Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.
'''

for i in range(65, 65 + 2 * 26):
    if i in range(91, 97):
        continue
    else:
        print(i, " stands for ", chr(i))


def message_encoder():
    message = input("Message to encode: ")
    coded_message = []

    for i in message:
        coded_message.append(ord(i))
    
    print("Coded message: ", coded_message)

message_encoder()


def rec_hw(n):
    if n > 0:
        print("Hello World!")
        rec_hw(n - 1)


rec_hw(10)

'''
2. 
​# "M" is visually more dense than "o".​
M = ​'land'​
o = ​'water'​
world = [[o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]

- Write a function that prints out all elements of the above board, starting 
from the first element of the first line, till the end. Each line should be read from beginning to end.
- Now write a function that prints out all elements in reverse.
'''

M = 'land'
o = 'water'

world = [[o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]


test_world = [['a', 'b', 'c'],['a', 'b', 'c', 'd'], ['a', 'b', 'c']]

def print_elements_of_list(list_of_list):
    for my_list in list_of_list:
        print(my_list)            

print_elements_of_list(test_world)


def reverse_print(list_of_list):
    i = len(list_of_list)
    while i > 0:
        n = len(list_of_list[i - 1])
        while n > 0:
            print(list_of_list[i - 1][n - 1])
            n -= 1
        i -= 1

reverse_print(test_world)





'''
3. 

a.
- There is one small bug in the continent counter above. Can you find it and fix it? 
    (Hint: change the world so that the continent borders the edge)
b.
- Write a function that generates an n x n sized board with either land or water chosen randomly.
'''


M = 'land'
o = 'water'
world = [
         [M,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,M],
         [o,o,o,o,M,M,M,M,o,o,M],
         [o,o,o,M,M,M,M,M,M,M,o],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]
        ]

def continent_counter(world, x, y):

    if world[y][x] != 'land':
        return 0

    size = 1


    world[y][x] = 'counted land'
 
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    # row above
    if x-1 > 0:
        size = size + continent_counter(world, x-1, y-1)
    #print('first recursion size: ' , size)
    if y-1 > 0:
        size = size + continent_counter(world, x  , y-1)
    if y-1 > 0  and x+1 < len(world[y]):
        size = size + continent_counter(world, x+1, y-1)

    # same row
    if x-1 > 0:
        size = size + continent_counter(world, x-1, y  )
    if x+1 < len(world[y]):
        size = size + continent_counter(world, x+1, y  )

    # row below
    if x-1 > 0 and y+1 < len(world):
        size = size + continent_counter(world, x-1, y+1)
    if y+1 < len(world):
        size = size + continent_counter(world, x  , y+1)
    if x+1 < len(world[y]) and y+1 < len(world):
        size = size + continent_counter(world, x+1, y+1)
    return size

print(continent_counter(world, 10, 5))



# 3. b.
def random_continent_generator(n):

    M = "land"
    o = "water"

    world = []

    for i in range(0, n):
        continent = []
        world.append(continent)
        for i in range(0, n):
            random_num = random.randint(0, 1)
            if random_num == 0:
                continent.append("o")
            else:
                continent.append("M")

    for i in world:
        print(i)

random_continent_generator(6)
random_continent_generator(3)
