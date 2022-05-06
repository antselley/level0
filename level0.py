
#### Task 0.1
##################################################
x = 0
y = 1
print(x)
print(y)
x = x + 3
y = y + x
print(x)
print(y)

#Variable assignment just updates what the variable (e.g. x) points to. In this case we change it to point to the integer object 3, so when we add it to y, we are adding 3 rather than the originally assigned value of 0.


#### Task 0.2
##################################################
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a = 1 + 1 * 2 / 2
b = (1 + 1 * 2 ) /  2

# print("x=",x)
# print("y=",y)
# print("z=",z)
# print("a=",a)
# print("b=",b)


#### Task 0.3
##################################################
def hello(input_string): 
    print("Hello ", input_string, "!")

# hello("Ant")

#Not sure if you wanted it to return the output, or print it. Opted for the printing option. 


##### Task 0.4
##################################################
def even_or_odd(input_integer):
    if input_integer % 2 == 0: 
        print("even")
    else:
        print("odd")

# even_or_odd(7)
# even_or_odd(4)
# even_or_odd(104)


##### Task 0.5
##################################################
def area_of_triangle(a,b,c):
    s = (a+b+c)/2 #The Semi Perimeter
    return (  s * (s-a) * (s-b) * (s-c)  )**0.5  #as per Heron's formula /// Raising to the power of 0.5 is the same as taking the square root

# #Test on some easy examples. (Pythongorean triples)
# print(area_of_triangle(3,4,5))
# print(area_of_triangle(6,8,10))


###### Task 0.6
##################################################
First Quick Solution
def maximum(*args):
    biggest_number = args[0]
    for arg in args: 
        if arg > biggest_number:
            biggest_number = arg
    return biggest_number

# print(maximum(5,6,7,2,-4,129))
# print(maximum(-40,-5.5,-234))


###### Task 0.7
##################################################
def celcius_to_farenheit(input_celcius):
    return input_celcius * 1.8 + 32

def farenheit_to_celcius(input_farenheit):
    return (input_farenheit - 32) * (5/9)

# print(celcius_to_farenheit(50))
# print(farenheit_to_celcius(81))


###### Task 0.8
##################################################
def num_to_duration(input_number):
    hours = input_number // 60
    minutes = input_number % 60
    
    if hours == 1:
        hours_wording = "hour"
    else:
        hours_wording = "hours"

    if minutes == 1:
        minutes_wording = "minute"
    else: 
        minutes_wording = "minutes"
    
    print(hours, hours_wording, ",", minutes, minutes_wording)

# num_to_duration(71)
# num_to_duration(133)
# num_to_duration(61)
# num_to_duration(121)

#### Task 0.9
##################################################
def print_vowels(input_string):
    return_list = []
    for char in input_string:
        if (char.lower() in ["a", "e", "i", "o", "u"]) and (return_list.count(char.lower()) == 0) : 
            return_list.append(char.lower())
    print(",".join(return_list))

# print_vowels("Umuzi")
# print_vowels("supercalifragilisticexpialidocious")

## Task 0.10 
##################################################
def common_letters(string1, string2):
    return_list = []
    for char in string1:
        if char.lower() in string2.lower() and return_list.count(char.lower()) ==0: 
            return_list.append(char.lower())
    print(",".join(return_list))
    
# common_letters("House", "Computers")
# common_letters("House", "School")

    