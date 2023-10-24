#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# Should return 5 

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Should print undefined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# Should return 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# Should return 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# Should print 5: It actually printed 5, none. That's because the function did return any value.


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# Should be 3, 5, none. The two functions can't be added together since they have no value


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# should be 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# Should print 100, 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# 7, 14, 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

500, 500, 300, 300


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# 500, 500, 300, 300


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# 500, 500, 300, 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# 1. It actually did 1, 3, 2. I forgot you could call a function inside a function.


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# 1, 3, 5, 10