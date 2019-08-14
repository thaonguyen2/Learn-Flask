def methodception(another):
    return another()

def add_two_numbers():
    return 33 + 77

# print(methodception(add_two_numbers))


# lamda function
# print(methodception(lambda: 33 + 77))

my_list = [12, 43, 66, 78]
print(list(filter(lambda x: x != 13, my_list)))

(lambda x: x * 3)(5) # == f(5)
def f(x):
    return x * 3

def not_thirteen(x):
    return x != 13
print(list(filter(not_thirteen, my_list)))

print([x for x in my_list if x != 13])
