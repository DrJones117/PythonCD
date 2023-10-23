# basic -----

for i in range(151):
    print(i)

# Multiples os five -----

for i in range(5, 1005, 5):
    print(i)

# Counting, the Dojo Way -----

for i in range(1, 101):
    if i % 5 == 0 and not i % 10 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

# Whoa. That Sucker's Huge -----

sum = 0
for i in range(0, 500000, 1):
    sum = sum + i
    print(sum)

# Countdown by Fours -----

for i in range(2018, -1, -4):
    print(i)

# Flexible Counter -----

low_num = 2
high_num = 9
mult = 3

for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)
