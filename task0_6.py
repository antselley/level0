
def maximum(*args):
    biggest_number = args[0]
    for arg in args: 
        if arg > biggest_number:
            biggest_number = arg
    return biggest_number

print(maximum(5,6,7,2,-4,129))
print(maximum(-40,-5.5,-234))