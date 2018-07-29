import string

#### Dictionaries - Things to try

''' 1.
- a. Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, 
    copy in the value, and then delete the old one.

- b. Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.

- c. Create a dictionary with your own personal details, feel free to be creative and funny so 
    for example, you could include key-value pairs with `quirky fact`, `fav quote`, `pet`. 
    Practice adding, modifying, accesing.
'''

#### Optional / Advanced
''' 2.
- Do Python the Hard Way ex. 39 exercises

'''

#### Things to try -Classes
''' 3.
- a. Review the chat reply of today's beautiful class interaction and instantiate a student variable 
    for everyone who shared their dream.

- b. Translate the real world 1MWTT student into a Student class, decide on all the attributes 
    that would be meaningful.

Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy 
but feel free to be creative and add/modify as you see it best! This is the REAL work of a creator 
to find the meaningful description of reality and translate it for computers.
'''

#### Optional, Advanced

''' 4. 
- Come up with a whole taxonomy of Classes for 1MWTT
    - Person()
        - Student()
        - Mentor()
        - Volunteer()
        - Employer()
    Feel free to suggest/invent and also use mixins, decorators, and any other design patterns that you see would help reach the mission of 1 million women to tech by 2020.

'''
# Python the Hard Way ex 30 Study Drills
''' 5.
- Write some more songs using this and make sure you understand that you're passing a list of strings 
    as the lyrics.
- Put the lyrics in a separate variable, then pass that variable to the class to use instead.
- See if you can hack on this and make it do more things. Don't worry if you have no idea how, 
    just give it a try, see what happens. Break it, trash it, thrash it, you can't hurt it.
- Search online for "object-oriented programming" and try to overflow your brain with what you read. 
    Don't worry if it makes absolutely no sense to you. Half of that stuff makes no sense to me too.
'''

# 1. a.

my_dict = {"alma": 52}
print(my_dict)
print(my_dict["alma"])

my_dict["áfonya"] = 54
my_dict["eper"] = 32
my_dict["banán"] = 98

my_dict["ALMA"] = 52
print(my_dict)

del my_dict["alma"]
print(my_dict)


# 1. b.
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


# 1. c.
personal_data = dict()
personal_data["f_name"] = "Aniko"
personal_data["l_name"] = "Barat"
personal_data["country"] = "Hungary"
personal_data["age"] = 30
personal_data["fav_foods"] = ["tomato", "yoghurt", "cottage cheese", "apple"]
print(personal_data)

for i in personal_data["fav_foods"]:
    print(i)

del personal_data["age"]
print(personal_data)

personal_data["country"] = "England"
print(personal_data["country"])

personal_data["full_name"] = "Aniko Barat"
print(personal_data)
del personal_data["f_name"]
del personal_data["l_name"]
print(personal_data)

#### Things to try -Classes
'''3.
- a. Review the chat reply of today's beautiful class interaction and instantiate a student variable 
    for everyone who shared their dream.

- b. Translate the real world 1MWTT student into a Student class, decide on all the attributes 
    that would be meaningful.

Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy 
but feel free to be creative and add/modify as you see it best! This is the REAL work of a creator 
to find the meaningful description of reality and translate it for computers.
'''

# 3. a.


class Student():

    def __init__(self, name, age, dream):
        self.name = name
        self.age = age
        self.dream = dream

    def print_personal_data(self):
        print("Name:", self.name, "Age:", self.age, "Dream:", self.dream)

s1 = Student("Ana", 21, "be healthy & happy")
s2 = Student("Gabrielle", 30, "have a family")
s3 = Student("Rena", 45, "have a new job I love")

s1.print_personal_data()
s2.print_personal_data()
s3.print_personal_data()


class Student_1mwtt():
    
    gender = ''
    
    coding_level = ''
    coding_levels = {1: 'Beginner', 2: 'Intermediate', 3: 'Advanced'}
    
    goal = ''
    goals = {1: 'Find my next job', 2: 'Become a freelancer', 3: 'Start my own tech startup'}
    
    subscribe_to = []
    subscribe_options = {'S': 'Student', 'W': 'Working', 'JS': 'Job seeking', 'E': 'Entrepreneur', 
    'M': 'Mom', 'SM': 'Single Mom', 'NB': 'Non-Binary', 'T': 'Trans', 'R': 'Retired', 
    'C': 'Career changer'} 
    
    extra_role = ''
    extra_roles = {'M': 'Mentor', 'V': 'Volunteer', 'H': 'Hire'}

    
    def __init__(self, f_name, l_name, e_mail, country_code, phone_number, github, country):
        self.f_name = f_name
        self.l_name = l_name
        self.e_mail = e_mail
        self.country_code = country_code
        self.phone_number = phone_number
        self.github = github
        self.country = country
        self.subscribe_to = []

    
    def set_gender(self, gender):
        self.gender = gender_options[gender]

    def set_coding_level(self, coding_level):
        self.coding_level = coding_levels[coding_level]

    def set_goal(self, goal):
        self.goal = goals[goal]

    def set_subscribe_to(self, subscribe_to):
        self.subscribe_to.append(subscribe_to)

    def set_extra_role(self, extra_role):
        self.extra_role = extra_roles[extra_role]
    
s1 = Student_1mwtt('Aniko', 'Barat', 'a@gmail.com', 345, 1234456, 'https://github.com/aB', 'HUN')
#s1.set_coding_level(1)
#s1.set_gender(1)
#s1.set_goal(1)
#s1.set_subscribe_to('JS')
#s1.set_extra_role('V')

print(s1.f_name)
print(s1.l_name)
print(s1.e_mail)
s1.set_subscribe_to(subscribe_options['JS'])