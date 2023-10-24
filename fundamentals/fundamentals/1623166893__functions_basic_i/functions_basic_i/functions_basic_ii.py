# Challenge 1 -----

def count_down(x):
    new_list = []
    for i in range(x, -1, -1):
        new_list.append(i)
    return new_list

print(count_down(5))

# Challenge 2 -----

v_list = [1, 2]

def print_return(x):
    print(x[0])
    return x[1]

print(print_return(v_list))

# Challenge 3 -----

w_list = [1,2,3,4,5]

def plus_length(x):
    sum = x[0] + len(x)
    return sum


print(plus_length(w_list))

# Challenge 4 -----

x_list = [1]
y_list = [1,3,5,7,9]

def greater_sec(x):
    new_list = []
    counter = 0
    if len(x) < 2:
        return False
    for i in range(0, len(x)):
        if (x[i] > x[1]):
            new_list.append(x[i])
            counter += 1
    print(counter)
    return new_list


print(greater_sec(x_list))
print(greater_sec(y_list))

# Challenge 5 -----

def len_val(x,y):
    new_list = []
    for i in range(0, x, 1):
        new_list.append(y)
    return new_list

print(len_val(4,7))
print(len_val(6,2))

