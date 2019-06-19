# should_continue = True
# if should_continue:
#     print("Hello")

# known_people = ["John", "Anna", "May"]
# person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))

# if person not in known_people:
#     print("You don't know this person!")

def calculate_balance():
    # TODO: calculate balance
    pass

def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(",")
    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())
    return people_without_spaces

def ask_user():
    person = input("Enter a name of someone: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("You don't know {}!".format(person))

ask_user()