'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Erik Milošovič
email: erik.milosovic@gmail.com
discord: erik.m#9937
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

if __name__ == "__main__":

    # Define users
    users = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
    }

    # Input user
    username = input("username:")
    password = input("password:")

    # Check user
    if username not in users or password != users[username]:
        print("unregistered user, terminating the program..")
        exit()

    print("----------------------------------------\n" +
          "Welcome to the app, bob\n" +
          "We have 3 texts to be analyzed.\n" +
          "----------------------------------------")

    # Choose text
    textSelect = input("Enter a number btw. 1 and 3 to select: ")

    # Check input
    if not textSelect.isnumeric():
        print("Inputted not a number, terminating the program..")
        exit()
    textSelect = int(textSelect)
    if textSelect not in range(1, 4):
        print("Inputted number not in range, terminating the program..")
        exit()
    # select text and then split it when there is a space
    splittedText = TEXTS[textSelect - 1].split()

    # Do statistics
    print("There are {} words in the selected text.".format(len(splittedText)))
    print("There are {} titlecase words.".format(
        len([i for i in splittedText if i.istitle()])))
    print("There are {} uppercase words.".format(
        len([i for i in splittedText if i.isupper()])))
    print("There are {} lowercase words.".format(
        len([i for i in splittedText if i.islower()])))
    print("There are {} numeric strings.".format(
        len([i for i in splittedText if i.isnumeric()])))
    print("The sum of all the numbers {}".format(
        sum([int(i) for i in splittedText if i.isnumeric()])))

    # len occurences
    print("----------------------------------------\n" +
          "LEN|  OCCURENCES  |NR.\n" +
          "----------------------------------------")
    maxoccurance = max([len([j for j in splittedText if len(j) == i])
                       for i in range(1, max([len(i) for i in splittedText]) + 1)])
    for i in range(1, max([len(i) for i in splittedText]) + 1):
        # print len part
        print((3 - len(str(i))) * " " + str(i) + "|", end="")
        # print occurences part
        occurences = len([j for j in splittedText if len(j) == i])
        print(("*" * occurences) + (maxoccurance +
              2 - occurences) * " " + "|", end="")
        # print nr part
        print(occurences)
