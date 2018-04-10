def my_function(STR1,STR2):
    print(STR1, STR2 )


my_function("abc", "vs")
my_function("argument1", "argument2")


def print_something(name="ABC", age=25):
    print("my name is",name, "age is" ,age)
print_something()
print_something("Something ", 22)
#  keyword arguments
print("Below are keyword arguments")
print_something(age=24, name="gndi")


def print_people(*people):
    for person in people:
        print("This person is", person)
print_people("nick", "ram","jack", "dan")

#  return values from function
def do_math(num1, num2):
    return(num1+num2)
math1= do_math(4,6)
math2= do_math(14,61)
print("return values from function")
print("first sum is", math1 , "second sum is", math2)

