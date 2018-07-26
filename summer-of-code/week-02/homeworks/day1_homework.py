import string

# Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in Alice in Wonderland (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)
# a: 34,560
# b: 5,027
# ...
# z: 893


def letter_counter(filename):
    file = open(filename, "r")

    raw = file.read() 
    table_for_letters = dict()
    for char in string.ascii_lowercase:
        table_for_letters[char] = 0

    for char in raw:
        for key in table_for_letters:
            if char == key:
                table_for_letters[key] += 1

    print(table_for_letters)

    for letter in string.ascii_lowercase:
        print(letter + ": " + str(table_for_letters[letter]))

    return table_for_letters
    

letter_counter("alice_in_wonderland.txt")


      
